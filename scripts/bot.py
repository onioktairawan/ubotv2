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

    # Command /menu
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

    # Callback handler
    @bot.on(events.CallbackQuery)
    async def feature_detail(event):
        fitur = {
            b"pin": ".pin - untuk menyematkan pesan",
            b"admin": ".admin - fitur admin grup",
            b"spam": ".spam - untuk mengatur spam",
            b"dll1": ".dll1 - deskripsi fitur dll1",
            b"dll2": ".dll2 - deskripsi fitur dll2",
            b"dll3": ".dll3 - deskripsi fitur dll3",
            b"dll4": ".dll4 - deskripsi fitur dll4",
            b"dll5": ".dll5 - deskripsi fitur dll5",
            b"dll6": ".dll6 - deskripsi fitur dll6",
            b"prev": "🔄 Kembali ke halaman sebelumnya",
            b"back": "🔙 Menutup menu",
            b"next": "➡️ Menu selanjutnya"
        }

        data = event.data
        jawaban = fitur.get(data, "❓ Tidak diketahui")
        await event.answer(jawaban, alert=True)

    await bot.run_until_disconnected()

if __name__ == "__main__":
    import asyncio
    asyncio.run(start())
