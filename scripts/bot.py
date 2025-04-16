import json
from telethon import TelegramClient, events
from telethon.tl.custom import Button

# Load config
with open("config.json", "r") as f:
    config = json.load(f)

API_ID = config["api_id"]
API_HASH = config["api_hash"]
BOT_TOKEN = config["bot_token"]

bot = TelegramClient("bot", API_ID, API_HASH)

# Status halaman
current_page = 1

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
        [Button.inline("Next", b"next")]
    ]
    return header, buttons

# Menu halaman kedua dengan tombol Dll 3x4
def second_page_menu():
    text = (
        "**Halaman Kedua**\n\n"
        "Ini adalah halaman kedua.\n"
        "Pilih opsi berikut."
    )
    buttons = [
        [Button.inline("Dll", b"dll7"), Button.inline("Dll", b"dll8"), Button.inline("Dll", b"dll9")],
        [Button.inline("Dll", b"dll10"), Button.inline("Dll", b"dll11"), Button.inline("Dll", b"dll12")],
        [Button.inline("Dll", b"dll13"), Button.inline("Dll", b"dll14"), Button.inline("Dll", b"dll15")],
        [Button.inline("Dll", b"dll16"), Button.inline("Dll", b"dll17"), Button.inline("Dll", b"dll18")],
        [Button.inline("Prev", b"prev"), Button.inline("Kembali", b"back_main"), Button.inline("Next", b"next")]
    ]
    return text, buttons

# Menu deskripsi fitur
def pin_menu():
    text = (
        "**Pin Menu**\n\n"
        "`.pin` — untuk menyematkan pesan.\n"
        "`.unpin` — untuk melepas sematan."
    )
    buttons = [
        [Button.inline("Kembali", b"back_main")]
    ]
    return text, buttons

def admin_menu():
    text = (
        "**Admin Menu**\n\n"
        "`.promote` — angkat jadi admin.\n"
        "`.demote` — turunkan admin."
    )
    buttons = [
        [Button.inline("Kembali", b"back_main")]
    ]
    return text, buttons

def spam_menu():
    text = (
        "**Spam Menu**\n\n"
        "`.mute` — bisukan pengguna.\n"
        "`.ban` — blokir pengguna."
    )
    buttons = [
        [Button.inline("Kembali", b"back_main")]
    ]
    return text, buttons

async def start():
    await bot.start(bot_token=BOT_TOKEN)
    print("🤖 Bot aktif")

    @bot.on(events.NewMessage(pattern="/menu"))
    async def show_menu(event):
        global current_page
        if current_page == 1:
            header, buttons = main_menu()
        else:
            header, buttons = second_page_menu()
        await event.respond(header, buttons=buttons)

    @bot.on(events.CallbackQuery)
    async def callback_handler(event):
        global current_page
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
            current_page = 1  # Reset ke halaman utama
            header, buttons = main_menu()
            await event.edit(header, buttons=buttons)
        elif data == "next":
            current_page = 2  # Pindah ke halaman kedua
            header, buttons = second_page_menu()
            await event.edit(header, buttons=buttons)
        elif data == "prev":
            current_page = 1  # Kembali ke halaman pertama
            header, buttons = main_menu()
            await event.edit(header, buttons=buttons)
        else:
            await event.answer("Belum tersedia.", alert=True)
