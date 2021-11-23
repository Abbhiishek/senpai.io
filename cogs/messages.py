from inspect import currentframe
import discord
import time
from datetime import date, time
from discord import Member, Embed
from discord.colour import Color
from discord.ext import commands,tasks

class message(commands.Cog):
    def __init__(self, commands):
        self.commands = commands
        self.senpai_id = 888414036662833164

    @commands.Cog.listener()
    async def on_message(self,ctx,message):
        if message.content=="good morning":
            await ctx.send("Good Morning !😀")
        
    @commands.Cog.listener()
    async def on_message(self, ctx , msg):
        if msg.content == "good night ":
            await ctx.send("Good Night! 😪")
        
    @commands.Cog.listener()
    async def on_message(self, ctx , msg):
        if msg.content == "good evening ":
            await ctx.send("Good Evening! 🤗")
        
    @commands.Cog.listener()
    async def on_message(self, ctx , msg):
        if msg.content == "good afternoon ":
            await ctx.send("Good Afternoon 🥱")
        
    @commands.Cog.listener()
    async def on_message(self, ctx , msg):
        if msg.content == "what's up":
            await ctx.send("Good to hear from you ! ^_^ ")
    @commands.Cog.listener()
    async def on_message(self, ctx , * , msg):
        if msg.content == "what is the time":
            time = date.today()
            isoTime= time.isoformat()
            
            await ctx.send(f" ⌚ The current time is {isoTime} ⏲")
    @commands.Cog.listener()
    async def on_message(self, ctx , msg):
        if msg.content == "what is the day":
            Time = date.today().weekday()
            if Time == 0:
                await ctx.send("Today is Monday Ⓜ")
            elif Time == 1:
                await ctx.send("Today is Tuesday 🦖")
            elif Time == 2:
                await ctx.send("Today is Wednesday 🧇")
            elif Time == 3:
                await ctx.send("Today is Thrusday 🏓")
            elif Time == 4:
                await ctx.send("Today is Friday 🐳")
            elif Time == 5:
                await ctx.send("Today is Saturday ♐")
            elif Time == 6:
                await ctx.send("Today is Sunday ☀")
        



def setup(commands):
    commands.add_cog(message(commands))
    print(">>> messgaes commands load ho gaya !!!!!!!!!")
