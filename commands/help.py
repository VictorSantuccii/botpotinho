from discord.ext import commands
import discord

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help_command(self, ctx):
        embed = discord.Embed(title="Ajuda - Comandos do Bot", color=discord.Color.green())
        embed.add_field(name="!ping", value="Testa a latência do bot", inline=False)
        embed.add_field(name="!roll [número]", value="Rola um dado de 1 até o número especificado (padrão 6)", inline=False)
        embed.add_field(name="!userinfo [@usuário]", value="Mostra informações sobre o usuário", inline=False)
        embed.add_field(name="!serverinfo", value="Mostra informações sobre o servidor", inline=False)
        embed.add_field(name="!avatar [@usuário]", value="Mostra o avatar do usuário", inline=False)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Help(bot))
