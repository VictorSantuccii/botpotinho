from discord.ext import commands
import discord

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help_command(self, ctx):
        embed = discord.Embed(
            title="📚 Ajuda - Comandos do Potinho",
            description="Aqui estão todos os comandos disponíveis!\n\n✨ **Use com carinho.**",
            color=discord.Color.purple()
        )

        # 📌 Utilitários
        embed.add_field(name="🔧 Utilitários", value=(
            "🔹 **p!ping** – Testa a latência do bot\n"
            "🎲 **p!roll [número]** – Rola um dado até o número escolhido (padrão 6)\n"
            "👤 **p!userinfo [@usuário]** – Mostra informações do usuário\n"
            "🏠 **p!serverinfo** – Mostra informações do servidor\n"
            "🖼️ **p!avatar [@usuário]** – Mostra o avatar do usuário"
        ), inline=False)

        # 🎉 Social / Interações
        embed.add_field(name="💞 Social & Interações", value=(
            "🤗 **p!abraçar [@usuário]** – Envia um abraço bem apertado\n"
            "💋 **p!beijar [@usuário]** – Dá um beijinho virtual\n"
            "👋 **p!tapa [@usuário]** – Dá um tapinha (de leve, viu?)\n"
            "❤️ **p!ship [@usuário1] [@usuário2]** – Calcula o amor entre dois usuários\n"
            "🎯 **p!par [@cargo]** – Sorteia dois membros com o cargo escolhido"
        ), inline=False)

        embed.set_footer(text="Use o prefixo !p antes de executar qualquer comando. | 💖 Aproveite o potinho inho inho :)")
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Help(bot))
