import discord
from discord import colour
from discord import embeds
from discord import user
from discord import message
from discord.ext import commands
import os

class MOD(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.senpai_id = 888414036662833164

    # EVENTS
    @commands.Cog.listener()
    async def on_ready(self):
        async with self.channel.typing():
            print("mod cogs loaded ........")
    @commands.command
    async def on_message(self,msg):
        file=open(r"./cogs/banned_words.json","r")
        for words in file:
            if words in msg.content:
                await msg.purge()
        await commands.process_commands(msg)

    
    # COMMANDS
    @commands.command()
    @commands.has_permissions(ban_members= True)
    async def abw(self,ctx,message : str):
        file=open(r"./cogs/banned_words.json","rb+")
        if message in file :
            await ctx.send('Word already there !')
        else:
            file.write(message)
            file.write('\n')
            file.close()
            await ctx.send(message+ "added to the banned words")

    @commands.command()
    @commands.has_permissions(ban_members= True)
    async def ban(self,ctx , user : discord.user= None, reason= None):
        if user == None or user == ctx.message.author:
            em = discord.Embed(title="Ban", description ='You cannot  BAN  yourself >/',colour=discord.Color.red())
            await ctx.channel.send(embed=em)
            return
        if reason == None:
            reason = "REASON NOT SPECIFIED !!!"
        await ctx.user.ban()
        em1 = discord.Embed(title="Ban", description =f'{user} has been banned >/ from {ctx.guild.name} because of : {reason}',colour=discord.Color.red())
        await ctx.send(embed=em1)
    @commands.command()
    @commands.has_permissions(ban_members= True)
    async def unban(self,ctx , * , member):
        banned_user = await ctx.guild.bans()
        member_name ,member_disc = member.spilt('#')
        for banned_entry in banned_user:
            user=banned_entry.user

            if (user.name , user.discriminator) == (member_name, member_disc):
                em3=discord.Embed(title="UnBan", description =f'{user} has been unbanned >/ from {ctx.guild.name}',colour=discord.Color.red())
                await ctx.send (embed=em3)
                return
            await ctx.send(member+ 'was not found in the server!')
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(self,ctx,member:discord.Member):
        muted_role = ctx.guild.get_role(911098944044531753)
        await member.add_roles(muted_role)
        await ctx.send(member.mention+"Has been `MUTED`")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def Unmute(self,ctx,member:discord.Member):
        muted_role = ctx.guild.get_role(911098944044531753)
        await member.remove_roles(muted_role)
        await ctx.send(member.mention+"Has been `MUTED`")


def setup(client):
    client.add_cog(MOD(client))
    print(">>> moderation  load ho gaya !!!!!!!!!")
