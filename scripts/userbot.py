from telethon import TelegramClient
from telethon import events
import json

# Load config
with open('data/config.json', 'r') as f:
    config = json.load(f)

api_id = config['api_id']
api_hash = config['api_hash']
phone_number = config['phone_number']

# Setup Telethon userbot client
userbot = TelegramClient('userbot', api_id, api_hash)

async def start():
    await userbot.start(phone_number)
    print("Userbot started!")

@userbot.on(events.NewMessage(pattern=r'.setprefix'))
async def set_prefix(event):
    # Set prefix per user
    new_prefix = event.text.split(' ', 1)[1]
    user_id = event.sender_id
    with open('data/user_data.json', 'r') as f:
        user_data = json.load(f)
    
    user_data['users'][str(user_id)] = user_data['users'].get(str(user_id), {})
    user_data['users'][str(user_id)]['prefix'] = new_prefix

    with open('data/user_data.json', 'w') as f:
        json.dump(user_data, f, indent=4)

    await event.respond(f"Prefix changed to {new_prefix}!")

# Start the userbot
userbot.start()
userbot.run_until_disconnected()
