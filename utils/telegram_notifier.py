import requests

from library_service.settings import TELEGRAM_BOT_TOKEN, CHAT_ID


def send_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
    requests.get(url)
