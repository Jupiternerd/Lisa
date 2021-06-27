'''
Author | Shokkunn
'''

from discord.errors import InvalidArgument
import discord, random, re
from discord.ext.commands.errors import BadArgument, BotMissingPermissions, CheckFailure, CommandInvokeError, CommandOnCooldown, DisabledCommand, MemberNotFound, MissingPermissions, NoPrivateMessage, NotOwner, TooManyArguments, UserInputError, UserNotFound
from utilities.constants import consts as constants
from utilities.constant_code import UserBlacklisted, NotInDb
from discord.ext import commands

#reg = "<class\s'discord\.ext\.commands\.errors\.([\w]*)'>"

class Err(commands.Cog):
    ''' 
    purpose | this cog conatains methods to handle errors.
    '''
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(error)
        

        
        ignore = (commands.CommandNotFound, UserBlacklisted, NotInDb)
        err = getattr(error, 'original', error) # We get the original error class.
        print(err.__class__.__name__)
        if (isinstance(err, ignore)): return # If we have to ignore the error.

        user = await ctx.format_user_name() # I cry for I am sad
        error_list = constants.get("on_error") # This is so if we edit the text we don't have to restard for the effect to take place.

        def from_list(name, erList=error_list): # this is for me to not repeat the bottom function over multiple times.
            err_from_list = erList.get(name) or erList.get("Default") 
            
            return err_from_list[random.randrange(0, len(err_from_list))]

        if ctx.cog._get_overridden_method(ctx.cog.cog_command_error) is not None: return #Damn that cog can handle it's own flaws.
        if (hasattr(ctx.command, 'on_error')): return # Damn, that command all grown up enough to handle it's own errors.


        reply = from_list(str(err.__class__.__name__))
        

        if (isinstance(err, CommandOnCooldown)): # If they are on cool down we give a helpful tip.
            retry = int(error.retry_after)
            seconds = str(retry if retry > 1 else "a") + str("s" if retry > 1 else " second")
            

            reply = f"{reply}".format(user= user, seconds= seconds)
        if (isinstance(err, BadArgument)):
            help = ctx.command.help
            
            reply = f"{reply}".format(user= user, help= help)

        if (isinstance(err, BotMissingPermissions)): # If the bot is not getting the big P
            reply = from_list("BotMissingPermissions")
    


            
        
        await ctx.reply(f">>> {reply}".format(user= user), mention_author= False)
        

        #print(isinstance(err, CommandOnCooldown))
        
        

        


      

    
 
def setup(bot):
    bot.add_cog(Err(bot))