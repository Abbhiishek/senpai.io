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
            time = int(datetime.datetime.now().time())
            await ctx.send(f" ⌚ The current time is {time} ⏲")
    @commands.command()
    async def on_message(self, ctx , msg):
        if msg.content == "what is the day":
            time = int(datetime.datetime.today().weekday())
            if time == 0:
                await ctx.send("Today is Monday Ⓜ")
            if time == 1:
                await ctx.send("Today is Tuesday 🦖")
            if time == 2:
                await ctx.send("Today is Wednesday 🧇")
            if time == 3:
                await ctx.send("Today is Thrusday 🏓")
            if time == 4:
                await ctx.send("Today is Friday 🐳")
            if time == 5:
                await ctx.send("Today is Saturday ♐")
            if time == 6:
                await ctx.send("Today is Sunday ☀")
        



def setup(commands):
    commands.add_cog(message(commands))
    print(">>> gerneral commands load ho gaya !!!!!!!!!")
