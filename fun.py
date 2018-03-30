import discord
from discord.ext import commands
from secrets import choice
import aiohttp
import json
import asyncio
import urllib

data = json.load(open('config.json'))
giphy = data["giphy"]

class Fun():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def leet(self, ctx, *, message):
        """<plainText> Translates given text to "leet".
            A command that will convert given text to leet format.
            """
        def leet(text):
            getchar = lambda c: chars[c] if c in chars else c
            chars = {"a":"4","e":"3","l":"1","o":"0","s":"5"}
            return ''.join(getchar(c) for c in text)

        await self.bot.say(leet(message))

    @commands.command(pass_context=True)
    async def oof(self, ctx):
        """oof! 
            A command that will return oof.
            """
        choices = ('**oof**', '***oof***', '__**oof**__', '__***oof***__', '~~oof~~')
        await self.bot.say(choice(choices))

    @commands.command(pass_context=True)
    async def hello(self, ctx):
        """Hello! 
            A command that will return with a warm message.
            """
        choices = ('Hey!', 'Hello!', 'Hi!', 'Hallo!', 'Bonjour!', 'Hola!')
        await self.bot.say(choice(choices))

    @commands.command(pass_context=True)
    async def quote(self, ctx):
        """Will tell you a quote.
            A command that will return a powerful quote.
            """
        choices = ('If you tell a big enough lie and tell it frequently enough, it will be believed.', 'Make the lie big, make it simple, keep saying it, and eventually they will believe it.', 'He alone, who owns the youth, gains the future.', 'Those who want to live, let them fight, and those who do not want to fight in this world of eternal struggle do not deserve to live.', 'Demoralize the enemy from within by surprise, terror, sabotage, assassination. This is the war of the future.', 'The great masses of the people will more easily fall victims to a big lie than to a small one.', 'As a Christian I have no duty to allow myself to be cheated, but I have the duty to be a fighter for truth and justice.', 'ur mom gay')
        await self.bot.say(choice(choices))

    @commands.command(pass_context=True)
    async def echo(self, ctx, *, message):
        """Will echo the message.
            A command that will echo the message.
            """
        if "@everyone" not in message:
            await self.bot.say(message + ' -{}'.format(ctx.message.author.mention))
        else:
            await self.bot.say('My names {} and I want attention.'.format(ctx.message.author.mention))

    @commands.command(pass_context=True)
    async def gif(self, ctx, *, query):
            """*search <query>
            A command that will return a random .gif that matches the search query.
            """

            params = {
                'api_key': giphy,
                'q': query,
                'limit': '100',
                'offset': '0',
                'rating': 'R',
                'lang': 'en'
            }

            async with aiohttp.ClientSession() as session:
                async with session.get('https://api.giphy.com/v1/gifs/search', params=params) as response:
                    data = await response.json()
                    values = [v for results in data['data']
                              for k, v in results.items() if k == 'url']

                    url = choice(values)
            await self.bot.say(url)

    @commands.command(pass_context=True)
    async def joke(self, ctx):
        """Tells you a joke.
            A command that will return a random joke provided by icanhazdadjoke.com.
            """
        h = { 'User-Agent' : 'curl/7.9.8', 'Accept' : 'text/plain' }
        q = urllib.request.Request('https://icanhazdadjoke.com/', None, h)
        r = urllib.request.urlopen(q)
        p = r.read()
        a = p.decode("utf8")
        await self.bot.say(a)

def setup(bot):
    bot.add_cog(Fun(bot))
