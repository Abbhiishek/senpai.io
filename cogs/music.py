import discord
from discord.ext import commands
from discord import utils
import youtube_dl
import os
from discord.voice_client import VoiceClient


class Music(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.senpai_id = 888414036662833164

    @commands.command()
    async def play(self,ctx, url : str): 
        song_there = os.path.isfile("song.mp3")
        try:
             if song_there:
                 os.remove("song.mp3")
        except PermissionError:
            await ctx.send("Wait for the current playing music to end or use the 'stop' command")
            return

        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='🎙General Cafe 🎙')
        await voiceChannel.connect()
        voice = discord.utils.get(commands.voice_clients, guild=ctx.guild)

        ydl_opts = {
           'format': 'bestaudio/best',
            'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
           }],
    }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")
        voice.play(discord.FFmpegPCMAudio("song.mp3"))


    @commands.command()
    async def leave(self,ctx):
        voice = discord.utils.get(commands.voice_clients, guild=ctx.guild)
        if voice.is_connected():
            await voice.disconnect()
        else:
            await ctx.send("The bot is not connected to a voice channel.")


    @commands.command()
    async def pause(self ,ctx):
        voice = discord.utils.get(commands.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
        else:
             await ctx.send("Currently no audio is playing.")


    @commands.command()
    async def resume(self, ctx):
        voice = discord.utils.get(commands.voice_clients, guild=ctx.guild)
        if voice.is_paused():
            voice.resume()
        else:
            await ctx.send("The audio is not paused.")


    @commands.command()
    async def stop(self,ctx):
       voice = discord.utils.get(commands.voice_clients, guild=ctx.guild)
       voice.stop()


def setup(client):
    client.add_cog(Music(client))
    print(">>> music load ho gaya hai load ho gaya !!!!!!!!!")
