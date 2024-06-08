import requests

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = '7381031219:AAFwVb54VMFCkz5H1Z6TdF29sMWuXUCmnyI'

# Replace 'YOUR_CHANNEL_ID' with your actual channel ID
CHANNEL_ID = '@aliddpfree'

def send_message():
    message = 'Hello from your Telegram bot!'
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHANNEL_ID}&text={message}'
    response = requests.get(url)
    if response.status_code == 200:
        print('Message sent successfully!')
    else:
        print('Failed to send message.')

if __name__ == "__main__":
    send_message()
