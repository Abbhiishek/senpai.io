
from operator import add
import discord
from discord import embeds
from discord.audit_logs import _transform_verification_level
from discord.colour import Color
from discord.ext import commands
from discord.ext.commands.core import Command, command
import random

from discord.user import User

greeting = [
    "welcome to the server , Hope you have a great time here !",
    "",
    "",
    "",
    "",
    "",
    "",
    ""
]
class Generalcomm(commands.Cog):
    def __init__(self , client):
        self.client = client
        


    #EVENTS
    @commands.Cog.listener()
    async def on_ready(self):
        async with self.channel.typing():
            print("general commands  cogs loaded ........")

    @commands.command()
    async def info(self,ctx, member: discord.Member):
        async with ctx.channel.typing():

            embed = discord.Embed(title=member.name , description=member.mention , color= discord.Colour.red())
            embed.add_field(name ="ID", value=member.id , inline=True)
            await ctx.send(embed=embed)

    @commands.command()
    async def server(self , ctx):
        async with ctx.channel.typing():
            embed=discord.Embed(title="hello buddu ")


            await ctx.send(embed=embed)



    @commands.command()
    async def greet(self, ctx , member:discord.Member):
        async with ctx.channel.typing():
            embed= discord.Embed(title="**GREETING**", description=random.choice(greeting))
            embed.set_author(name="Senpai.io" , url=Command.avatar)
            embed.set_footer(text="watching s.server for more help")
            await  ctx.send(embed=embed)





def setup(client):
    client.add_cog(Generalcomm(client))
    print(">>> gerneral commands load ho gaya !!!!!!!!!")