'''
author : Shokk

This is a port of a js menu application, original author @jowsey.
Not a one to one port, basic/same idea, different execution.


'''
import asyncio
from asyncio.tasks import wait_for
import discord
from utilities.constants import consts as constants
from events import Events
class Novel_Buttons(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    # When the confirm button is pressed, set the inner value to `True` and
    # stop the View from listening to more input.
    # We also send the user an ephemeral message that we're confirming their choice.
    @discord.ui.button(label='<', style=discord.ButtonStyle.green)
    async def confirm(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.value + 1 != 0:
            self.value - 1;
        #await interaction.response.send_message('Confirming', ephemeral=False)



    # This one is similar to the confirmation button except sets the inner value to `False`
    @discord.ui.button(label='>', style=discord.ButtonStyle.grey)
    async def cancel(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.value + 1;
        #await interaction.response.send_message('Cancelling', ephemeral=False)



class Pages(object):
    '''
    purpose | serve as page containers
    '''
    def __init__(self, singles, index):
        #emoji_numbers = constants["emoji_numbers"] 

        self.index = singles.get("index") or index
        reactions = singles.get("reactions")
        if type(reactions) is int:
            self.reactions = constants["reaction_dict"][reactions]
        else: 
            self.reactions = reactions
            
        self.bg = singles.get("bg") or None
        self.msg = singles.get("msg") or None
        self.color = singles.get("color") or None
        self.wait = singles.get("wait") or None


class Novel(object):
    '''
    purpose | this cog conatains novel playing parts.

    params
    
    :json : json of the novel you want to play
    
    :bot : client
    
    :channel : channel to send msg in

    :user : user you only want to react to

    '''

    def __init__(self, json, bot, channel, user):
        self.events = Events()
        self.bot = bot
        self.pageCount = 0
        self.index = 0
        self.pages = []
        self.channel = channel
        self.user = user
        self.ReactIsActive = True
        self.MessageIsActive = True
        
        for singles in json["multiples"]:
            self.pageCount += 1
            newSingles = Pages(singles, self.pageCount)
            newSingles.bg = bot.UniverseDb["backgrounds"].find_one({"name": newSingles.bg})
            self.pages.append(newSingles)
        #print(self.pages[0].bg["link"])
    
    def __del__(self):
        print("deleted")
    
    async def add_reaction(self):
        if self.page.wait is not None: await asyncio.sleep(self.page.wait)
        if self.message:
            for emoji in self.page.reactions.keys():
                await self.message.add_reaction(emoji)
        
    def reaction_check(self, reaction, user):
        return reaction.emoji in self.page.reactions.keys() and user.id == self.user.id
        
    async def wait_for_reaction(self):

        while self.ReactIsActive:
            try:
                reaction, user = await self.bot.wait_for('reaction_add', check= self.reaction_check, timeout= constants["timeout"])
                #reaction, user = await self.bot.wait_for('reaction_remove', check= self.check, timeout= constants["timeout"])
            except asyncio.TimeoutError:
                await self.clear_reactions()
                break
            else:
                await self.message.remove_reaction(reaction, user)
                cmd_line = self.page.reactions[reaction.emoji] #can be either 1, or "backward"
                cmd_type = type(cmd_line)
                self.emoji_bank = []
                for emoji in reaction.message.reactions: self.emoji_bank.append(emoji.emoji)

                if cmd_type is int:
                    await self.set_page(cmd_line)

                elif cmd_type is str:
                    method = getattr(self, cmd_line)
                    await method()


    async def forward(self):
        if self.index >= 0:
           await self.set_page(self.index + 1)


    async def backward(self):
        if self.index is not 0:
           await self.set_page(self.index - 1)

    async def clear_reactions(self, emoji=None):
        self.events.clear_reactions()
        if self.message is not None:
            if emoji is not None:
                await self.message.clear_reaction(emoji)
            else:
                await self.message.clear_reactions()


        else: raise Exception("No message!")



    async def set_page(self, index):
        self.index = index
        self.page = self.pages[self.index]

        self.events.set(index, self.page)
        
        content = str('>>> ' + self.page.msg)
        color = discord.Color(int(self.page.color, 16))
        embed = discord.Embed(author=self.user.name, color =color).set_image(url=self.page.bg["link"])
        await self.message.edit(content = content, embed = embed)

        if self.page.reactions is None: 
            await self.stop()
            return await self.clear_reactions()

        if list(self.emoji_bank) != list(self.page.reactions.keys()) or self.page.wait is not None:
            await self.clear_reactions()
            await self.add_reaction()
        
    async def stop(self):
        self.events.stop()
        await self.clear_reactions()
        self.ReactIsActive = False
        print("stop")
        


    async def start(self):
        self.events.start()
        self.page = self.pages[self.index]
        content = str('>>> ' + self.page.msg)
        color = discord.Color(int(self.page.color, 16))
        embed = discord.Embed(author=self.user.name, color=color).set_image(url=self.page.bg["link"])
        self.message = await self.channel.send(content = content, embed = embed)
        await self.add_reaction()
        await self.wait_for_reaction()

        
        

        
        

        

        


        




        
        
        
    

