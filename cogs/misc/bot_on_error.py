'''
Author | Shokkunn
'''
import discord
from utilities.constants import consts as constants
from discord.ext import commands

class Err(commands.Cog):
    '''
    purpose | this cog conatains methods to handle errors.
    '''
    def __init__(self, bot):
        self.bot = bot
    '''
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        err = constants["on_error"]
        string = "unknown"
        if hasattr(ctx.command, 'on_error'): return

        ignored = (commands.CommandNotFound)

        if isinstance(error, ignored): return
        if isinstance(error, commands.DisabledCommand): 
            string = "disabled"
        if isinstance(ctx.channel, discord.channel.DMChannel):
            string = "in_dms"

        errString = ">>> " + err[string]
        if string is "unknown": print(error)
        return await ctx.reply(errString)
    '''
 
def setup(bot):
    bot.add_cog(Err(bot))