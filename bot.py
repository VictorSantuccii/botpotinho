import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)


async def load_extensions():
    await bot.load_extension("commands.ping")
    await bot.load_extension("commands.avatar")
    await bot.load_extension("commands.userinfo")
    await bot.load_extension("commands.serverinfo")
    await bot.load_extension("commands.roll")
    await bot.load_extension("commands.help")
    
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')

async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)

import asyncio
asyncio.run(main())
