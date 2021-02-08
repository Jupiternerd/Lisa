'''
Author | Shokkunn
'''
import discord, typing

from discord.ext.commands import bot
from discord.ext import commands, tasks

class Moderation(commands.Cog):
    '''
    purpose | this cog conatains before invocation tasks.

    @todo | implement the permission check only for this cog
    '''
    def __init__(self, bot):
        self.bot = bot
        self.Orio = self.bot.OrioDb
        self.Db = self.bot.DiscordDb
    
    @commands.command(name= "kick")
    async def fish(self, ctx, member: discord.Member , reason: str):
        guild = ctx.guild
        ctx.reply("Kicked for", reason)
        guild.kick(member, reason=reason);
        


def setup(bot):
    bot.add_cog(Moderation(bot))