'''
Author | Shokkunn
'''


from discord.ext import commands


class OnMsg(commands.Cog):
    '''
    purpose | this cog conatains checks.
    '''
    def __init__(self, bot):
        self.bot = bot

    '''
    This applies to all commands.
    '''

    @commands.Cog.listener()
    async def message(self, message):


        await self.bot.process_commands(message)

        


def setup(bot):
    bot.add_cog(OnMsg(bot))