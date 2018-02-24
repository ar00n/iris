import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import datetime
from random import randint
import aiohttp
import json
import hashlib
import urllib.parse
import urllib.request
import urllib.response

bot = commands.Bot(command_prefix='.')

data = json.load(open('config.json'))
key = data["key"]
giphy = data["giphy"]

heads = 0
tails = 0

@bot.event
async def on_ready():
    print (bot.user.name + ' is ready')
    await bot.change_presence(game=discord.Game(name='.help'))

@bot.command(pass_context=True)
async def ping(ctx):
    """pong!
        A command that will return a pong.
        """
    await bot.say(':ping_pong: skrt')
    
@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    """*search <user>
        A command that will return information about the requested user.
        """
    await bot.say('```Status: {}'.format(user.status) + '\nRole: {}'.format(user.top_role) + '\nJoined: {}'.format(user.joined_at) + '\nPlaying: {}'.format(user.game) + '```')

@bot.command(pass_context=True)
async def md5(ctx, *, message):
    """*plain <plainText>
        A command that will convert given text to md5 format.
        """
    m = hashlib.md5()
    m.update(str.encode(message))
    await bot.say('{}'.format(m.hexdigest()))

@bot.command(pass_context=True)
async def sha256(ctx, *, message):
    """*plain <plainText>
        A command that will convert given text to sha256 format.
        """
    m = hashlib.sha256()
    m.update(str.encode(message))
    await bot.say('{}'.format(m.hexdigest()))

@bot.command(pass_context=True)
async def leet(ctx, *, message):
    """*plain <plainText>
        A command that will convert given text to leet format.
        """
    def leet(text):
        getchar = lambda c: chars[c] if c in chars else c
        chars = {"a":"4","e":"3","l":"1","o":"0","s":"5"}
        return ''.join(getchar(c) for c in text)

    await bot.say(leet(message))

@bot.command(pass_context=True)
async def avatar(ctx, user: discord.Member):
    """*search <user>
        A command that will return the url of a user.
        """
    await bot.say('{}'.format(user.avatar_url))

@bot.command(pass_context=True)
async def owner(ctx):
    """Shows the creator of me!
        A command that will return the owner of this bot.
        """
    await bot.say('This bot is owned by `ar0n#1462`.')

@bot.command(pass_context=True)
async def flip(ctx):
    """Heads or Tails.
        A command that will return "Heads" or "Tails".
        """
    rand = random.randint(0,1)
    if rand == 0:
        await bot.say('Heads! :moneybag:')
        global heads
        heads += 1
    else:
        await bot.say('Tails! :moneybag:')
        global tails
        tails += 1

@bot.command(pass_context=True)
async def flips(ctx):
    """flip statistics.
        A command that will return the statistics of the flip command.
        """
    await bot.say('```Heads: ' + str(heads) + '\n\nTails: ' + str(tails) + "```")

@bot.command(pass_context=True)
async def randint(ctx):
    """Generate a random integer. 
        A command that will return a random number between 1000000 and 9999999.
        """
    await bot.say(random.randint(1000000, 9999999))

@bot.command(pass_context=True)
async def echo(ctx, *, message):
    """Will echo the message.
        A command that will echo the message.
        """
    await bot.say(message + ' -{}'.format(ctx.message.author.mention))

@bot.command(pass_context=True)
async def hello(ctx):
    """Hello! 
        A command that will return with a warm message.
        """
    choices = ('Hey!', 'Hello!', 'Hi!', 'Hallo!', 'Bonjour!', 'Hola!', 'Fuck off! :middle_finger:')
    await bot.say(random.choice(choices))

@bot.command(pass_context=True)
async def time(ctx):
    """What's the time?
        A command that will return the time.
        """
    choices = (str(datetime.datetime.now().time()), 'Hammer Time :hammer:', 'ITS TIME TO STOP')
    await bot.say(random.choice(choices))

@bot.command(pass_context=True)
async def quote(ctx):
    """Will tell you a quote.
        A command that will return a powerful quote.
        """
    choices = ('If you tell a big enough lie and tell it frequently enough, it will be believed.', 'Make the lie big, make it simple, keep saying it, and eventually they will believe it.', 'He alone, who owns the youth, gains the future.', 'Those who want to live, let them fight, and those who do not want to fight in this world of eternal struggle do not deserve to live.', 'Demoralize the enemy from within by surprise, terror, sabotage, assassination. This is the war of the future.', 'The great masses of the people will more easily fall victims to a big lie than to a small one.', 'As a Christian I have no duty to allow myself to be cheated, but I have the duty to be a fighter for truth and justice.', 'ur mom gay')
    await bot.say(random.choice(choices))

