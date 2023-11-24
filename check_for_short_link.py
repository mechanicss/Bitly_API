import requests, os
from dotenv import load_dotenv


def shorten_link(token, user_input):

    link = 'https://api-ssl.bitly.com/v4/shorten'

    headers = {
        'Authorization': f'Bearer {token}',
    }

    payload = {
        'long_url': user_input,
    }

    response = requests.post(url=link, headers=headers, json=payload, timeout=5)
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


def is_bitlink(url_input, token):
    try:
        count_clicks(token, bitlink=url_input)
        return True
    
    except requests.exceptions.HTTPError as ex:
        return False


if __name__ == '__main__':
    load_dotenv()
    token = os.environ['BITLINK_TOKEN']

    url_input  = input('Укажите ссылку: ')

    bitlink_status = is_bitlink(url_input, token)

    if bitlink_status:
        print(count_clicks(token, bitlink=url_input), 'кликов')
    else:
        print('Битлинк', shorten_link(token, user_input=url_input))

