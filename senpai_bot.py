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
from random import choice
from discord.voice_client import VoiceClient
import youtube_dl



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
    await ctx.send('Made by `Abhishek Kushwaha`')
    await ctx.send('Thanks to `Abhishek` for coming up with the idea')

@client.command(name='creditz', help='This command returns the TRUE credits')
async def creditz(ctx):
    await ctx.send('**No one but me, lozer!**')




    
switchpresence.start()    
client.run('token')
#starting the loop for the switch_presence
#rumming the client in the server


