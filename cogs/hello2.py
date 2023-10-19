from discord.ext import commands


class Hello2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hello2', help='挨拶します')
    async def hello(self, ctx):
        await ctx.send('こんにちは！')


async def setup(bot):
    await bot.add_cog(Hello2(bot))
