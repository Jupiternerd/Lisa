'''
Author | Shokkunn
'''
from utilities.menu import Menu
import discord
import asyncio
import json
from discord.errors import InvalidArgument
from events import Events
from discord.ext.commands import bot
from discord.ext import commands, tasks
from discord.ext.commands.core import check, is_owner
from discord.ext.commands.errors import BadArgument, UserInputError

class Core(commands.Cog, name="Core"):

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
            prefix = await self.bot.get_prefix(ctx.message)

            helpList = f"[Bot Commands]\n";
            #print(self.bot.cogs)
            for cogs in self.bot.cogs:
                #print(type(cogs))
                cog = self.bot.cogs.get(cogs)
                commands = cog.get_commands()
                #print(cog.__cog_name__)
                
                if len(commands) > 0:
                  helpList += "----" + cog.__cog_name__ + "----\n"
                  for cmd in commands:
                      
                      try:
                          helpList += prefix + cmd.name + "\n"  if await cmd.can_run(ctx) else "" ; #the can_run(ctx) part, remove it entirely
                    
                      except:
                          print("can not run this command " + cmd.name)


            
            toSend = helpList
            
        await ctx.reply(toSend, mention_author=False);
    #prefix
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.command(name= "prefix", help= "prefix *prefix*")
    async def prefix(self, ctx, prefix= None):
        if prefix is not None:
            if (len(prefix) > 3):
                raise BadArgument;
        

        
        toSend = "Successfully **changed** to : " + prefix if prefix is not None else " default ";
        UserDb = self.bot.DiscordDb["users"]
        filter = {"_id": ctx.author.id}
        
        newValues = { "$set": { 'prefix': prefix } }

        UserDb.update_one(filter, newValues)

        await ctx.reply(toSend, mention_author=False);


    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.command(name= "men", help= "menu")
    async def menu(self, ctx):
        with open("././assets/menu.json", encoding='utf-8') as jsonFile:
            jsonObject = json.load(jsonFile)
            jsonFile.close()
            
        
        x = Menu(jsonObject, self.bot, ctx.channel, ctx.message.author)

        def te(list):
            print("aaaaaaaaaa")
            print(list)
        
        x.events.set += te
        
        await x.start()
        #del x  



        


def setup(bot):
    bot.add_cog(Core(bot))