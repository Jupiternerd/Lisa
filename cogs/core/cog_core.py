'''
Author | Shokkunn
'''
from discord.components import SelectOption
from utilities.menu import Menu
import discord, io
import asyncio
import json
from PIL import Image
from discord.errors import InvalidArgument
from events import Events
from discord.ext.commands import bot
from discord.ext import commands, tasks
from discord.ext.commands.core import check, is_owner
from discord.ext.commands.errors import BadArgument, UserInputError

class Confirm(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
    @discord.ui.select(options= [discord.SelectOption(label="1", default= True), discord.SelectOption(label="2", description="numba2", default= False), discord.SelectOption(label="3", default= False)])
    async def No(self, select: discord.ui.Select, interaction: discord.Interaction):
        await interaction.response()
        print(select.values)
    # When the confirm button is pressed, set the inner value to `True` and
    # stop the View from listening to more input.
    # We also send the user an ephemeral message that we're confirming their choice.
    @discord.ui.button(style=discord.ButtonStyle.danger, emoji="<:shinut:866117972291354634>")
    async def confirm(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message('Confirming', ephemeral=True)
        self.value = True
        
        self.stop()

    # This one is similar to the confirmation button except sets the inner value to `False`
    @discord.ui.button(label='Cancel', style=discord.ButtonStyle.grey)
    async def cancel(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message('Cancelling', ephemeral=True)
        self.value = False
        self.stop()





class Core(commands.Cog, name="Core"):

    '''
    purpose | Help command.
    '''
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ask(self, ctx: commands.Context):
       """Asks the user a question to confirm something."""
       # We create the view and assign it to a variable so we can wait for it later.
       view = Confirm()
       message = await ctx.send('Do you want to continue?', view=view)
       # Wait for the View to stop listening for input...
       await view.wait()
       if view.value is None:
           print('Timed out...')
       elif view.value:
           print('Confirmed...')
       else:
           await message.delete()
           print('Cancelled...')


    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.command(name= "settings", help= "change your stuff")
    async def settings(self, ctx):
        pass
    
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.command(name= "help", help= "help *command", aliases=["hell"])
    async def help(self, ctx, command = None):
        toSend = ""
        #if there is a sub command
        #bot.get_command(, "sum")

        if (command in self.bot.commands):
            print(dir(ctx.command.aliases))
            cmdFind = discord.utils.find(lambda cmd: cmd.aliases == command, self.bot.commands)
            if (cmdFind == None): raise BadArgument
            #print (dir(cmdFind))
            toSend = cmdFind.help
            print(toSend)


            
            
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


    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.command(name= "info", help= "info")
    async def info(self, ctx):
        toSend = ""
        width = 450
        height = 235
        color_1 = (255, 255, 255)
        

                    
        img = Image.new('RGB', (width, height), color_1)
        #img.show()

        with io.BytesIO() as image_binary:
                img.save(image_binary, 'PNG')
                image_binary.seek(0)
                await ctx.reply(file=discord.File(fp=image_binary, filename="why.png"), mention_author= False)
        


def setup(bot):
    bot.add_cog(Core(bot))