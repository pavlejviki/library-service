import requests
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
def send_message(bot_token, chat_id, text):
    print(TELEGRAM_BOT_TOKEN)
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={text}"
    response = requests.get(url)
    return print(response.json())


send_message(TELEGRAM_BOT_TOKEN, CHAT_ID, "hello")