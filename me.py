import discord
from discord.ext import commands

class Me():
    def __init__(self, bot):
        self.bot = bot  

    @commands.command(pass_context=True)
    async def servers(self, ctx):
        """Who am I connected to?
            A command that will return a list of servers that I'm connected to.
            """
        #servers = list(self.bot.servers)
        await self.bot.say('I am currently running on ' + str(len(self.bot.servers)) + ' servers.')

    @commands.command(pass_context=True)
    async def contact(self, ctx):
        """How many users can I see?
            A command that will return the number of users that this bot can see.
            """
    
        await self.bot.say('I can see {} Discord users.'.format(sum(1 for _ in bot.get_all_members())))

    @commands.command(pass_context=True)
    async def owner(self, ctx):
        """Shows the creator of me!
            A command that will return the owner of this bot.
            """
        await self.bot.say('This bot is owned by `ar0n#1462`.')

    @commands.command(pass_context=True)
    async def gay(self, ctx):
        """Gays on Sunshine invite link.
            A command that will return an invite to the most awesome Discord ever.
            """
        await self.bot.say('https://discord.gg/hwR5neh')

    @commands.command(pass_context=True)
    async def invite(self, ctx):
        """Invite me to your server!
            A command that will return a link that you can use to invite this bot!
            """
        await self.bot.say('You can invite me to your server with: https://discordapp.com/api/oauth2/authorize?client_id=396322727079968778&permissions=70778055&scope=bot.')

    @commands.command(pass_context=True)
    async def support(self, ctx):
        """iris Official Discord
            A command that will return the invite link for the iris discord.
            """
        await self.bot.say('Official iris Discord: https://discord.gg/JrYWrnv')

    @commands.command(pass_context=True)
    async def upvote(self, ctx):
        """Please upvote this bot on discordbots.org <3
            A command that will return the link to iris on discordbots.org.
            """
        await self.bot.say('UPVOTE!!! :thumbsup: https://discordbots.org/bot/396322727079968778')

def setup(bot):
    bot.add_cog(Me(bot))