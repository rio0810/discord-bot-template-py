from discord.ext import commands


class Hello1(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hello1', help='挨拶します')
    async def hello(self, ctx):
        await ctx.send('こんにちは！よろしくお願いします')


async def setup(bot):
    await bot.add_cog(Hello1(bot))
