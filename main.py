import asyncio
from scripts import userbot, bot

async def main():
    await asyncio.gather(
        userbot.start(),
        bot.start()
    )

asyncio.run(main())
