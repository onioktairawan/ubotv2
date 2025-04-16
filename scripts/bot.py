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

# Menu Utama
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

    # Menangani perintah /menu
    @bot.on(events.NewMessage(pattern="/menu"))
    async def show_menu(event):
        header, buttons = main_menu()
        await event.respond(header, buttons=buttons)

    # Menangani klik tombol inline
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
        elif data == "dll1":
            await event.answer("DLL 1 Selected!", alert=True)
        elif data == "dll2":
            await event.answer("DLL 2 Selected!", alert=True)
        elif data == "dll3":
            await event.answer("DLL 3 Selected!", alert=True)
        elif data == "dll4":
            await event.answer("DLL 4 Selected!", alert=True)
        elif data == "dll5":
            await event.answer("DLL 5 Selected!", alert=True)
        elif data == "dll6":
            await event.answer("DLL 6 Selected!", alert=True)
        elif data == "prev":
            await event.answer("Previous action selected!")
        elif data == "next":
            await event.answer("Next action selected!")

if __name__ == "__main__":
    import asyncio
    asyncio.run(start())
