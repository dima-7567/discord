import discord

TOKEN = "MTA4MTU4OTcwMjczOTYyODEwNA.G-PPP1.5ZpVhdf07IiuzwwzQ9p1RGH26o7WtFKHpm5P44"

intents = discord.Intents.default()
client = discord.Client(intents=intents)
client.run(TOKEN)