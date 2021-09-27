import discord
from discord.ext import commands, tasks
from discord.voice_client import VoiceClient
import youtube_dl
import asyncio
from random import choice
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class Music(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.senpai_id = 888414036662833164

    @commands.command()
    async def play(ctx, url):
        
        channel = ctx.message.author.voice.channel

        await channel.connect()

        server = ctx.message.guild
        voice_channel = server.voice_client

        async with ctx.typing():
             player = await YTDLSource.from_url(url, loop=commands.loop)
             voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

        await ctx.send('**Now playing:** {}'.format(player.title))


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
       voice = discord.utils.get(commands.voice_commands, guild=ctx.guild)
       voice.stop()


def setup(client):
    client.add_cog(Music(client))
    print(">>> music load ho gaya hai load ho gaya !!!!!!!!!")