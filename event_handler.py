from discord.ext import commands
from start_script import intents


bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "привет" in message.content.lower():
        await message.channel.send("И тебе привет")
    else:
        await message.channel.send("Спасибо за сообщение")