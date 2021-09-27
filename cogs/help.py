import discord
from discord.ext import commands
from discord_components import DiscordComponents, Button, Select, SelectOption
import asyncio

gemb = discord.Embed(title="GAMES", color=0x2e69f2)
gemb.add_field(
    name=" **TRUTH OR DARE**",
    value="`senpai help tod`",
    inline=True
)
gemb.add_field(
    name=" **LOTTERY**",
    value="`senpai help lotto`",
    inline=True
)

gemb.add_field(
    name=" **HIGHLOW**",
    value="`senpai highlow`",
    inline=True
)
gemb.add_field(
    name=" **UNSCRAMBLE**",
    value="`senpai uns`",
    inline=True
)
gemb.add_field(
    name=" **RIDDLE**",
    value="`senpai riddle`",
    inline=True
)

avemb = discord.Embed(title=" **AVATAR**", description="**Command**: `av`, `avatar`, `pfp`\n`senpai av @user` Sends avatar of mentioned person. If no one is mentioned senpai sends your avatar.\n\n`senpai av @user1 @user2` Sends the merged pfp of two users (matching pfp uwu).\n\n**ENLARGE USER BANNER**\n**Command**: `bnr`, `banner`, `bn`\n`senpai bnr @user` Sends banner of mentioned person. If no one is mentioned senpai sends your banner by default.", color=0x2e69f2)

