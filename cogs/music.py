import discord
from discord import player
from discord.ext import commands
from discord.ext.commands.core import command
from discord.player import FFmpegAudio
import youtube_dl
import os
import DiscordUtils


music = DiscordUtils.Music()


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
        player = music.get_player(guild_id=ctx.guild.id)
        if not player :
            player = music.create_player(ctx, ffmpeg_error_betterfix=True)
        if not ctx.voice_client.is_playing():
            await player.queue(url , search= True)
            song= await player.play()
            await ctx.send (f' I Have Started Playing --{song.name}')
        else:
            song= await player.queue(url, search =True)
            await ctx.send(f"{','.join([song.name for song in player.current_queue()])}")



    @commands.command()
    async def queue(self,ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.pause()
        await ctx.send(f"Senpai Paused The song {song.name}")



    @commands.command()
    async def pause(self,ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.pause()
        await ctx.send(f"Senpai Paused The song {song.name}")

    @commands.command()
    async def resume(self,ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.resume()
        await ctx.send(f"Senpai Resumed The song {song.name}")

    @commands.command()
    async def loop(self, ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.toggle_song_loop()
        if song.is_looping:
            return await ctx.send(f'{song.name} is looping ')
        else:
            return await ctx.send(f'{song.name} is not looping ')

    @commands.command()
    async def nowplaying(self , ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song= player.now_playing()
        await ctx.send(song.name)


def setup(client):
    client.add_cog(Music(client))
    print(">>> music load ho gaya hai load ho gaya !!!!!!!!!")
