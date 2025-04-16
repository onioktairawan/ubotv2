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
        header = (
            "⚡ **Header**\n"
            "Via @navyfavbot\n"
            "Inline Help\n"
            "Prefixes: g\n"
            "Plugins: 83\n\n"
            "**Serpa Gengs**\n"
            "NavyUbot by @usnownerbot"
        )

        # Daftar fitur
        features = (
            "🔹 Pin | 🔹 Admin | 🔹 Spam\n"
            "🔹 Dll | 🔹 Dll | 🔹 Dll\n"
            "🔹 Dll | 🔹 Dll | 🔹 Dll"
        )

        # Tombol untuk navigasi dan fitur
        buttons = [
            [Button.inline("Pin", data="pin")],
            [Button.inline("Admin", data="admin")],
            [Button.inline("Spam", data="spam")],
            [Button.inline("Prev", data="prev"), Button.inline("Kembali", data="back"), Button.inline("Next", data="next")]
        ]

        # Kirim pesan dengan inline buttons
        await event.respond(
            f"{header}\n\n{features}",
            buttons=buttons
        )

    # Menangani klik tombol inline
    @bot.on(events.CallbackQuery)
    async def callback_handler(event):
        if event.data == b"prev":
            await event.answer("🔙 Memuat halaman sebelumnya...")
        elif event.data == b"next":
            await event.answer("➡️ Memuat halaman berikutnya...")
        elif event.data == b"back":
            await event.answer("🔄 Kembali ke menu utama.")
        elif event.data == b"pin":
            # Menampilkan deskripsi untuk Pin
            await event.answer("📌 *Pin message* akan disematkan. Gunakan `.pin \"pesan yang ingin dipin\"` untuk menyematkan pesan.")
        elif event.data == b"admin":
            # Menampilkan deskripsi untuk Admin
            await event.answer("👑 *Admin* fitur untuk mengelola grup dan user. Gunakan perintah seperti `.ban`, `.mute`, dll.")
        elif event.data == b"spam":
            # Menampilkan deskripsi untuk Spam
            await event.answer("🚫 *Spam* fitur untuk mengatasi pesan spam dalam grup. Gunakan `.spam` untuk mengaktifkan fitur ini.")
        
    await bot.run_until_disconnected()

if __name__ == "__main__":
    import asyncio
    asyncio.run(start())
