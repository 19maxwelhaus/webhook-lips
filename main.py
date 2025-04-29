from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = '7944590947:AAGzJ9xsQVeiAnAcpSy8rOSx5SgCtB8Fk-Q'
CHAT_ID = '383196764'

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    print("Прийнято:", data)

    username = data.get('username', 'невідомо')

    message = f"🔔 Оплата підтверджена!\nКлієнт: https://instagram.com/{username}\nПеревір вручну."

    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }

    requests.post(telegram_url, json=payload)
    return 'ok', 200

if __name__ == '__main__':
    app.run()
