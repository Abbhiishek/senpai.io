import discord
from datetime import datetime
from discord import Member, Embed
from discord.colour import Color
from discord.ext import commands,tasks
from random import choice
import os
from discord.user import User
from discord_components import DiscordComponents
from discord.enums import UserFlags
from discord.flags import Intents
import random
from discord.user import commandsUser
import requests
import asyncio
from typing import optional

class Generalcomm(commands.Cog):
    def __init__(self, commands):
        self.commands = commands

    #EVENTS
    @commands.Cog.listener()
    async def on_ready(self):
        async with self.channel.typing():
            print("general commands  cogs loaded ........")

    @commands.command()
    async def info(self, ctx, target:optional[Member]):
        target = target or ctx.author
        async with ctx.channel.typing():

            embed = discord.Embed(title="INFORMATION OF THE USER!",
                                  description=target.mention,
                                  timestamp=datetime.utcnow(),
                                  color=discord.Colour.red())
            embed.add_field(name="USER ID", value=target.id, inline=False)
            embed.add_field(name="Bot?", value=target.bot, inline=False)
            embed.add_field(name="Top Role", value=target.top_role.mention, inline=False)
            embed.add_field(name="Created at", value=target.created_at.strftime("%d/%m/%Y"), inline=False)
            embed.add_field(name="Joined at", value=target.joined_at.strftime("%d/%m/%Y"), inline=False)
            embed.add_field(name="Boosted", value=bool(target.premium.since), inline=False)

            embed.set_thumbnail(url=target.avatar_url)
            embed.set_footer(icon_url=ctx.author.avatar_url,
                             text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)

    @commands.command()
    async def status(ctx):
            
            async with ctx.channel.typing():
                embed = discord.Embed(title="senpai.io", description="These are the config of senpai.io")
                embed.add_field(name="version" , value=" 1.01.02", inline=True)
                embed.add_field(name="created by", value='<@752362202945683480>')
                embed.add_field(name="Total servers", value=f"{len(commands.guilds)} Servers!",inline=True)
                embed.add_field(name="Total User ", value= f"{len(commands.users)} Users!",inline=True)
                embed.set_thumbnail(url=discord.guild.avatar_url)

                await ctx.send(embed=embed)
    @commands.command()
    async def serverstats(ctx):
            embed=discord.Embed(title=f"server's name  \n {ctx.guild.name}")
            embed.add_field(name="Users:", value=ctx.guild.member_count, inline=False)
            embed.add_field(name="Channels:", value=len(ctx.guild.channels), inline=False)
            embed.set_thumbnail(url=ctx.guild.icon_url)
            await ctx.send(embed=embed)
    @commands.command(name='hello',help='This command returns a random welcome message')
    async def hello(self, ctx ):
        responses = [
            '***grumble*** Why did you wake me up? \n'
            'Top of the morning to you lad!', 'Hello, how are you?', 'Hi',
            '**Wasssuup!**'
        ]
        await ctx.send(choice(responses))

    
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

    @commands.command(name='credits', help='This command returns the credits')
    async def credits(self, ctx):
        await ctx.send('Made by <@752362202945683480>')
        await ctx.send(
            'Thanks to <@752362202945683480> for coming up with the idea')

    @commands.command(name='creditz',
                      help='This command returns the TRUE credits')
    async def creditz(self ,ctx):
        await ctx.send('**No one but me, lozer!**')

    @commands.command(name='die',help='This command returns a random last words')
    async def die(self ,ctx):
        responses = [
            'why have you brought my short life to an end',
            'i could have done so much more',
            'i have a family, kill them instead'
        ]
        await ctx.send(choice(responses))



    @commands.command()
    async def source(self, ctx):
        emb = discord.Embed(title="Source code!!", description="I[Click here](https://github.com/Abbhiishek/senpai.io)", color=0x2e69f2)
        senpai = self.client.get_user(self.senpai_id)
        emb.set_footer(
            text=f"SENPAI.IO",
            icon_url=senpai.avatar_url,
        )
        await ctx.send(embed=emb)

    @commands.command()
    async def invite(self, ctx):
        emb = discord.Embed(title="INVITE SENPAI.IO!!", description="Invite SENPAI  in your server uwu\n[Click here](https://discord.com/api/oauth2/authorize?client_id=888414036662833164&permissions=3394560&scope=bot)", color=0x2e69f2)
        senpai = self.client.get_user(self.senpai_id)
        emb.set_footer(
            text=f"SENPAI.IO",
            icon_url=senpai.avatar_url,
        )
        await ctx.send(embed=emb)

    @commands.command()
    async def prefix(self, ctx):
        await ctx.send("Prefixes for senpai are `s.`, `senpai ` and `S. `.")
        
def setup(commands):
    commands.add_cog(Generalcomm(commands))
    print(">>> gerneral commands load ho gaya !!!!!!!!!")
