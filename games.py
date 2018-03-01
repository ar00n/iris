import discord
from discord.ext import commands
from random import randint

heads = 0
tails = 0

class Games():
    def __init__(self, bot):
        self.bot = bot  

    @commands.command(pass_context=True)
    async def flip(self, ctx):
        """Heads or Tails.
            A command that will return "Heads" or "Tails".
            """
        rand = randint(0,1)
        if rand == 0:
            await self.bot.say('Heads! :moneybag:')
            global heads
            heads += 1
        else:
            await self.bot.say('Tails! :moneybag:')
            global tails
            tails += 1

    @commands.command(pass_context=True)
    async def dice(self, ctx, dice: int = 1):
        """Rolls a dice or a defined amount of dice.
            A command that will roll dice.
            """
        num = 6 * dice
        rand = 0
        if dice > 100:
            rand = 'a lot of dice'
        elif dice == None:
            rand = randint(1,6)
        else:
            rand = randint(1,num)

        await self.bot.say('You rolled {}! :game_die:'.format(rand))

    @commands.command(pass_context=True)
    async def flips(self, ctx):
        """flip statistics.
            A command that will return the statistics of the flip command.
            """
        await self.bot.say('```Heads: ' + str(heads) + '\n\nTails: ' + str(tails) + "```")

def setup(bot):
    bot.add_cog(Games(bot))