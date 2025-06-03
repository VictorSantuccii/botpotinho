import discord
from discord.ext import commands

class PingCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='oi')
    async def ping(self, ctx):
        await ctx.send('meu nome é potinho inho inho, e sou umaa criação do meu desenvolvedor santucci :)')

async def setup(bot):
    await bot.add_cog(PingCommand(bot))
