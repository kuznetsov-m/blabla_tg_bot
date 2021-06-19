import telebot
import re
import requests
from telebot import types
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import yandex_speechkit

token = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(token)

def get_iq_articles():
    article = types.InlineQueryResultArticle(
        id='1',
        title='Озувучить!',
        # description='description',
        input_message_content=types.InputTextMessageContent(
            message_text='voice'
        )
    )
    return [article]

def generate_audio_file(text: str):
    file_path = 'audio.ogg'
    yandex_speechkit.generate_audio_file(
        message=f'Этого бота собрал. @kuznets+ov1024. {text}',
        file_path=file_path,
        x_csrf_token=os.getenv('X_CSRF_TOKEN'),
        xsrf_token=os.getenv('XSRF_TOKEN')
    )

def get_audio_file_id(text: str) -> str:
    generate_audio_file(text)
    with open('audio.ogg', 'rb') as audio:
        payload = {
            'chat_id': int(os.getenv('ADMIN_USER_ID')),
            'title': 'Озвучить!',
            'parse_mode': 'HTML'
        }
        files = {
            'audio': audio.read(),
        }
        resp = requests.post(
            "https://api.telegram.org/bot{token}/sendAudio".format(token=token),
            data=payload,
            files=files).json()

        file_id = resp.get('result').get('audio').get('file_id')

    return file_id

@bot.inline_handler(func=lambda query: len(query.query) > 0)
def query_text(query):
    file_id = get_audio_file_id(query.query)
    inline_btn = types.InlineQueryResultCachedAudio(id='1', caption=query.query, audio_file_id=file_id)
    bot.answer_inline_query(query.id, [inline_btn])

bot.polling(none_stop=True)