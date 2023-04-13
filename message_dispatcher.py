import requests


def send_msg(message: str) -> None:
    apiToken = "TBD"  # set once a telegram bot is created
    chatID = "TBD"  # set once a telegram bot is created
    apiURL = f"https://api.telegram.org/bot{apiToken}/sendMessage"

    try:
        response = requests.post(apiURL, json={"chat_id": chatID, "text": message})
        print(response.text)
    except Exception as e:
        print(e)
