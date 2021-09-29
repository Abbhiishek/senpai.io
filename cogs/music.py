import discord
from discord.ext import commands
from discord.player import FFmpegAudio
import youtube_dl
import os



class Music(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.senpai_id = 892408470870057030
    @commands.command()
    async def join (self , ctx):
        if ctx.author.voice is None:
            await ctx.send("You Are Not In Any Voice Channel!!!")
        voice_channel=ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def disconnect(self,ctx):
        await ctx.voice_client.disconnect()
        await ctx.send("The bot is not connected to a voice channel.")


    @commands.command()
    async def play(self , ctx ,url):
        
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn'}
        ydl_opts = {
           'format': "bestaudio"}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url , download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)


    @commands.command()
    async def pause(self,ctx):
        await ctx.voice_client.pause()
        await ctx.send("Senpai Paused The Player")

    @commands.command()
    async def resume(self,ctx):
        await ctx.voice_client.resume()
        await ctx.send("Senpai Resumed The Player")



def setup(client):
    client.add_cog(Music(client))
    print(">>> music load ho gaya hai load ho gaya !!!!!!!!!")
