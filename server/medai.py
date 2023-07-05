from telebot import TeleBot
from dotenv import load_dotenv
import os

load_dotenv()

bot_token = os.getenv("bot_token")

bot = TeleBot(bot_token)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hi! Welcome to ResQbot, What's your emergency")

@bot.message_handler(content_types=["voice"])
def voice_message_handler(message):
    voice = message.voice

    duration = voice.duration  # in seconds
    bot.reply_to(message, f"Your voice message is {duration} seconds long.")

    file_id = voice.file_id
    bot.reply_to(message, "Your emergency is recorded and processed. The file identifier for you voice message is: " + file_id)

    file_info = bot.get_file(file_id)
    file_path = file_info.file_path  # file path on Telegram server
    url = f"https://api.telegram.org/file/bot{bot.token}/{file_path}"
    print(url)
    return url

bot.polling()
