from .commands import Commands


def setup(bot):
    n = Commands()
    bot.add_cog(n)
