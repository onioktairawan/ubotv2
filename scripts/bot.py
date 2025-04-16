import json
from telethon import TelegramClient, events
from telethon.tl.custom import Button

# Membaca konfigurasi dari config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)

API_ID = config["api_id"]
API_HASH = config["api_hash"]
BOT_TOKEN = config["bot_token"]

# Membuat client bot dengan bot token
bot = TelegramClient("bot", API_ID, API_HASH)

async def start():
    await bot.start(bot_token=BOT_TOKEN)
    print("🤖 Bot aktif")

    # Menampilkan menu fitur userbot
    @bot.on(events.NewMessage(pattern="/menu"))
    async def menu_handler(event):
        header = "⚡ **Header**\nVia @navyfavbot\nInline Help Prefixes: g\nPlugins: 83\n\n**Serpa Gengs**\nNavyUbot by @kenapanan"
        features = "🔹 Pin | 🔹 Admin | 🔹 Spam\n🔹 Dll | 🔹 Dll | 🔹 Dll\n🔹 Dll | 🔹 Dll | 🔹 Dll"
        pagination = "🔄 Prev | ➡️ Next"

        # Membuat tombol inline untuk navigation dan pin
        buttons = [
            [Button.inline("Pin", data="pin")],  # Tombol Pin
            [Button.inline("Prev", data="prev"), Button.inline("Next", data="next")]
        ]

        # Kirim pesan dengan inline buttons
        await event.respond(
            f"{header}\n\n{features}\n\n{pagination}",
            buttons=buttons
        )

    # Menangani klik tombol inline
    @bot.on(events.CallbackQuery)
    async def callback_handler(event):
        if event.data == b"prev":
            await event.answer("🔙 Memuat halaman sebelumnya...")
        elif event.data == b"next":
            await event.answer("➡️ Memuat halaman berikutnya...")
        elif event.data == b"pin":
            # Perintah untuk pin pesan
            await event.answer("📌 *Pin message* akan disematkan.")
            await event.respond(".pin \"untuk sematkan pesan\"")  # Perintah pin

    await bot.run_until_disconnected()

if __name__ == "__main__":
    import asyncio
    asyncio.run(start())
