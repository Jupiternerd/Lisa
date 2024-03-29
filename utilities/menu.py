'''
author : Shokk | A_Deidara, same person.

this is a port of a js menu application, love you @jowsey
Not a one to one port.


'''
import asyncio
from asyncio.tasks import wait_for
import discord
from discord.embeds import Embed
from events import Events
from utilities.constants import consts as constants
class Pages(object):
    '''
    purpose | serve as page containers
    '''
    def __init__(self, singles, index):
        
        #emoji_numbers = constants["emoji_numbers"] 

        self.index = singles.get("index") or index
        reactions = singles.get("reactions")
        #print(reactions)
        if type(reactions) is int:
            self.reactions = constants["reaction_dict"][reactions]
        else: 
            self.reactions = reactions
        print(self.reactions)
        #print(self.reactions)
        
        self.embed = singles.get("embed") or None

        if self.embed != None and not isinstance(self.embed, Embed):
            footer = self.embed.get("footer")
            if footer:
                self.embed["footer"] = footer
            self.color = singles.get("color") or None
                


        self.msg = singles.get("msg") or None
        self.wait = singles.get("wait") or None




class Menu(object):
    '''
    purpose | this cog contains menu playing parts.

    params
    
    :main : structure: [{index: 0, "embed":{title, body, color, footer} - or - embed, reactions: {"reaction":code_word}, wait: 0}]
    
    :bot : client
    
    :channel : channel to send msg in

    :user : user you only want to react to.
    '''

    def __init__(self, main, bot, channel, user, check=None):
        print(channel)
        self.events = Events()
        self.bot = bot
        self.pageCount = 0
        self.index = 0
        self.pages = []
        self.channel = channel
        self.user = user
        self.check = check
        self.ReactIsActive = True
        
        for singles in main:
            self.pageCount += 1
            newSingles = Pages(singles, self.pageCount)
            self.pages.append(newSingles)
        #print(self.pages[0].bg["link"])
    
    def __del__(self):
        print("deleted")
    
    async def add_reaction(self):
        if self.page.wait is not None: 
            print(self.page.wait)
            await asyncio.sleep(int(self.page.wait))
        
        print("going")
        if self.message:
            for emoji in self.page.reactions.keys():
                await self.message.add_reaction(emoji)
        
    def reaction_check(self, reaction, user):
        return reaction.emoji in self.page.reactions.keys() and user.id == self.user.id
        
    async def wait_for_reaction(self):

        while self.ReactIsActive:
            try:
                reaction, user = await self.bot.wait_for('reaction_add', check= self.reaction_check if self.check is None else self.check, timeout= constants["timeout"])
                #reaction, user = await self.bot.wait_for('reaction_remove', check= self.check, timeout= constants["timeout"])
            except asyncio.TimeoutError:
                try:
                    await self.stop()
                except:
                    print("Could not stop the menu.")
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

    async def custom(self):
        self.events.custom([self.index, self.page])

    async def forward(self):
        if self.index >= 0:
           await self.set_page(self.index + 1)


    async def backward(self):
        if self.index != 0:
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
        self.events.set([index, self.page])

        if self.page.embed:
            
            curEmbed = self.page.embed
            if isinstance(self.page.embed, Embed):
                embed = self.page.embed
            else:
                color = discord.Color(int(curEmbed["color"], 16))
                embed = Embed(type = "rich", title= curEmbed["title"], description= curEmbed["body"], color=color)
                embed.set_footer(text= curEmbed.get("footer"))
            
            await self.message.edit(content = "", embed= embed, suppress= False)
        else:
            content = self.page.msg
            await self.message.edit(content= content, suppress= True)

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
        print("starting")
        self.page = self.pages[self.index]
        if self.page.embed is not None:
            
            curEmbed = self.page.embed
            if isinstance(self.page.embed, Embed):
                embed = self.page.embed
            else:
                color = discord.Color(int(curEmbed["color"], 16))
                embed = Embed(type = "rich", title= curEmbed["title"], description= curEmbed["body"], color=color)
                embed.set_footer(text= curEmbed.get("footer"))
            
            self.message = await self.channel.send(embed= embed)
        else:
            content = self.page.msg
            self.message = await self.channel.send(content= content)
        await self.add_reaction()
        await self.wait_for_reaction()