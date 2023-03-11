import asyncio
from Commands import Commands
from event_handler import bot
from CONSTS import TOKEN


async def main():
    await bot.add_cog(Commands(bot))
    await bot.start(TOKEN)


asyncio.run(main())
