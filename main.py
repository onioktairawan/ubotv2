import asyncio
from scripts import userbot, bot

async def main():
    await asyncio.gather(
        userbot.start(),
        bot.start()
    )

if __name__ == "__main__":
    asyncio.run(main())
