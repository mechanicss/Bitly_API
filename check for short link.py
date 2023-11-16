import requests, os
from dotenv import load_dotenv


load_dotenv()
token = os.environ['TOKEN']


def shorten_link(token, user_input):

    link = 'https://api-ssl.bitly.com/v4/shorten'

    headers = {
        'Authorization': f'Bearer {token}',
    }

    data = {
        'long_url': user_input,
    }

    response = requests.post(url=link, headers=headers, json=data, timeout=5)
    response.raise_for_status()

    return response.json().get('id')


def count_clicks(token, bitlink):

    link = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'

    headers = {
        'Authorization': f'Bearer {token}',
    }

    params = {
        'units': '-1',
    }

    response = requests.get(url=link, headers=headers, params=params, timeout=5)
    response.raise_for_status()

    return response.json().get('total_clicks')


def is_bitlink(url_input):
    try:
        print(count_clicks(token, bitlink=url_input), 'кликов')
    except requests.exceptions.HTTPError as ex:
        try:
            print('Битлинк', shorten_link(token, user_input=url_input))
        except requests.exceptions.HTTPError as ex:
            exit(ex)


if __name__ == '__main__':

    is_bitlink(input('Укажите ссылку: \n'))

