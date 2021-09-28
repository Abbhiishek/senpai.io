import discord
from discord.ext import commands
from discord_components import DiscordComponents, Button, Select, SelectOption
import asyncio


aboutemb = discord.Embed(title="I GUESS YOU ASKED FOR HELP !!", description="BOT CREATOR:\n [**ABHISHEK KUSHWAHA**](https://github.com/Abbhiishek)\n `Abbhishek#2959`",color=0x2e69f2)
aboutemb.add_field(
    name=" **PREFIX**", 
    value=f"senpai ; s. ; S.", 
    inline=True
)
aboutemb.add_field(
    name=" **SOURCE**",
    value=f"Send `senpai source`",
    inline=True
)
aboutemb.add_field(
    name="**INVITE ME**",
    value=f"[Click here](https://discord.com/api/oauth2/authorize?client_id=857835279259664403&permissions=138445974593&scope=bot%20applications.commands)",
    inline=True
)

aboutemb.add_field(
    name=" **ABOUT**",
    value=f"[Click here](https://github.com/Abbhiishek/senpai.io/blob/main/README.md)",
    inline=True
)
aboutemb.add_field(
    name=" **CUSTOM HELP**",
    value="IN WHICH EVER TOPIC YOU NEED HELP \n JUST TYPE IT WITH HELP KEYWORD \n LIKE FOR GAMES <senpai help games>",
    inline=True
)



generalemb = discord.Embed(title=" **Gerenal-commands**", color=0x2e69f2)
generalemb.add_field(
    name=" WELCOME MESSAGE",
    value="`senpai wsetup #nel` Setup a nel where senpai will welcome new members in your server!\n**It's an Admin/Mod only command**",
    inline=False
)
generalemb.add_field(
    name="SERVER",
    value="`senpai server ` Shows the server stats !\n**It's an Admin/Mod only command \n need server insight permisssion**",
    inline=False
)
generalemb.add_field(
    name=" INFO",
    value="`senpai info #nel` Setup a nel where senpai will welcome new members in your server!\n**It's an Admin/Mod only command**",
    inline=False
)
generalemb.add_field(
    name=" VERSION",
    value="`senpai version`show the version of the bot!\n",
    inline=False
)
generalemb.add_field(
    name="STATUS",
    value="`senpai status` shows the whole status of the bot!\n**It's an Admin/Mod only command**",
    inline=False
)

respemb = discord.Embed(title="**RESPONSES**", color=0x2e69f2)
respemb.add_field(
    name=" SIMP",
    value="`senpai simp @user` senpai sends a pickup line for the mentioned person with a cute gif uwu.",
    inline=True
)
respemb.add_field(
    name=" ROAST",
    value="`senpai roast @user` Roast anyone .",
    inline=True
)

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.senpai_id = 888414036662833164

    @commands.command()
    async def help(self, ctx):
        senpai = self.client.get_user(self.senpai_id)
        await ctx.send("Use this embed for help regarding any commands. ",embed=aboutemb)
        
    @commands.command()
    async def help_games(self,ctx):
        helpgamesemb=discord.Embed(title="HELP REGARDING GAMES",description=" For Games Help Type--\n senpai games" ,color=0x2e69f2)
        await ctx.send(embed=helpgamesemb)

    @commands.command()
    async def help_actions(self,ctx):
        helpactionsemb=discord.Embed(title="HELP REGARDING ACTION",description=" For Games Help Type--\n senpai actions" ,color=0x2e69f2)
        await ctx.send(embed=helpactionsemb)
    
    @commands.command()
    async def help_general(self,ctx):
        helpgeneralemb=discord.Embed(title="HELP REGARDING GERENAL COMMANDS",description=" For Games Help Type--\n senpai general" ,color=0x2e69f2)
        await ctx.send(embed=helpgeneralemb)
    @commands.command()
    async def help_music(self,ctx):
        helpmusicemb=discord.Embed(title="HELP REGARDING MUSICS",description=" For Games Help Type--\n senpai music" ,color=0x2e69f2)
        await ctx.send(embed=helpmusicemb)

    

 
def setup(client):
    client.add_cog(Help(client))
    print(">> Help loaded")
