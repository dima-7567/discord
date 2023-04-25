import asyncio
from Commands import Commands
from event_handler import bot
from CONSTS import TOKEN
import logging
from data import db_session


async def main():
    await bot.add_cog(Commands(bot))
    db_session.global_init("db/blogs.db")
    await bot.start(TOKEN)


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

asyncio.run(main())

