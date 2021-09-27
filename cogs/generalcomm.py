from operator import add
from os import name
import discord
from discord import embeds
from discord.audit_logs import _transform_verification_level
from discord.colour import Color
from discord.ext import commands
from discord.ext.commands.core import Command, command
import random
from random import choice
from discord.user import User
from discord.user import ClientUser
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


intents = discord.Intents.default()
intents.members = True

class Generalcomm(commands.Cog):
    def __init__(self, commands):
        self.commands = commands

    #EVENTS
    @commands.Cog.listener()
    async def on_ready(self):
        async with self.channel.typing():
            print("general commands  cogs loaded ........")

    @commands.command()
    async def info(self, ctx, member: discord.Member):
        async with ctx.channel.typing():

            embed = discord.Embed(title=member.name,
                                  description=member.mention,
                                  color=discord.Colour.red())
            embed.add_field(name="USER ID", value=member.id, inline=False)
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(icon_url=ctx.author.avatar_url,
                             text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)

    @commands.command()
    async def server(self, ctx ):
        async with ctx.channel.typing():
            embed = discord.Embed(title="senpai.io", description="these are the config of senpai.io")
            embed.add_field(name="version" , value=" 1.01.02", inline=True)
            embed.add_field(name="created by", value='<@752362202945683480>')
            embed.add_field(name="Total servers", value=f"{len(commands.guilds)} Servers!",inline=True)
            embed.add_field(name="Total User ", value= f"{len(commands.users)} Users!",inline=True)


            await ctx.send(embed=embed)

    @commands.command(name='greet',help='This command greet prople whom you had mention')
    async def greet(self, ctx, member: discord.Member):
        async with ctx.channel.typing():
            greeting = [
                "welcome to the server , Hope you have a great time here !",
                "What’s up?", "How are things?", " Good to see you",
                " Pleased to meet you", "How have you been?", "Yo!", " Hiya!"
            ]
            embed = discord.Embed(
                title=f"{ctx.author.name} Greeted" , description=member.mention, color=discord.Colour.red())
            embed.add_field(name="-", value=random.choice(greeting))

            embed.set_thumbnail(url=member.avatar_url)
        
            embed.set_footer(icon_url=ctx.author.avatar_url,
                             text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)

    @commands.command(name='hello',help='This command returns a random welcome message')
    async def hello(self, ctx ):
        responses = [
            '***grumble*** Why did you wake me up?',
            'Top of the morning to you lad!', 'Hello, how are you?', 'Hi',
            '**Wasssuup!**'
        ]
        await ctx.send(choice(responses))

    @commands.command(name='die',
                      help='This command returns a random last words')
    async def die(self ,ctx):
        responses = [
            'why have you brought my short life to an end',
            'i could have done so much more',
            'i have a family, kill them instead'
        ]
        await ctx.send(choice(responses))

    @commands.command(name='credits', help='This command returns the credits')
    async def credits(self, ctx):
        await ctx.send('Made by <@752362202945683480>')
        await ctx.send(
            'Thanks to <@752362202945683480> for coming up with the idea')

    @commands.command(name='creditz',
                      help='This command returns the TRUE credits')
    async def creditz(self ,ctx):
        await ctx.send('**No one but me, lozer!**')


def setup(commands):
    commands.add_cog(Generalcomm(commands))
    print(">>> gerneral commands load ho gaya !!!!!!!!!")
