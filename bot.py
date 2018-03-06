import discord
from discord.ext import commands
from discord.ext.commands import Bot
import json
import asyncio

bot = commands.Bot(command_prefix=['.', '<@396322727079968778> '])

startup_extensions = ["admin", "utility", "fun", "games", "me"]
data = json.load(open('config.json'))
key = data["key"]

@bot.event
async def on_ready():
    print (bot.user.name + ' is ready')
    await bot.change_presence(game=discord.Game(name='.help | .invite'))

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def playing(ctx, *, message):
    """Only @ar0n#1462 can run.
    A command that will change the "playing" state of iris.
    """
    if ctx.message.author.id == '231715673435275274':
        await bot.change_presence(game=discord.Game(name=message))
        #await bot.say('I am now playing `' + message + '` :smiley:')

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run(key)