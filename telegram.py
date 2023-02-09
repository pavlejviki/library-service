import requests
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def send_message(user, borrowing):
    text = (
        f"Borrowing created successfully on {borrowing.borrow_date} "
        f'for book "{borrowing.book_id.title}"'
        f' with expected return date "{borrowing.expected_return_date}" for user {user.first_name} {user.last_name}'
    )
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}"
    requests.get(url)
