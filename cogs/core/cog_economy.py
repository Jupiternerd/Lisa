'''
Author | Shokkunn
'''
import discord, typing

from discord.ext.commands import bot
from discord.ext import commands, tasks

class Economy(commands.Cog, name="Economy"):
    '''
    purpose | this cog conatains before invocation tasks.
    '''
    def __init__(self, bot):
        self.bot = bot
        self.Db = self.bot.DiscordDb
    
    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name= "fish", aliases=["cast"])
    async def fish(self, ctx):
        fish = self.Db["items"].find_one({"type": "fish"})
        print(fish)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(name= "balance", aliases=["bal", "purse"])
    async def balance(self, ctx, member: discord.Member=None):
        if not member:
            member = ctx.author
        
        user = self.Db["users"].find_one({"_id": member.id})
        cur = user.get("universe").get("currency")
        nCur = cur[0]
        pCur = cur[1]
        await ctx.reply(f"Balance = {nCur}\nPremium = {pCur}", mention_author=False)
        


def setup(bot):
    bot.add_cog(Economy(bot))