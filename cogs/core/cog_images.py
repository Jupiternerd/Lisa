'''
Author | Shokkunn
'''

from discord.ext.commands import bot
from discord.ext import commands

class Images(commands.Cog, name="Images"):
    pass


def setup(bot):
    bot.add_cog(Images(bot))