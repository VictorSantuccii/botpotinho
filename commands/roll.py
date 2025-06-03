import random
from discord.ext import commands
import discord

class Roll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="roll")
    async def roll(self, ctx, max_number: int = 6):
        """Rola um dado de 1 até max_number (padrão 6)."""
        if max_number < 1:
            await ctx.send("O número deve ser maior que 0.")
            return

        resultado = random.randint(1, max_number)
        embed = discord.Embed(title="🎲 Resultado do dado!", color=discord.Color.blurple())
        embed.add_field(name="Número rolado", value=str(resultado))
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Roll(bot))
