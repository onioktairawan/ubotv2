from threading import Thread
from scripts.bot import client
from scripts.userbot import start, userbot

def start_bot():
    client.run_until_disconnected()

def start_userbot():
    userbot.start(phone_number)
    userbot.run_until_disconnected()

if __name__ == "__main__":
    bot_thread = Thread(target=start_bot)
    userbot_thread = Thread(target=start_userbot)

    bot_thread.start()
    userbot_thread.start()

    bot_thread.join()
    userbot_thread.join()
