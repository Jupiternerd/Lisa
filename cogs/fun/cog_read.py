'''
Author | Shokkunn
'''
from utilities.novel import Novel
from utilities.makeGif import Gif
from discord.ext import commands, tasks


class Read(commands.Cog):
    '''
    purpose | this cog conatains before invocation tasks.
    '''
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=["novel"])
    async def read(self, ctx):
        novelJSON = self.bot.OrioDb["stories"].find_one({"_id": 2})
        x = Novel(novelJSON, self.bot, ctx.channel, ctx.message.author)
        await x.start() 
        #print(novelJSON + "NOVEL")   
    @commands.command(aliases=["gif"])
    async def g(self, ctx):
        x = Gif(ctx.channel)
        await x.start() 
        print("aaa", ctx.author.id)
        del x           
        

def setup(bot):
    bot.add_cog(Read(bot))