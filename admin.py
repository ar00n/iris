import discord
from discord.ext import commands

class Admin():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member):
        """Kicks defined member.
            A command that will kick inputted member.
            """
        await self.bot.kick(user)

    @commands.command(pass_context=True)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member):
        """Blasts defined member into oblivion.
            Beam Me Up, Scotty.
            """
        await self.bot.ban(user)

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        """*purge <amount>
            A command that will purge a specified amount of messages from a text channel.
            """
        deleted = await self.bot.purge_from(ctx.message.channel, limit=amount)
        await self.bot.say('Deleted {} message(s)'.format(len(deleted)))

def setup(bot):
    bot.add_cog(Admin(bot))