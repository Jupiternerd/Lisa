'''
Author | Shokkunn
'''


import random
from discord.ext import commands
from utilities.constants import consts 
class Tag(commands.Cog):
    '''
    purpose | this cog for when bot gets tagged.
    '''
    def __init__(self, bot):
        self.bot = bot
        self.user = self.bot.user
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        
        if (self.bot.user.mentioned_in(msg) and msg.author.bot is False):
            ctx = await self.bot.get_context(msg)
            
            if (ctx.command is None):
                print("is not command")
                ctx = await self.bot.get_context(msg)
                async with msg.channel.typing():
                    await ctx.invoke(self.bot.get_command('help'))
                

                
                
            
     

    
 
def setup(bot):
    bot.add_cog(Tag(bot))