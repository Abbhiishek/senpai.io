from inspect import currentframe
import discord
from datetime import datetime, time
from discord import Member, Embed
from discord.colour import Color
from discord.ext import commands,tasks

class message(commands.Cog):
    def __init__(self, commands):
        self.commands = commands
        self.senpai_id = 888414036662833164

    @commands.command()
    async def on_message(self, ctx , msg):
        if msg.content == "good morning ":
            await ctx.send("Good Morning !😀")
        
    @commands.command()
    async def on_message(self, ctx , msg):
        if msg.content == "good night ":
            await ctx.send("Good Night! 😪")
        
    @commands.command()
    async def on_message(self, ctx , msg):
        if msg.content == "good evening ":
            await ctx.send("Good Evening! 🤗")
        
    @commands.command()
    async def on_message(self, ctx , msg):
        if msg.content == "good afternoon ":
            await ctx.send("Good Afternoon 🥱")
        
    @commands.command()
    async def on_message(self, ctx , msg):
        if msg.content == "what's up":
            await ctx.send("Good to hear from you ! ^_^ ")
    @commands.command()
    async def on_message(self, ctx , msg):
        if msg.content == "what is the time":
            time = datetime.datetime.now().time()
            
            await ctx.send(f" ⌚ The current time is {datetime.utcnow()} ⏲")
    @commands.command()
    async def on_message(self, ctx , msg):
        if msg.content == "what is the day":
            Time = int(datetime.datetime.today().weekday())
            if Time == 0:
                await ctx.send("Today is Monday Ⓜ")
            if Time == 1:
                await ctx.send("Today is Tuesday 🦖")
            if Time == 2:
                await ctx.send("Today is Wednesday 🧇")
            if Time == 3:
                await ctx.send("Today is Thrusday 🏓")
            if Time == 4:
                await ctx.send("Today is Friday 🐳")
            if Time == 5:
                await ctx.send("Today is Saturday ♐")
            if Time == 6:
                await ctx.send("Today is Sunday ☀")
        



def setup(commands):
    commands.add_cog(message(commands))
    print(">>> gerneral commands load ho gaya !!!!!!!!!")
