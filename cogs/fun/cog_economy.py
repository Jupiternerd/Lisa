'''
Author | Shokkunn
'''
import discord, typing

from discord.ext.commands import bot
from discord.ext import commands, tasks

class Economy(commands.Cog):
    '''
    purpose | this cog conatains before invocation tasks.
    '''
    def __init__(self, bot):
        self.bot = bot
        self.Orio = self.bot.OrioDb
        self.Db = self.bot.DiscordDb
    
    @commands.command(name= "Fish", aliases=["cast"])
    async def fish(self, ctx):
        self.Orio["fishes"].find_one()

    @commands.command(name= "balance", aliases=["bal", "purse"])
    async def balance(self, ctx, member: discord.Member=None):
        if not member:
            member = ctx.author
        
        user = self.Db["users"].find_one({"_id": member.id})
        await ctx.send(user["prefix"])

        print(member.id)
        


def setup(bot):
    bot.add_cog(Economy(bot))