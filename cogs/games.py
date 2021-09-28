import discord
from discord.ext import commands
import random
import json
import requests
from discord import utils
from discord_components import DiscordComponents, Button, Select, SelectOption, ButtonStyle
import asyncio
from PIL import Image, ImageDraw


class Games(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.senpai_id = 888414036662833164

    # EVENTS
    @commands.Cog.listener()
    async def on_ready(self):
        async with self.channel.typing():
            print("games cogs loaded ........")

    # COMMANDS
    @commands.command()
    async def Games(self, ctx):
        async with ctx.channel.typing():

            GAMES_embed = discord.Embed(title="GAMES", color=0x2e69f2)
            GAMES_embed.add_field(
                name="🌚 **TRUTH OR DARE**",
                    value="`senpai help td`",
                inline=True
            )
            GAMES_embed.add_field(
                name="🎰 **LOTTERY**",
                value="`senpai help lotto`",
                inline=True
            )

            GAMES_embed.add_field(
                name="🤔 **HIGHLOW**",
                value="`senpai highlow`",
                inline=True
            )
            GAMES_embed.add_field(
                name="✍ **UNSCRAMBLE**",
                value="`senpai uns`",
                inline=True
            )

            GAMES_embed.add_field(
                name="🙌 **RPS**",
                value="`kana rps`",
                inline=True
            )
            GAMES_embed.set_footer(text=">>>>Games by senpai.io<<<<")
            await ctx.send(embed=GAMES_embed)

    @commands.command()
    async def dare(self, ctx):
        dare = [
            "Show the most embarrassing photo on your phone",
            "Show the last five people you texted and what the messages said",
            "Let the rest of the group DM someone from your Instagram account",
            "Eat a raw piece of garlic",
            "Do 100 squats",
            "Keep three ice cubes in your mouth until they melt",
            "Say something dirty to the person on your left",
            "Give a foot massage to the person on your right",
            "Put 10 different available liquids into a cup and drink it",
            "Yell out the first word that comes to your mind",
            "Give a lap dance to someone of your choice",
            "Remove four items of clothing",
            "Like the first 15 posts on your Facebook newsfeed",
            "Eat a spoonful of mustard",
            "Keep your eyes closed until it's your go again",
            "Send a text to the last person in your phonebook",
            "Show off your orgasm face",
            "Seductively eat a banana",
            "Empty out your wallet/purse and show everyone what's inside",
            "Do your best sexy crawl",
            "Pretend to be the person to your right for 10 minutes",
            "Eat a snack without using your hands",
            "Say two honest things about everyone else in the group",
            "Twerk for a minute",
            "Try and make the group laugh as quickly as possible",
            "Try to put your whole fist in your mouth",
            "Tell everyone an embarrassing story about yourself",
            "Try to lick your elbow",
            "Post the oldest selfie on your phone on Instagram Stories",
            "Tell the saddest story you know",
            "Howl like a wolf for two minutes",
            "Dance without music for two minutes",
            "Pole dance with an imaginary pole",
            "Let someone else tickle you and try not to laugh",
            "Put as many snacks into your mouth at once as you can",
        ]
        async with ctx.channel.typing():
            await ctx.send(f"Dare: {random.choice(dare)}")

    @commands.command()
    async def truth(self, ctx):
        truth = [
            "When was the last time you lied?",
            "When was the last time you cried?",
            "What's your biggest fear?",
            "What's your biggest fantasy?",
            "Do you have any fetishes?",
            "What's something you're glad your mum doesn't know about you?",
            "Have you ever cheated on someone?",
            "What's the worst thing you've ever done?",
            "What's a secret you've never told anyone?",
            "Do you have a hidden talent?",
            "Who was your first celebrity crush?",
            "What are your thoughts on politicians?",
            "What's the worst intimate experience you've ever had?",
            "Have you ever cheated in an exam?",
            "What's the most drunk you've ever been?",
            "Have you ever broken the law?",
            "What's the most embarrassing thing you've ever done?",
            "What's your biggest insecurity?",
            "What's the biggest mistake you've ever made?",
            "What's the most disgusting thing you've ever done?",
            "Who would you like to kiss in this server?",
            "What's the worst thing anyone's ever done to you?",
            "Have you ever had a run in with the law?",
            "What's your worst habit?",
            "What's the worst thing you've ever said to anyone?",
            "Have you ever peed in the shower?",
            "What's the strangest dream you've had?",
            "Have you ever been caught doing something you shouldn't have?",
            "What's the worst date you've been on?",
            "What's your biggest regret?",
            "What's the biggest misconception about you?",
            "Are you virgin?",
            "Why did your last relationship break down?",
            "Have you ever lied to get out of a bad date?",
            "What's the most trouble you've been in?",
        ]

        async with ctx.channel.typing():
            await ctx.send(f"Truth: {random.choice(truth)}")

    

    @commands.command()
    async def tictao(self , ctx ):    
        await ctx.send("this fucking game is not playable now?!?!?!?!?!")    


    @commands.command()
    async def riddle(self, ctx):
        async with ctx.channel.typing():
            await ctx.send("this game is under code \n pls try again after one year \n Since Master Abhishek Is Busy")


    @commands.command(aliases=['lotto'])
    async def lottery(self, ctx, *, guesses):
        #Enter the lottery and see if you win!
        numbers = []
        for x in range(3):
            numbers.append(random.randint(0, 9))

        split = guesses.split(' ')
        if len(split) != 3:
            return await ctx.send('Please separate your numbers with a space, and make sure there are 3 numbers between 0 and 9.')
        string_numbers = [str(i) for i in numbers]
        if split[0] == string_numbers[0] and split[1] == string_numbers[1] and split[2] == string_numbers[2]:
            await ctx.send(f'{ctx.author.mention} You won! Congratulations on winning the lottery!')
        else:
            await ctx.send(f"{ctx.author.mention} Better luck next time... You were one of the 124/125 who lost the lottery...\nThe numbers were `{', '.join(string_numbers)}`")
  
    @commands.command()
    async def rps(self, ctx):
        def return_embed(kana, user):
            cond = ""
            if kana == user:
                cond = "t"
            game = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
            if game[user] == kana:
                cond = "w"
            elif game[user] != kana and kana != user:
                cond = "l"
            if cond == "t":
                emb = discord.Embed(title=f"{ctx.author.display_name}'s RPS game!", description="**🙂 Oops, It's a draw..\nTry again :)**", color=0x2e69f2)
                return emb
            elif cond == "w":
                emb = discord.Embed(title=f"{ctx.author.display_name}'s RPS game!", description=f"**😏 You won the game!\nI chose {kana} and you chose {user}!**", color=0x2e69f2)
                return emb
            elif cond == "l":
                emb = discord.Embed(title=f"{ctx.author.display_name}'s RPS game!", description=f"**😞 You lost the game, Better luck next time..\nI chose {kana} and you chose {user}.**", color=0x2e69f2)
                return emb


        emb = discord.Embed(title=f"{ctx.author.display_name}'s RPS game!", description="**rock, paper, scissors..\nClick on any one button to play the game!**", color=0x2e69f2)
        msg=await ctx.send(embed=emb,
            components=[
                [
                Button(style=ButtonStyle.blue, label="Rock", emoji="✊"),
                Button(style=ButtonStyle.red, label="Paper", emoji="🤚"),
                Button(style=ButtonStyle.green, label="Scissors", emoji="✌")
                ],
            ],
        )
        try:
            def check(resp):
                return resp.user == ctx.author and resp.channel == ctx.channel
        
            resp = await self.client.wait_for("button_click", check=check, timeout=60)
            bot = random.choice(["rock", "paper", "scissors"])
            player = resp.component.label.lower()
            embed = return_embed(bot, player)
            await resp.respond(type=7, embed=embed,
                components=[
                    [
                    Button(style=ButtonStyle.blue, label="Rock", emoji="✊", disabled=True),
                    Button(style=ButtonStyle.red, label="Paper", emoji="🤚", disabled=True),
                    Button(style=ButtonStyle.green, label="Scissors", emoji="✌", disabled=True)
                    ],
                ],
            ) 
        except asyncio.TimeoutError:
            await msg.edit(components=[[
                Button(style=ButtonStyle.blue, label="Rock", emoji="✊", disabled=True),
                Button(style=ButtonStyle.red, label="Paper", emoji="🤚", disabled=True),
                Button(style=ButtonStyle.green, label="Scissors", emoji="✌", disabled=True),
                ],],)

    @commands.command(aliases=['hl'])
    async def highlow(self, ctx,):
        def return_embed(num1, num2, guess):
            cond = ""
            if num1 == num2:
                cond = "t"
            elif num1 > num2 and guess == "high":
                cond = "w"
            elif num1 < num2 and guess == "low":
                cond = "w"
            else:
                cond = "l"
            if cond == "t":
                emb = discord.Embed(title=f"{ctx.author.display_name}'s HIGHLOW game!", description=f"**😏 woah, It's a JACKPOT!!\nThe number was exactly {num2}!**", color=0x2e69f2)
                return emb
            elif cond == "w":
                emb = discord.Embed(title=f"{ctx.author.display_name}'s HIGHLOW game!", description=f"**🙂 You won the game!\nThe number was {num1}!**", color=0x2e69f2)
                return emb
            elif cond == "l":
                emb = discord.Embed(title=f"{ctx.author.display_name}'s HIGHLOW game!", description=f"**😞 You lost the game, Better luck next time..\nThe number was {num1}.**", color=0x2e69f2)
                return emb
        n1 = random.randint(1, 100)
        n2 = random.randint(1, 100)
        emb = discord.Embed(title=f"{ctx.author.display_name}'s HIGHLOW game!", description=f"**Guess whether the number is higher or lower than {n2}.\nYou have 30s to answer!**", color=0x2e69f2)
        msg=await ctx.send(embed=emb,
            components=[
                [
                Button(style=ButtonStyle.blue, label="HIGH", emoji=discord.PartialEmoji(name="KannaAwh", id="758724574010409071")),
                Button(style=ButtonStyle.blue, label="JACKPOT!", emoji=discord.PartialEmoji(name="RWKannaSmug", id="762995028200128522")),
                Button(style=ButtonStyle.blue, label="LOW", emoji=discord.PartialEmoji(name="kannah", id="873191866387013654"))
                ],
            ],
        )
        try:
            def check(resp):
                return resp.user == ctx.author and resp.channel == ctx.channel
        
            resp = await self.client.wait_for("button_click", check=check, timeout=30)
            player = resp.component.label.lower()
            embed = return_embed(n1, n2, player)
            await resp.respond(type=7, embed=embed,
                components=[
                    [
                    Button(style=ButtonStyle.blue, label="HIGH", emoji=discord.PartialEmoji(name="KannaAwh", id="758724574010409071"), disabled=True),
                    Button(style=ButtonStyle.blue, label="JACKPOT!", emoji=discord.PartialEmoji(name="RWKannaSmug", id="762995028200128522"), disabled=True),
                    Button(style=ButtonStyle.blue, label="LOW", emoji=discord.PartialEmoji(name="kannah", id="873191866387013654"), disabled=True)
                    ],
                ],
            ) 
        except asyncio.TimeoutError:
            await msg.edit(components=[[
                Button(style=ButtonStyle.blue, label="HIGH", emoji=discord.PartialEmoji(name="KannaAwh", id="758724574010409071"), disabled=True),
                Button(style=ButtonStyle.blue, label="JACKPOT!", emoji=discord.PartialEmoji(name="RWKannaSmug", id="762995028200128522"), disabled=True),
                Button(style=ButtonStyle.blue, label="LOW", emoji=discord.PartialEmoji(name="kannah", id="873191866387013654"), disabled=True)
                ],],)

    
def setup(client):
    client.add_cog(Games(client))
    print(">>> games load ho gaya !!!!!!!!!")
