import asyncio
from start_script import TOKEN
from Commands import Commands
from event_handler import bot


async def main():
    await bot.add_cog(Commands(bot))
    await bot.start(TOKEN)


asyncio.run(main())