aboutemb = discord.Embed(title="I GUESS YOU NEEDED FOR HELP !!", description="BOT CREATOR: [**ABHISHEK KUSHWAHA**](https://github.com/Abbhiishek) `Abbhishek#2959`",color=0x2e69f2)
aboutemb.add_field(
    name=" **PREFIX**", 
    value=f"Send `senpai prefix`", 
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


h = discord.Embed(
            title="ACTIONS",
            description="**AVAILABLE ACTIONS**\n`pat`, `hug   `, `cuddle  `, `kiss  `, `bonk  `, `kill  `, `punch  `, `highfive  `, `feed  `, `nom  `, `slap  `, `pout  `, `smug  `, `tickle  `, `poke  `, `blush  `.",
            color=0x2e69f2
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
    async def help(self, ctx, *, topic=None):
        senpai = self.client.get_user(self.senpai_id)
        if topic == None:
            try:
                msg = await ctx.send("Use this embed for help regarding any commands. ",embed=aboutemb,
                    components=[
                        Select(placeholder="Select", options=[
                        SelectOption(label="General", value="general",  default=True),
                        SelectOption(label="Games", value="games"),
                        SelectOption(label="Avatar & Banner", value="avatar"),
                        SelectOption(label="Actions", value="actions"),
                        SelectOption(label="Responses", value="responses"),

                        ]
                        )
                    ]
                )
                try:
                    while True:
                        def check(interaction):
                            return interaction.user==ctx.author and interaction.channel == ctx.channel
                        interaction = await self.client.wait_for("select_option",check=check, timeout=40)
                        print(interaction.values[0])
                        response = interaction.values[0]
                        if response.lower() == "general":
                            await interaction.respond(type=7, embed=generalemb, components=[
                            Select(placeholder="Select", options=[
                            SelectOption(label="General", value="general",  default=True),
                            SelectOption(label="Games", value="games"), 
                            SelectOption(label="Avatar & Banner", value="avatar & banner"),
                            SelectOption(label="Actions", value="actions"),
                            SelectOption(label="Responses", value="responses"),
                            ])])
                        elif response.lower() == "games":
                            await interaction.respond(type=7, embed=gemb, components=[
                            Select(placeholder="Select", options=[
                            SelectOption(label="General", value="general" ),
                            SelectOption(label="Games", value="games", default=True), 
                            SelectOption(label="Avatar & Banner", value="avatar & banner"),
                            SelectOption(label="Actions", value="actions"),                                                       
                            SelectOption(label="Responses", value="responses")
                            ])])
                        elif response.lower() == "avatar & banner":
                            await interaction.respond(type=7,content="Join senpai's Server for fun emotes and cool events discord.gg/7CYP8pKzDB", embed=avemb, components=[
                            Select(placeholder="Select", options=[
                            SelectOption(label="General", value="general" ,default=True), 
                            SelectOption(label="Games", value="games"), 
                            SelectOption(label="Avatar & Banner", value="avatar & banner"),
                            SelectOption(label="Actions", value="actions"),
                            SelectOption(label="Responses", value="responses"),
                            ])])
                        elif response.lower() == "actions":
                            await interaction.respond(type=7,content="Join senpai's Server for fun emotes and cool events discord.gg/7CYP8pKzDB", embed=h, components=[
                            Select(placeholder="Select", options=[
                            SelectOption(label="General", value="general"),
                            SelectOption(label="Games", value="games"), 
                            SelectOption(label="Avatar & Banner", value="avatar & banner"),
                            SelectOption(label="Actions", value="actions"),                           
                            SelectOption(label="Responses", value="responses"),
                            ])])
                        elif response.lower() == "responses":
                            await interaction.respond(type=7,content="Join senpai's Server for fun emotes and cool events discord.gg/7CYP8pKzDB", embed=respemb, components=[
                            Select(placeholder="Select", options=[
                            SelectOption(label="General", value="general"), 
                            SelectOption(label="Games", value="games"),
                            SelectOption(label="Avatar & Banner", value="avatar & banner"),
                            SelectOption(label="Actions", value="actions"),
                            SelectOption(label="Responses", value="responses", default=True),
                            ])])
                        
                except asyncio.TimeoutError:
                    await msg.edit(components=[
                            Select(placeholder="Select", options=[
                            SelectOption(label="General", value="general"),
                            SelectOption(label="Games", value="games", default=True), 
                            SelectOption(label="Avatar & Banner", value="avatar & banner"),
                            SelectOption(label="Actions", value="actions"),
                            SelectOption(label="Responses", value="responses"),
                            ], disabled = True)])            
                
            except Exception as e:
                print(e)
        elif topic.lower() == "bot":
            emb = discord.Embed(title="MAKE ME BOT", description="Turn yourself into bot! To use send ~ \n`senpai bot (your message without brackets)` and senpai will delete your message and make your message be sent by bot with your name and pfp!\n**Permission Needed: Manage Webhooks**", color=0x2e69f2)
            emb.set_footer(
            text=f"senpai.io",
            icon_url=senpai.avatar_url,
            )
            await ctx.send(embed=emb)
        
        elif topic.lower() == "tod":
            emb = discord.Embed(title="TRUTH OR DARE", description="Start a game of truth or dare using senpai.io!\nFor truth send `senpai truth` and for dare send `senpai dare`.", color=0x2e69f2)
            emb.set_image(url="https://is1-ssl.mzstatic.com/image/thumb/Purple125/v4/af/71/bc/af71bca4-9c75-2ae3-5dca-490286d51284/AppIcon-0-0-1x_U007emarketing-0-0-0-7-0-0-sRGB-0-0-0-GLES2_U002c0-512MB-85-220-0-0.jpeg/1200x630wa.png")
            emb.set_footer(
            text=f"senpai.io",
            icon_url=senpai.avatar_url,
            )
            await ctx.send(embed=emb)
        elif topic.lower() == "lotto":
            emb = discord.Embed(title="LOTTERY", description="Start a game of lattery using senpai.\nYou will have to send three random numbers between 0 to 5 with space in between like `senpai lottery 1 3 4`.", color=0x2e69f2)
            emb.set_footer(
            text=f"senpai.io",
            icon_url=senpai.avatar_url,
            )
            await ctx.send(embed=emb)
        
        else:
            await ctx.send("senpai was not able to find help for this command..does this even exist?")

    @commands.command()
    async def source(self, ctx):
        await ctx.send("https://github.com/AsheeshhSenpai/senpai-")
        
    

    @commands.command()
    async def invite(self, ctx):
        emb = discord.Embed(title="INVITE SENPAI.IO!!", description="Invite SENPAI  in your server uwu\n[Click here](https://discord.com/api/oauth2/authorize?client_id=888414036662833164&permissions=3394560&scope=bot)", color=0x2e69f2)
        senpai = self.client.get_user(self.senpai_id)
        emb.set_footer(
            text=f"SENPAI.IO",
            icon_url=senpai.avatar_url,
        )
        await ctx.send(embed=emb)

    @commands.command()
    async def prefix(self, ctx):
        await ctx.send("Prefixes for senpai are `s.`, `senpai ` and `S. `.")

 
def setup(client):
    client.add_cog(Help(client))
    print(">> Help loaded")
