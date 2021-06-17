'''
Author | Shokkunn
'''

from discord.errors import InvalidArgument
from utilities.dBframeworks.schematics import User
import discord, random, re
from discord.ext.commands.errors import BadArgument, BotMissingPermissions, CommandInvokeError, CommandOnCooldown, DisabledCommand, MemberNotFound, MissingPermissions, NoPrivateMessage, NotOwner, TooManyArguments, UserInputError
from utilities.constants import consts as constants
from utilities.constant_code import UserBlacklisted
from discord.ext import commands

reg = "<class\s'discord\.ext\.commands\.errors\.([\w]*)'>"

class Err(commands.Cog):
    '''
    purpose | this cog conatains methods to handle errors.
    '''
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):


        screened = re.match(reg, str(error.__class__))
        print(screened)
        print(error.with_traceback)

        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return

        if hasattr(ctx.command, 'on_error'): 
            return
        err = constants["on_error"]
        string = screened[1] or "unknown"
        #print(string)
        appendStr = "";

        ignored = (commands.CommandNotFound, UserBlacklisted)

        if isinstance(error, ignored): return
        
        

        if isinstance(error, CommandOnCooldown):
            #error.retry_after = double , cast it to int and then to str.
            seconds = str("**" + str(int(error.retry_after)) + "**") if int(error.retry_after) > 1 else "a" or "zero"
            appendStr = str(f"{seconds} second") + str("s" if int(error.retry_after) > 1 else "") + "!"

        if isinstance(error, UserInputError): 
            print("YES")
     
            appendStr = discord.utils.find(lambda cmd: cmd.name == str(ctx.command.name), self.bot.commands).help or None
            
            
        if string == "unknown": print(error)
        
        errString = ">>> " + err[string][random.randrange(0, len(err[string]))] + f" {appendStr}";
        
        



        
        return await ctx.reply(errString, mention_author=False)

    
 
def setup(bot):
    bot.add_cog(Err(bot))