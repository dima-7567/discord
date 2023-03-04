import asyncio
from typing import Any

import discord
from discord import client
from discord.ext import commands
import random, logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

TOKEN = "MTA4MTU4OTcwMjczOTYyODEwNA.G-PPP1.5ZpVhdf07IiuzwwzQ9p1RGH26o7WtFKHpm5P44"

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='/', intents=intents)


class YLBotClient(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.command()
    async def foo(self, arg):
        await self.bot.send(arg)


async def main():
    await bot.add_cog(YLBotClient(bot))
    await bot.start(TOKEN)


asyncio.run(main())

