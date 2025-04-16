import json
from telethon import TelegramClient, events
from telethon.tl.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telethon.tl.custom import Button

# Load config
with open("config.json", "r") as f:
    config = json.load(f)

API_ID = config["api_id"]
API_HASH = config["api_hash"]
BOT_TOKEN = config["bot_token"]

bot = TelegramClient("bot", API_ID, API_HASH)

# Template menu utama
def main_menu():
    header = (
        "via @navyfavbot\n"
        "Inline Help\n"
        "Prefixes: g\n"
        "Plugins: 83\n"
        "serpa gengs\n"
        "NavyUbot by @kenapanan"
    )
    buttons = [
        [Button.inline("Pin", b"pin"), Button.inline("Admin", b"admin"), Button.inline("Spam", b"spam")],
        [Button.inline("Dll", b"dll1"), Button.inline("Dll", b"dll2"), Button.inline("Dll", b"dll3")],
        [Button.inline("Dll", b"dll4"), Button.inline("Dll", b"dll5"), Button.inline("Dll", b"dll6")],
        [Button.inline("Prev", b"prev"), Button.inline("Kembali", b"back_main"), Button.inline("Next", b"next")]
    ]
    return header, buttons

# Menu deskripsi fitur
def pin_menu():
    text = (
        "**Pin Menu**\n\n"
        "`.pin` — untuk menyematkan pesan.\n"
        "`.unpin` — untuk melepas sematan."
    )
    buttons = [[Button.inline("Kembali", b"back_main")]]
    return text, buttons

def admin_menu():
    text = (
        "**Admin Menu**\n\n"
        "`.promote` — angkat jadi admin.\n"
        "`.demote` — turunkan admin."
    )
    buttons = [[Button.inline("Kembali", b"back_main")]]
    return text, buttons

def spam_menu():
    text = (
        "**Spam Menu**\n\n"
        "`.mute` — bisukan pengguna.\n"
        "`.ban` — blokir pengguna."
    )
    buttons = [[Button.inline("Kembali", b"back_main")]]
    return text, buttons

async def start():
    await bot.start(bot_token=BOT_TOKEN)
    print("🤖 Bot aktif")

    # Perintah /menukeyboard untuk menampilkan atau menyembunyikan tombol
    @bot.on(events.NewMessage(pattern="/menukeyboard"))
    async def toggle_keyboard(event):
        msg_text = event.raw_text.strip().lower()
        if "menu" in msg_text:
            keyboard = ReplyKeyboardMarkup(
                rows=[
                    [KeyboardButton("/start")],
                    [KeyboardButton("/menu")],
                    [KeyboardButton("/restart")],
                    [KeyboardButton("Tutup")]
                ],
                resize=True
            )
            await event.respond("📋 Menu ditampilkan.", buttons=keyboard)
        elif "tutup" in msg_text:
            await event.respond("🗂️ Menu disembunyikan.", buttons=ReplyKeyboardRemove())

    # Respon terhadap tombol "Tutup"
    @bot.on(events.NewMessage(pattern="Tutup"))
    async def close_keyboard(event):
        await event.respond("✅ Menu ditutup.", buttons=ReplyKeyboardRemove())

    # /start default
    @bot.on(events.NewMessage(pattern="/start"))
    async def start_cmd(event):
        keyboard = ReplyKeyboardMarkup(
            rows=[
                [KeyboardButton("Menu")],
            ],
            resize=True
        )
        await event.respond("Selamat datang!\nKlik 'Menu' untuk melihat perintah.", buttons=keyboard)

    # /menu = tampilkan inline menu
    @bot.on(events.NewMessage(pattern="/menu"))
    async def show_menu(event):
        header, buttons = main_menu()
        await event.respond(header, buttons=buttons)

    @bot.on(events.CallbackQuery)
    async def callback_handler(event):
        data = event.data.decode("utf-8")

        if data == "pin":
            text, buttons = pin_menu()
            await event.edit(text, buttons=buttons)
        elif data == "admin":
            text, buttons = admin_menu()
            await event.edit(text, buttons=buttons)
        elif data == "spam":
            text, buttons = spam_menu()
            await event.edit(text, buttons=buttons)
        elif data == "back_main":
            header, buttons = main_menu()
            await event.edit(header, buttons=buttons)
        else:
            await event.answer("Belum tersedia.", alert=True)

if __name__ == "__main__":
    import asyncio
    asyncio.run(start())
