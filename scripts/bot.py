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


async def start():
    await bot.start(bot_token=BOT_TOKEN)
    print("🤖 Bot aktif")

    # Menu utama saat /menu dikirim
    @bot.on(events.NewMessage(pattern="/menu"))
    async def show_menu(event):
        header = (
            "via @navyfavbot\n"
            "Inline Help\n"
            "Prefixes: g\n"
            "Plugins: 83\n"
            "serpa gengs\n"
            "NavyUbot by @kenapanan\n"
        )

        buttons = [
            [Button.inline("🔹 Pin", b"pin"), Button.inline("🔹 Admin", b"admin"), Button.inline("🔹 Spam", b"spam")],
            [Button.inline("🔹 Dll", b"dll1"), Button.inline("🔹 Dll", b"dll2"), Button.inline("🔹 Dll", b"dll3")],
            [Button.inline("🔹 Dll", b"dll4"), Button.inline("🔹 Dll", b"dll5"), Button.inline("🔹 Dll", b"dll6")],
            [Button.inline("🔄 Prev", b"prev"), Button.inline("🔙 Kembali", b"back"), Button.inline("➡️ Next", b"next")]
        ]

        await event.respond(header, buttons=buttons)

    # Handle saat tombol ditekan
    @bot.on(events.CallbackQuery)
    async def callback_handler(event):
        data = event.data.decode("utf-8")

        if data == "pin":
            await event.respond("🔹 **Pin Menu**\n\n`.pin` — untuk menyematkan pesan.\n`.unpin` — untuk melepas sematan.")
        elif data == "admin":
            await event.respond("🔹 **Admin Menu**\n\n`.promote` — angkat jadi admin.\n`.demote` — turunkan admin.")
        elif data == "spam":
            await event.respond("🔹 **Spam Menu**\n\n`.mute` — bisukan pengguna.\n`.ban` — blokir pengguna.")
        else:
            await event.answer("Belum ada konten untuk tombol ini", alert=True)
