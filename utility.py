import discord
from discord.ext import commands
import hashlib
from translate import Translator
import datetime
from random import choice
import urllib
import json

class Utility():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def ping(self, ctx):
        """pong!
            A command that will return a pong.
            """
        await self.bot.say('Pong! :ping_pong:')

    @commands.command(pass_context=True)
    async def translate(self, ctx, fromLang, toLang, *, message):
        """<from> <to> <text> Will translate given text.
            A command that will translate given text from and to specified languages.
            """
        translator = Translator(to_lang=toLang, from_lang=fromLang)
        translation = translator.translate(message)
        await self.bot.say(translation)

    @commands.command(pass_context=True)
    async def info(self, ctx, user: discord.Member = None):
        """*search <user>
            A command that will return information about the requested user or you!
            """
        if user == None:
            user = ctx.message.author
        await self.bot.say('```Status: {}'.format(user.status) + '\nRole: {}'.format(user.top_role) + '\nJoined: {}'.format(user.joined_at) + '\nPlaying: {}'.format(user.game) + '```')

    @commands.command(pass_context=True)
    async def avatar(self, ctx, user: discord.Member):
        """*search <user>
            A command that will return the avatar url of a user.
            """
        await self.bot.say('{}'.format(user.avatar_url))

    @commands.command(pass_context=True)
    async def hash(self, ctx, hash, *, message):
        """<algorithm> <plainText> Converts given text to requested hash.
            A command that will convert given text to: sha1, sha224, sha256, sha384, sha512, blake2b, blake2s and md5()
            """
        if hash == "md5":
            m = hashlib.md5()
            m.update(str.encode(message))
        elif hash == "sha1":
            m = hashlib.sha1()
            m.update(str.encode(message))
        elif hash == "sha256":
            m = hashlib.sha256()
            m.update(str.encode(message))
        elif hash == "sha384":
            m = hashlib.sha384()
            m.update(str.encode(message))
        elif hash == "sha512":
            m = hashlib.sha512()
            m.update(str.encode(message))
        elif hash == "blake2b":
            m = hashlib.blake2b()
            m.update(str.encode(message))
        elif hash == "blake2s":
            m = hashlib.blake2s()
            m.update(str.encode(message))

        await self.bot.say('{}'.format(m.hexdigest()))

    @commands.command(pass_context=True)
    async def time(self, ctx):
        """What's the time?
            A command that will return the time.
            """
        choices = (str(datetime.datetime.now().time())[:-7], 'Hammer Time :hammer:', 'ITS TIME TO STOP')
        await self.bot.say(choice(choices))

    @commands.command(pass_context=True)
    async def members(self, ctx):
        """How many members?
            A command that will return the number of users in a discord server.
            """

        await self.bot.say('There are {} members in this server.'.format(ctx.message.server.member_count))

    @commands.command(pass_context=True)
    async def randint(self, ctx):
        """Generate a random integer. 
            A command that will return a random number between 1000000 and 9999999.
            """
        await self.bot.say(random.randint(1000000, 9999999))

    @commands.command(pass_context=True)
    async def value(self, ctx, crypto, currency = None):
        """<crypto> <currency> Information on specified crypto.
            A command that will return market information provided by CoinMarketGap.
            """
        if currency == None:
            url = 'https://api.coinmarketcap.com/v1/ticker/{}/'.format(crypto)
        else:
            url = 'https://api.coinmarketcap.com/v1/ticker/{}/?convert={}'.format(crypto, currency)
        req = urllib.request.Request(url)

        r = urllib.request.urlopen(req).read()
        cont = json.loads(r.decode('utf-8'))
        counter = 0
        if currency == None:
            price = '\nPrice ($): {} ({}%)'.format(cont[0]['price_usd'], cont[0]['percent_change_24h'])
        else:
            price = '\nPrice ({}): {} ({}%)'.format(currency.upper(), cont[0]['price_' + currency], cont[0]['percent_change_24h'])
        await self.bot.say('```Name: {} ({})'.format(cont[0]['name'], cont[0]['symbol']) + price + '\nPrice (BTC): {}'.format(cont[0]['price_btc']) + '\n24 Hr Volume ($): {}```'.format(cont[0]['24h_volume_usd']))


def setup(bot):
    bot.add_cog(Utility(bot))