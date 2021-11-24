from inspect import currentframe
import discord
import time
from datetime import date, time,datetime
from discord import Member, Embed
from discord.colour import Color
from discord.ext import commands,tasks

class message(commands.Cog):
    def __init__(self, commands):
        self.commands = commands
        self.senpai_id = 888414036662833164

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content=="good morning":
            await message.reply("Good Morning !😀")
            await self.client.process_commands(message)
        elif message.content == "good night ":
            await message.reply("Good Night! 😪")
            await self.client.process_commands(message)
        elif message.content == "good evening ":
            await message.reply("Good Evening! 🤗")
            await self.client.process_commands(message)
        elif message.content == "good afternoon ":
            await message.reply("Good Afternoon 🥱")
            await self.client.process_commands(message)
        elif message.content == "what's up":
            await message.reply("Good to hear from you ! ^_^ ")
            await self.client.process_commands(message)
        elif message.content == "what is the date":
            time = date.today()
            isoTime= time.isoformat()
            await message.reply(f" ⌚ Today's Date  is {isoTime} ⏲")
            await self.client.process_commands(message)
        elif message.content == "what is the time":
            time =datetime.time()
            isoTime= time.isoformat()
            await message.reply(f" ⌚ The current time is {isoTime} ⏲")
            await self.client.process_commands(message)
        elif message.content == "what is the day":
            Time = date.today().weekday()
            if Time == 0:
                await message.reply("Today is Monday Ⓜ")
                await self.client.process_commands(message)
            elif Time == 1:
                await message.reply("Today is Tuesday 🦖")
                await self.client.process_commands(message)
            elif Time == 2:
                await message.reply("Today is Wednesday 🧇")
                await self.client.process_commands(message)
            elif Time == 3:
                await message.reply("Today is Thrusday 🏓")
                await self.client.process_commands(message)
            elif Time == 4:
                await message.reply("Today is Friday 🐳")
                await self.client.process_commands(message)
            elif Time == 5:
                await message.reply("Today is Saturday ♐")
                await self.client.process_commands(message)
            elif Time == 6:
                await message.reply("Today is Sunday ☀")
                await self.client.process_commands(message)
        
    # @commands.Cog.listener("on_message")
    # async def on_message(self, message):
    #     if message.content == "good night ":
    #         await message.reply("Good Night! 😪")
        
    # @commands.Cog.listener("on_message")
    # async def on_message(self, message):
    #     if message.content == "good evening ":
    #         await message.reply("Good Evening! 🤗")
        
    # @commands.Cog.listener("on_message")
    # async def on_message(self, message):
    #     if message.content == "good afternoon ":
    #         await message.reply("Good Afternoon 🥱")
        
    # @commands.Cog.listener("on_message")
    # async def on_message(self, message):
    #     if message.content == "what's up":
    #         await message.reply("Good to hear from you ! ^_^ ")
    # @commands.Cog.listener("on_message")
    # async def on_message(self,  message):
    #     if message.content == "what is the time":
    #         time = date.today()
    #         isoTime= time.isoformat()
            
    #         await message.reply(f" ⌚ The current time is {isoTime} ⏲")
    # @commands.Cog.listener("on_message")
    # async def on_message(self, message):
    #     if message.content == "what is the day":
    #         Time = date.today().weekday()
    #         if Time == 0:
    #             await message.reply("Today is Monday Ⓜ")
    #         elif Time == 1:
    #             await message.reply("Today is Tuesday 🦖")
    #         elif Time == 2:
    #             await message.reply("Today is Wednesday 🧇")
    #         elif Time == 3:
    #             await message.reply("Today is Thrusday 🏓")
    #         elif Time == 4:
    #             await message.reply("Today is Friday 🐳")
    #         elif Time == 5:
    #             await message.reply("Today is Saturday ♐")
    #         elif Time == 6:
    #             await message.reply("Today is Sunday ☀")
        



def setup(commands):
    commands.add_cog(message(commands))
    print(">>> messgaes commands load ho gaya !!!!!!!!!")
