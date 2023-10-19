import discord
from discord.ext import commands
import asyncio
import json

json_file_path = 'data/config.json'
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)


token = data['token']
prefix = data['prefix']
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=intents)
initial_extensions = ['cogs.hello1', 'cogs.hello2']


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


async def load_extension():
    for cog in initial_extensions:
        await bot.load_extension(cog)


async def main():
    async with bot:
        await load_extension()
        await bot.start(token)

asyncio.run(main())
