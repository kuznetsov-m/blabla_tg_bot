import requests
import os

def generate_audio_file(message: str, file_path: str, x_csrf_token: str, xsrf_token: str):
    message = message[:5000]

    speed = 1.1
    voices = ['alyss', 'jane', 'oksana', 'omazh', 'zahar', 'ermil', 'alena', 'filipp']
    voice = voices[6]
    emotions = ['good', 'evil', 'neutral']
    emotion = emotions[0]
    languages = ['ru-RU', 'en-US', 'tr-TR']
    language = languages[0]

    url = 'https://cloud.yandex.ru/api/speechkit/tts'
    headers = {
        'Host': 'cloud.yandex.ru',
        'Connection': 'keep-alive',
        # 'Content-Length': '254',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'Accept': 'application/json, text/plain, */*',
        'x-csrf-token': f'{x_csrf_token}',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://cloud.yandex.ru',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://cloud.yandex.ru/services/speechkit',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.9',
        'Cookie': f'ymex=1939202819.yrts.1623842819#1939202819.yrtsi.1623842819; yandexuid=6792193101623842819; yuidss=6792193101623842819; i=Oeun+pMCrTrnR8/i5fd5OKZvBaG1mnhurGxj+6+Y3N1qCEtgMPgTHgV3K55kmGJh2OeZViMDwR3VD3qGiPAoopC4baQ=; is_gdpr=0; is_gdpr_b=CJ3XLxD9NA==; skid=9325928121624017196; gdpr=0; _ym_uid=1624017199990790668; _ym_d=1624017199; session-geo-data=eyJyZWdpb25OYW1lIjoi0JzQvtGB0LrQstCwINC4INCc0L7RgdC60L7QstGB0LrQsNGPINC%2B0LHQu9Cw0YHRgtGMIiwiY291bnRyeU5hbWUiOiLQoNC%2B0YHRgdC40Y8iLCJ0aW1lem9uZSI6IkV1cm9wZS9Nb3Njb3ciLCJsb2NhbGUiOnsiY29kZSI6InJ1LVJVIiwibmFtZSI6ItCg0L7RgdGB0LjRjyAo0KDRg9GB0YHQutC40LkpIiwibGFuZyI6InJ1IiwibGFuZ05hbWUiOiLQoNGD0YHRgdC60LjQuSIsInJlZ2lvbiI6InJ1IiwicmVnaW9uTmFtZSI6ItCg0L7RgdGB0LjRjyIsImN1cnJlbmN5IjoiUlVCIiwidGxkIjoicnUiLCJvcmRlciI6MX19; XSRF-TOKEN={xsrf_token}; _ym_isad=2; _ym_visorc=w'
    }

    body = f'{{"message":"{message}","language":"{language}","speed":{speed},"voice":"{voice}","emotion":"{emotion}","format":"oggopus"}}'

    req = requests.post(url, headers=headers, data=body.encode('utf-8'))

    print(req.status_code)

    f = open(file_path, 'wb')
    f.write(req.content)
    f.close()