@bot.command(pass_context=True)
async def members(ctx):
    """How many members?
        A command that will return the number of users in a discord server.
        """
    await bot.say('There are {} members in this server.'.format(sum(1 for _ in bot.get_all_members())))

@bot.command(pass_context=True)
async def gay(ctx):
    """Gays on Sunshine invite link.
        A command that will return an invite to the most awesome Discord ever.
        """
    await bot.say('https://discord.gg/hwR5neh')

@bot.command(pass_context=True)
async def invite(ctx):
    """Invite me to your server!
        A command that will return a link that you can use to invite this bot!
        """
    await bot.say('You can invite me to your server with: https://discordapp.com/api/oauth2/authorize?client_id=396322727079968778&permissions=3406913&scope=bot.')

@bot.command(pass_context=True)
async def gif(ctx, *, query):
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

                url = random.choice(values)
        await bot.say(url)

@bot.command(pass_context=True)
async def joke(ctx):
    """Tells you a joke.
        A command that will return a random joke.
        """
    h = { 'User-Agent' : 'curl/7.9.8', 'Accept' : 'text/plain' }
    q = urllib.request.Request('https://icanhazdadjoke.com/', None, h)
    r = urllib.request.urlopen(q)
    p = r.read()
    a = p.decode("utf8")
    await bot.say(a)

@bot.command(pass_context=True)
async def grlc(ctx):
    """Current market information on Garlicoin.
        A command that will return market information provided by CoinMarketGap.
        """
    url = 'https://api.coinmarketcap.com/v1/ticker/garlicoin/'
    req = urllib.request.Request(url)

    r = urllib.request.urlopen(req).read()
    cont = json.loads(r.decode('utf-8'))
    counter = 0

    await bot.say('```Name: {} ({})'.format(cont[0]['name'], cont[0]['symbol']) + '\nPrice ($): {} ({}%)'.format(cont[0]['price_usd'], cont[0]['percent_change_24h']) + '\nPrice (BTC): {}'.format(cont[0]['price_btc']) + '\n24 Hr Volume ($): {}```'.format(cont[0]['24h_volume_usd']))

@bot.command(pass_context=True)
async def btc(ctx):
    """Current market information on Bitcoin.
        A command that will return market information provided by CoinMarketGap.
        """
    url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
    req = urllib.request.Request(url)

    r = urllib.request.urlopen(req).read()
    cont = json.loads(r.decode('utf-8'))
    counter = 0

    await bot.say('```Name: {} ({})'.format(cont[0]['name'], cont[0]['symbol']) + '\nPrice ($): {} ({}%)'.format(cont[0]['price_usd'], cont[0]['percent_change_24h']) + '\n24 Hr Volume ($): {}```'.format(cont[0]['24h_volume_usd']))

@bot.command(pass_context=True)
async def support(ctx):
    """iris Official Discord
        A command that will return the invite link for the iris discord.
        """
    await bot.say('Official iris Discord: https://discord.gg/JrYWrnv')

@bot.command(pass_context=True)
async def upvote(ctx):
    """Please upvote this bot on discordbots.org <3
        A command that will return the link to iris on discordbots.org.
        """
    await bot.say('UPVOTE!!! :thumbsup: https://discordbots.org/bot/396322727079968778')

@bot.command(pass_context=True)
async def servers(ctx):
    """Who am I connected to?
        A command that will return a list of servers that I'm connected to.
        """
    servers = list(bot.servers)
    await bot.say('I am currently running on ' + str(len(bot.servers)) + ' servers.')

@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member):
    """Kicks defined member.
        A command that will kick inputted member.
        """
    await bot.kick(user)

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member):
    """Blasts defined member into oblivion.
        Beam Me Up, Scotty.
        """
    await bot.ban(user)
    
@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount: int):
    """*purge <amount>
    A command that will purge a specified amount of messages from a text channel.
    """

    deleted = await bot.purge_from(ctx.message.channel, limit=amount)
    await bot.say('Deleted {} message(s)'.format(len(deleted)))

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def playing(ctx, *, message):
    """Only @ar0n#1462 can run.
    A command that will change the "playing" state of iris.
    """
    if ctx.message.author.id == '231715673435275274':
        await bot.change_presence(game=discord.Game(name=message))
        #await bot.say('I am now playing `' + message + '` :smiley:')

bot.run(key)

