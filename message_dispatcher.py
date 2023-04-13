from typing import List 
import requests


def send_msg(message: str) -> None:

    apiToken = 'TBD'
    chatID = 'TBD'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)
