'''
Author | Shokkunn
'''
import discord
import asyncio
from discord.errors import InvalidArgument

from discord.ext.commands import bot
from discord.ext import commands, tasks
from discord.ext.commands.errors import BadArgument, UserInputError

class Core(commands.Cog):

    '''
    purpose | Help command.
    '''
    def __init__(self, bot):
        self.bot = bot

    
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.command(name= "help", help= "help *command")
    async def help(self, ctx, command = None):
        toSend = ""
        #if there is a sub command
        if (command):
            print("a")
            cmdFind = discord.utils.find(lambda cmd: cmd.name == command, self.bot.commands)
            if (cmdFind == None): raise BadArgument
            print (dir(cmdFind))
            toSend = cmdFind.help


            
            
            pass
            
        else:

            helpList = f"[ Your prefix : **{ctx.prefix}** ] Bot Commands :\n";
            for cmds in self.bot.commands:
                #print (dir(cmds));
                helpList += cmds.name + f" [ Help ] {cmds.help}\n " ;
            
            toSend = helpList
            
        await ctx.reply(toSend, mention_author=False);
    #prefix
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.command(name= "prefix", help= "prefix *prefix*")
    async def prefix(self, ctx, prefix= None):
        if prefix is not None:
            if (len(prefix) > 3):
                raise BadArgument;
        

        
        toSend = "Successfully **changed** to : ";
        
        toSend += f"* {prefix} *" if prefix is not None else f" default "
        
        UserDb = self.bot.DiscordDb["users"]
        filter = {"_id": ctx.author.id}
        
        newValues = { "$set": { 'prefix': prefix } }

        UserDb.update_one(filter, newValues)

        await ctx.reply(toSend, mention_author=False);



        


def setup(bot):
    bot.add_cog(Core(bot))