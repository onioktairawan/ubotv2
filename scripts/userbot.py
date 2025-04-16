from telethon import TelegramClient, events
from telethon.errors import ChatAdminRequiredError
import asyncio

api_id = 123456        # Ganti dengan milikmu
api_hash = "your_api_hash"
session = "user"       # Session name

client = TelegramClient(session, api_id, api_hash)

async def start():
    await client.start()
    print("✅ Userbot aktif")

    @client.on(events.NewMessage(outgoing=True, pattern=r"\.pin"))
    async def pin_handler(event):
        if event.is_reply:
            reply_msg = await event.get_reply_message()
            try:
                await reply_msg.pin()
                await event.respond("📌 Pesan berhasil di-pin.")
            except ChatAdminRequiredError:
                await event.respond("❌ Gagal: butuh akses admin untuk pin pesan.")
            except Exception as e:
                await event.respond(f"❌ Error: {e}")
        else:
            await event.respond("↩️ Balas pesan yang ingin kamu pin, lalu ketik `.pin`")

    await client.run_until_disconnected()
