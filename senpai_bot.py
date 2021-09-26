#importing databases we need for the projects
import discord
from discord.errors import ClientException
from discord.ext import commands
from discord.ext import tasks
import os
from discord.enums import UserFlags
from discord.flags import Intents
import random
import json
from discord.user import ClientUser
import requests
import asyncio



#adding our client (our bot , i am using client as bot)
#setting up Intents

intents = discord.Intents.default()
intents.members = True

#senpai variables
senpai_id = 888414036662833164
client = commands.Bot(command_prefix=commands.when_mentioned_or(  'S.', 's.'), case_insensitive=True, intents=intents)
client.remove_command("help")

print(">>>> The Master Is Logging To The Server... \n >>>Please wait for the connections to stablish...////////")

#Loads all the cogs in the cogs folder 
def load_cogs():
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            client.load_extension(f"cogs.{file[:-3]}")

@client.command()
@commands.is_owner()
async def reload(ctx):
  for file in os.listdir("./cogs"):
    if file.endswith(".py") and not file.startswith("_"):
      client.reload_extension(f"cogs.{file[:-3]}")
  await ctx.send("```>> Senpai reloaded cogs```")

 #creating a task that change the activity status of the bot every 5 seconds so that it show different information evry 5 second. 

@tasks.loop(seconds=5)
async def switchpresence():
    await client.wait_until_ready()
    sm = [f"{len(client.guilds)} Servers!", f"{len(client.users)} Users!"]
    ast = random.choice(sm)
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=f"senpai & {ast}"))

# loading all the information on the terminal when the bot goes online 

@client.event
async def on_ready():
    load_cogs()
    print(f">> Logged in as : {client.user.name} \n>> ID : {client.user.id}")
    print(f">> Total  Active Servers : {len(client.guilds)}")
    print('>> Senpai is Onwork.')
    print(">> Data loaded.")
                 




#do stuffs

import discord
from discord.ext import commands, tasks
from discord.voice_client import VoiceClient
import youtube_dl

from random import choice

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


client = commands.Bot(command_prefix='?')

status = ['Jamming out to music!', 'Eating!', 'Sleeping!']

@client.event
async def on_ready():
    change_status.start()
    print('Bot is online!')

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='general')
    await channel.send(f'Welcome {member.mention}!  Ready to jam out? See `?help` command for details!')

@client.command(name='ping', help='This command returns the latency')
async def ping(ctx):
    await ctx.send(f'**Pong!** Latency: {round(client.latency * 1000)}ms')

@client.command(name='hello', help='This command returns a random welcome message')
async def hello(ctx):
    responses = ['***grumble*** Why did you wake me up?', 'Top of the morning to you lad!', 'Hello, how are you?', 'Hi', '**Wasssuup!**']
    await ctx.send(choice(responses))

@client.command(name='die', help='This command returns a random last words')
async def die(ctx):
    responses = ['why have you brought my short life to an end', 'i could have done so much more', 'i have a family, kill them instead']
    await ctx.send(choice(responses))

@client.command(name='credits', help='This command returns the credits')
async def credits(ctx):
    await ctx.send('Made by `RK Coding`')
    await ctx.send('Thanks to `DiamondSlasher` for coming up with the idea')
    await ctx.send('Thanks to `KingSticky` for helping with the `?die` and `?creditz` command')

@client.command(name='creditz', help='This command returns the TRUE credits')
async def creditz(ctx):
    await ctx.send('**No one but me, lozer!**')

@client.command(name='play', help='This command plays music')
async def play(ctx, url):
    if not ctx.message.author.voice:
        await ctx.send("You are not connected to a voice channel")
        return

    else:
        channel = ctx.message.author.voice.channel

    await channel.connect()

    server = ctx.message.guild
    voice_channel = server.voice_client

    async with ctx.typing():
        player = await YTDLSource.from_url(url, loop=client.loop)
        voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

    await ctx.send('**Now playing:** {}'.format(player.title))

@client.command(name='stop', help='This command stops the music and makes the bot leave the voice channel')
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()

@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))

client.run('token')








#starting the loop for the switch_presence


switchpresence.start()

#rumming the client in the server

client.run('ODg4NDE0MDM2NjYyODMzMTY0.YUSWDA.c_fqaRhhwVgsN79QYfqezlZGFAA')
