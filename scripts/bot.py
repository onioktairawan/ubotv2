from telethon import TelegramClient, events
import json

api_id = 123456
api_hash = "your_api_hash"
bot_token = "your_bot_token"

bot = TelegramClient("bot", api_id, api_hash)

async def start():
    await bot.start(bot_token=bot_token)
    print("🤖 Bot aktif")

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
