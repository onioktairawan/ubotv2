import json
from telethon import TelegramClient, events

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
        try:
            with open("shared/features_list.json") as f:
                data = json.load(f)
            fitur = "\n".join(f"🔹 {f}" for f in data.get("userbot_features", []))
            await event.respond(f"📋 Fitur Userbot:\n\n{fitur}")
        except Exception as e:
            await event.respond(f"❌ Gagal memuat fitur: {e}")

    await bot.run_until_disconnected()

if __name__ == "__main__":
    import asyncio
    asyncio.run(start())
