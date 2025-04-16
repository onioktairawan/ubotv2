from telethon import TelegramClient, events
from telethon.errors import ChatAdminRequiredError
from config import API_ID, API_HASH, SESSION_USER

# Membuat client dengan session untuk userbot
client = TelegramClient(SESSION_USER, API_ID, API_HASH)

async def start():
    await client.start()
    print("✅ Userbot aktif")

    # Fitur .pin untuk mem-pin pesan yang di-reply
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

if __name__ == "__main__":
    import asyncio
    asyncio.run(start())

