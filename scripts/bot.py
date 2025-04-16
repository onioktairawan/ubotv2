from telethon import TelegramClient, events, Button
import json
import asyncio

# Load config
with open("config.json") as f:
    config = json.load(f)

API_ID = config["api_id"]
API_HASH = config["api_hash"]
BOT_TOKEN = config["bot_token"]

bot = TelegramClient("bot", API_ID, API_HASH).start(bot_token=BOT_TOKEN)

HEADER = (
    "via @navyfavbot\n"
    "Inline Help\n"
    "Prefixes: g\n"
    "Plugins: 83\n"
    "serpa gengs\n"
    "NavyUbot by @kenapanan\n"
)

# ===== Menu Functions =====
def main_menu():
    text = HEADER
    buttons = [
        [Button.inline("🔹 Pin", b"pin"), Button.inline("🔹 Admin", b"admin"), Button.inline("🔹 Spam", b"spam")],
        [Button.inline("🔹 Dll", b"dll1"), Button.inline("🔹 Dll", b"dll2"), Button.inline("🔹 Dll", b"dll3")],
        [Button.inline("🔹 Dll", b"dll4"), Button.inline("🔹 Dll", b"dll5"), Button.inline("🔹 Dll", b"dll6")],
        [Button.inline("🔹 Prev", b"prev"), Button.inline("🔙 Kembali", b"back_main"), Button.inline("➡️ Next", b"next")]
    ]
    return text, buttons

def pin_menu():
    text = (
        f"{HEADER}\n"
        "**Pin Menu**\n\n"
        "`.pin` — untuk menyematkan pesan.\n"
        "`.unpin` — untuk melepas sematan."
    )
    buttons = [[Button.inline("Kembali", b"back_main")]]
    return text, buttons

def admin_menu():
    text = (
        f"{HEADER}\n"
        "**Admin Menu**\n\n"
        "`.promote` — angkat jadi admin.\n"
        "`.demote` — turunkan admin."
    )
    buttons = [[Button.inline("Kembali", b"back_main")]]
    return text, buttons

def spam_menu():
    text = (
        f"{HEADER}\n"
        "**Spam Menu**\n\n"
        "`.mute` — bisukan pengguna.\n"
        "`.ban` — blokir pengguna."
    )
    buttons = [[Button.inline("Kembali", b"back_main")]]
    return text, buttons

# ===== Event Handlers =====
@bot.on(events.NewMessage(pattern="/menu"))
async def show_menu(event):
    text, buttons = main_menu()
    await event.respond(text, buttons=buttons)

@bot.on(events.CallbackQuery)
async def callback_handler(event):
    data = event.data.decode("utf-8")

    if data == "back_main":
        text, buttons = main_menu()
        await event.edit(text, buttons=buttons)
    elif data == "pin":
        text, buttons = pin_menu()
        await event.respond(text, buttons=buttons)
    elif data == "admin":
        text, buttons = admin_menu()
        await event.respond(text, buttons=buttons)
    elif data == "spam":
        text, buttons = spam_menu()
        await event.respond(text, buttons=buttons)
    else:
        await event.answer("Belum tersedia", alert=True)

# ===== Start Bot =====
async def start():
    print("🤖 Bot aktif")
    await bot.run_until_disconnected()
