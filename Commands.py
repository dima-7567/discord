import discord
from discord.ext import commands
import random
from discord.ext import commands
from start_script import intents
from apps import get_cat
import asyncio


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='randint')
    async def my_randint(self, ctx, min_int, max_int):
        num = random.randint(int(min_int), int(max_int))
        await ctx.send(num)

    @commands.command(name='set_timer')
    async def timer(self, ctx, *time):
        # $set_timer in 0 minutes 3 seconds
        minutes = int(time[1])
        seconds = int(time[3])
        await asyncio.sleep(60 * minutes + seconds)
        await ctx.send('Time X has come')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content[0] != '$':
            if message.author == self.bot.user:
                    return
            if "кот" in message.content.lower():
                await message.channel.send(get_cat())
            else:
                await message.channel.send("Хочешь кота")

