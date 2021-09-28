import discord
from discord import embeds
from discord.ext import commands
import random
import json
import requests
from discord import utils
import asyncio
from discord.user import User
from random import choice


slap_gifs = [
    "https://c.tenor.com/6HwcYSSpszUAAAAC/hamsteak-hammy.gif",
    "https://c.tenor.com/rJpHDhh3jDEAAAAd/slap-slapping.gif",
    "https://c.tenor.com/Ws6Dm1ZW_vMAAAAC/girl-slap.gif",
    "https://c.tenor.com/EfhPfbG0hnMAAAAC/slap-handa-seishuu.gif",
    "https://c.tenor.com/cM-pYb791poAAAAC/back-slap-backhand.gif",
    "https://c.tenor.com/L0U84S9YTrYAAAAC/pikachu-slap.gif",
    "https://c.tenor.com/OYYTU-ShQTIAAAAd/slapping-wet-slap.gif",
    "https://c.tenor.com/EzwsHlQgUo0AAAAC/slap-in-the-face-angry.gif",
]

smirk_gifs = [
    "https://c.tenor.com/spYJzEXz8BsAAAAC/smirk-ryan-reynolds.gif",
    "https://c.tenor.com/BEojRq5dfQsAAAAd/smile-evil-smile.gif",
    "https://c.tenor.com/DsltXyB5fJQAAAAd/smirk-funny.gif",
    "https://c.tenor.com/KNEnPw-KrekAAAAd/naughty-dog.gif",
    "https://c.tenor.com/vYS9rGpnqiIAAAAC/smug-anime.gif",
    "https://c.tenor.com/Z-HudBx1fJIAAAAd/bts-bangtan-boys.gif",
    "https://c.tenor.com/H_f_Bf7scj4AAAAC/jyugo-nanbaka.gif",
    "https://c.tenor.com/EqmQKDJghk4AAAAC/anime-pink-lips.gif",
    "https://c.tenor.com/8utxYD5HDKgAAAAC/sasuke-grin.gif",
    "https://c.tenor.com/sWgHS98drkgAAAAC/spongebob-evil-smile.gif",
    ""
]

highfive_gifs =[
    "https://c.tenor.com/mpCnVpX0xIYAAAAC/high-five-spongebob.gif",
    "https://c.tenor.com/eCtm70W3J2QAAAAS/borat-high-five.gif",
    "https://c.tenor.com/2oPrdhJpUpEAAAAS/kuzco-yzma.gif",
    "https://c.tenor.com/ZfU8QUZXq30AAAAS/high-five.gif",
    "https://c.tenor.com/Pfi1xdN7JvYAAAAS/cat-animated.gif",
    "https://c.tenor.com/q6PnbtGXo5AAAAAS/tos-high-five.gif",
    "https://c.tenor.com/UMADm-COXgcAAAAS/monday-high-five.gif",
]

punch_gifs =[
    "https://c.tenor.com/wvCSg5-wYssAAAAS/nope-stupid.gif",
    "https://c.tenor.com/_DOU2Mi1TG0AAAAS/dean-winchester-punch.gif",
    "https://c.tenor.com/29hGOXF71nkAAAAS/grab-and-punch-grab-n-punch.gif",
    "https://c.tenor.com/--80HfIQWT4AAAAS/punchy-one-punch-man.gif",
    "https://c.tenor.com/25f3EArLzgcAAAAd/punch-in-the-face-joshua-buatsi.gif",
    "https://c.tenor.com/rjR2Z67erfkAAAAS/death-saitama.gif",
    "https://c.tenor.com/1PwavmgiEK0AAAAd/onepunchman-punch.gif",
]

poke_gifs = [ 
    "https://c.tenor.com/G3JseGtZ31kAAAAd/h%C3%A1mster-susto.gif",
    "https://c.tenor.com/QDNTqOInK5MAAAAC/anime-poke.gif",
    "https://c.tenor.com/ubtPHkuWkGgAAAAC/baymax-big-hero6.gif",
    "https://c.tenor.com/YbemOLXA_UIAAAAd/octopus-touch.gif"
]

simp_gifs = [
    "https://i.imgur.com/RlrlmmP.gif",
    "https://c.tenor.com/nOARJZENR9UAAAAS/anime-in-love.gif",
    "https://c.tenor.com/hCqcNUuWCf0AAAAS/blush-anime.gif",
    "https://c.tenor.com/u1H1QTx8sxIAAAAC/anime-in-love.gif",
    "https://c.tenor.com/RzmW-BtosV4AAAAS/show-by-rock-cyan-hijirikawa.gif",
    "https://c.tenor.com/xc7x66o3rPUAAAAS/anime-love-anime.gif"
]
roast = [
    "hahaha",
    "If your brain was dynamite, there wouldn’t be enough to blow your hat off",
    " You are more disappointing than an unsalted pretzel."
    " Light travels faster than sound, which is why you seemed bright until you spoke.",
    " We were happily married for one month, but unfortunately, we’ve been married for 10 years.",
    "Your kid is so annoying he makes his Happy Meal cry.",
    "You have so many gaps in your teeth it looks like your tongue is in jail.",
    "Your secrets are always safe with me. I never even listen when you tell me them.",
    "I’ll never forget the first time we met. But I’ll keep trying.",
    "I forgot the world revolves around you. My apologies! How silly of me.",
    "I only take you everywhere I go just so I don’t have to kiss you goodbye.",
    " Hold still. I’m trying to imagine you with a personality.",
    "Our kid must have gotten his brain from you! I still have mine.",
    "Your face makes onions cry.",
]
hug_gifs=[
    "https://c.tenor.com/5tkkWFegYvUAAAAd/hug-couple.gif",
    
    "https://c.tenor.com/MBWZf-CK98gAAAAj/hug-love.gif",
]
kiss_gifs=[
    "https://tenor.com/view/love-wife-husband-yes-kiss-gif-17770873",
    "https://c.tenor.com/M0dI1g4vdr0AAAAj/love-wife.gif",
    "https://c.tenor.com/YAVvwR_va6MAAAAj/kiss-love.gif",
    "https://c.tenor.com/cZ4AykKErIYAAAAj/hugs-love.gif",
    "https://c.tenor.com/fU2-2CgMonsAAAAj/kiss-dinner.gif"
    "https://c.tenor.com/XMsFBHyi2WAAAAAd/love-you-my-princess-kiss-on-forehead.gif"
 ]
class Action(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.senpai_id = 888414036662833164
 
    @commands.command()
    async def action(self, ctx):
        async with ctx.channel.typing():

            actionemb = discord.Embed(
            title="ACTIONS",
            description="**AVAILABLE ACTIONS**\n`hug   ` `kiss  `, `kill  `, `punch  `, `highfive  ` , `slap  `, `poke  `, `roast `,`smirk ` ",
            color=0x2e69f2
            )


  
    @commands.command()
    async def dadjoke(self, ctx):
        dadjoke = [
            "I'm afraid for the calendar. Its days are numbered.",
            "My wife said I should do lunges to stay in shape. That would be a big step forward.",
            "Why do fathers take an extra pair of socks when they go golfing?",
            "In case they get a hole in one!",
            "Singing in the shower is fun until you get soap in your mouth. Then it's a soap opera.",
            "What do a tick and the Eiffel Tower have in common?",
            "They're both Paris sites.",
            "What do you call a fish wearing a bowtie?", "Sofishticated.",
            "How do you follow Will Smith in the snow?",
            "You follow the fresh prints.",
            "If April showers bring May flowers, what do May flowers bring?"
            "Pilgrims.",
            "I thought the dryer was shrinking my clothes. Turns out it was the refrigerator all along.",
            "What do you call a factory that makes okay products?"
            "A satisfactory.",
            "Dear Math, grow up and solve your own problems.",
            "What did the janitor say when he jumped out of the closet?"
            "Supplies!",
            "Have you heard about the chocolate record player? It sounds pretty sweet.",
            "What did the ocean say to the beach?"
            "Nothing, it just waved.", "Why do seagulls fly over the ocean?"
            "Because if they flew over the bay, we'd call them bagels.",
            "I only know 25 letters of the alphabet. I don't know y.",
            "How does the moon cut his hair?"
            "Eclipse it.", "What did one wall say to the other?"
            "I'll meet you at the corner.",
            "What did the zero say to the eight?"
            "That belt looks good on you.",
            "A skeleton walks into a bar and says, 'Hey, bartender. I'll have one beer and a mop.'",
            "Where do fruits go on vacation?"
            "Pear-is!",
            "I asked my dog what's two minus two. He said nothing.",
            "What did Baby Corn say to Mama Corn?"
            "Where's Pop Corn?", "What's the best thing about Switzerland?"
            "I don't know, but the flag is a big plus.",
            "What does a sprinter eat before a race?"
            "Nothing, they fast!", "Where do you learn to make a banana split?"
            "Sundae school.", "What has more letters than the alphabet?"
            "The post office!", "Dad, did you get a haircut?"
            "No, I got them all cut!", "What do you call a poor Santa Claus?"
            "St. Nickel-less.",
            "I got carded at a liquor store, and my Blockbuster card accidentally fell out. The cashier said never mind.",
            "Where do boats go when they're sick?"
            "To the boat doc.",
            "I don't trust those trees. They seem kind of shady.",
            "My wife is really mad at the fact that I have no sense of direction. So I packed up my stuff and right!",
            "How do you get a squirrel to like you? Act like a nut.",
            "Why don't eggs tell jokes? They'd crack each other up.",
            "I don't trust stairs. They're always up to something.",
            "What do you call someone with no body and no nose? Nobody knows.",
            "Did you hear the rumor about butter? Well, I'm not going to spread it!",
            "Why couldn't the bicycle stand up by itself? It was two tired.",
            "What did one hat say to the other?"
            "Stay here! I'm going on ahead.",
            "Why did Billy get fired from the banana factory? He kept throwing away the bent ones.",
            "Dad, can you put my shoes on?"
            "No, I don't think they'll fit me."
            "Why can't a nose be 12 inches long? Because then it would be a foot.",
            "What does a lemon say when it answers the phone?"
            "Yellow!",
            "This graveyard looks overcrowded. People must be dying to get in.",
            "What kind of car does an egg drive?"
            "A yolkswagen.", "Dad, can you put the cat out?"
            "I didn't know it was on fire.", "How do you make 7 even?"
            "Take away the s.", "How does a taco say grace?"
            "Lettuce pray.",
            "What time did the man go to the dentist? Tooth hurt-y.",
            "Why didn't the skeleton climb the mountain?"
            "It didn't have the guts.",
            "What do you call it when a snowman throws a tantrum?"
            "A meltdown.",
            "How many tickles does it take to make an octopus laugh? Ten tickles.",
            "I have a joke about chemistry, but I don't think it will get a reaction.",
            "What concert costs just 45 cents? 50 Cent featuring Nickelback!",
            "What does a bee use to brush its hair?"
            "A honeycomb!",
            "How do you make a tissue dance? You put a little boogie in it.",
            "Why did the math book look so sad? Because of all of its problems!",
            "What do you call cheese that isn't yours? Nacho cheese.",
            "My dad told me a joke about boxing. I guess I missed the punch line.",
            "What kind of shoes do ninjas wear? \nSneakers!",
            "How does a penguin build its house? \nIgloos it together.",
            "How did Harry Potter get down the hill?"
            "\nWalking. JK! Rowling.",
            "I used to be addicted to soap, but \nI'm clean now.",
            "A guy walks into a bar...and he was disqualified from the limbo contest.",
            "You think swimming with sharks is expensive? \nSwimming with sharks cost me an arm and a leg.",
            "When two vegans get in an argument, \nis it still called a beef?",
            "I ordered a chicken and an egg from Amazon.\n I'll let you know...",
            "Do you wanna box for your leftovers?"
            "\nNo, but I'll wrestle you for them.",
            "That car looks nice but the muffler seems exhausted.",
            "Shout out to my fingers. \nI can count on all of them.",
            "If a child refuses to nap, \nare they guilty of resisting a rest?",
            "What country's capital is growing the fastest?"
            "Ireland. \nEvery day it's Dublin.",
            "I once had a dream I was floating in an ocean of orange soda.\n It was more of a fanta sea.",
            "Did you know corduroy pillows are in style? \nThey're making headlines.",
            "Did you hear about the kidnapping at school?\n It's okay, he woke up.",
            "A cheeseburger walks into a bar. The bartender says, \n'Sorry, we don't serve food here.'",
            "I once got fired from a canned juice company.\n Apparently I couldn't concentrate.",
            "I used to play piano by ear. \nNow I use my hands.",
            "Have you ever tried to catch a fog? \nI tried yesterday but I mist.",
            "I'm on a seafood diet. \nI see food and I eat it.",
            "Why did the scarecrow win an award?\n Because he was outstanding in his field.",
            "I made a pencil with two erasers. \nIt was pointless.",
            "How do you make a Kleenex dance? \nPut a little boogie in it!",
            "I'm reading a book about anti-gravity. \nIt's impossible to put down!",
            "Did you hear about the guy who invented the knock-knock joke?\n He won the 'no-bell' prize.",
            "I've got a great joke about construction,\n but I'm still working on it.",
            "I used to hate facial hair...\nbut then it grew on me.",
            "I decided to sell my vacuum cleaner—it was just gathering dust!",
            "I had a neck brace fitted years ago and I've never looked back since.",
            "You know, people say they pick their nose,\n but I feel like I was just born with mine.",
            "What's brown and sticky?\n A stick.",
            "Why can't you hear a psychiatrist using the bathroom? \nBecause the 'P' is silent.",
            "What do you call an elephant that doesn't matter? \nAn irrelephant.",
            "What do you get from a pampered cow?\n Spoiled milk.",
            "I like telling Dad jokes. \nSometimes he laughs!",
            "What's the best smelling insect?"
            "\nA deodor-ant.",
            "I used to be a personal trainer. \nThen I gave my too weak notice.",
            "Did I tell you the time I fell in love during a backflip? I was heels over head!",
            "If a child refuses to sleep during nap time, \nare they guilty of resisting a rest?",
            "I ordered a chicken and an egg online. \nI’ll let you know.",
            "It takes guts to be an organ donor.",
            "If you see a crime at an Apple Store, \ndoes that make you an iWitness?",
            "I'm so good at sleeping,\n I can do it with my eyes closed!",
            "I was going to tell a time-traveling joke, \nbut you guys didn't like it.",
            "What do you call a fake noodle?"
            "\nAn impasta.", "What do you call a belt made of watches?"
            "\nA waist of time.",
            "What happens when a strawberry gets run over crossing the street?"
            "\nTraffic jam.",
            "What do you call two monkeys that share an Amazon account?\nPrime mates.",
            "What do you call a pony with a sore throat?\nA little hoarse.",
            "Where do math teachers go on vacation? \nTimes Square.",
            "Whenever I try to eat healthy, a chocolate bar looks at me and Snickers.",
            "What does garlic do when it gets hot?"
            "\nIt takes its cloves off.",
            "What's a robot's favorite snack? \nComputer chips.",
            "How much does it cost Santa to park his sleigh?"
            "Nothing, it's on the house.",
            "Mountains aren't just funny. \nThey're hill areas.",
            "Why did the orange lose the race? \nIt ran out of juice.",
            "How you fix a broken pumpkin?\n With a pumpkin patch."
            "Why are fish so smart?\n They live in schools!"
            "What's the best thing about Switzerland?\n I don't know, but the flag is a big plus."
            "Why did the man fall down the well?\n Because he couldn’t see that well!"
            "Why do peppers make such good archers?\n Because they habanero."
            "What did the sink tell the toilet?\n You look flushed!"
            "Where do boats go when they're sick?\n To the dock."
            "What has ears but cannot hear? \nA cornfield!"
            "Stop looking for the perfect match; \nuse a lighter."
            "Can February March? \nNo, but April May!"
            "Why was 6 afraid of 7?\n Because 7 ate nine!"
            "I'm so good at sleeping that I do it with my eyes closed."
            "Try the seafood diet—you see food, \nthen you eat it."
            "What do you call a pencil with two erasers?\n Pointless."
            "Did you hear the one about the roof?\n Never mind, it's over your head."
            "What's brown and sticky?\n A stick."
            "I hated facial hair but then it grew on me."
            "It really takes guts to be an organ donor."
            "Did you hear the rumor about butter? Well, \nI'm not going to go spreading it!"
            "What did the plumber say to the singer? \nNice pipes."
            "I was going to tell a time-traveling joke, \nbut you didn't like it."
            "How do you deal with a fear of speed bumps?\n You slowly get over it."
            "I ordered a chicken and an egg online.\n I'll let you know."
            "I'm reading an anti-gravity book. \nI can't put it down!"
            "I'd avoid the sushi if I were you. \nIt's a little fishy!"
            "What state is known for its small drinks?\n Minnesota."
            "What's Forrest Gump's password?\n 1forrest1"
            "What do houses wear? \nAn address."
            "What did the two pieces of bread say on their wedding day?\n It was loaf at first sight."
            "What kind of shoes does a lazy person wear?\n Loafers."
            "What did the ocean say to the beach? \n Nothing, it just waved."
            "What happens when a snowman throws a tantrum? \n He has a meltdown."
        ]

        async with ctx.channel.typing():
            embed = discord.Embed(title="**JOKE  :  **",
                                  description=random.choice(dadjoke),
                                  color=discord.Colour.red())
            await ctx.send(embed=embed)

    @commands.command()
    async def roast(self, ctx, member: discord.Member):
        await ctx.send(f"{member.mention}\n{random.choice(roast)}")

    @commands.command()
    async def simp(self, ctx, mem: discord.Member = None):
        if mem == None:
            mem = ctx.author
        emb = discord.Embed(
            titile="",
            description=f"{ctx.author.mention} simps on {mem.mention} <3\n\n*",
            color=0x2e69f2)
        emb.set_image(url=f"{random.choice(simp_gifs)}")
        await ctx.send(embed=emb)


    @commands.command()
    async def hug(self, ctx, mem: discord.Member = None):
        if mem == None:
            mem = ctx.author
        emb = discord.Embed(
            titile="",
            description=f"{ctx.author.mention} hugged {mem.mention} <3\n\n*",
            color=0x2e69f2)
        emb.set_image(url=f"{random.choice(hug_gifs)}")
        await ctx.send(embed=emb)
    @commands.command()
    async def kiss(self, ctx, mem: discord.Member = None):
        if mem == None:
            mem = ctx.author
        emb = discord.Embed(
            titile="",
            description=f"{ctx.author.mention} kissed {mem.mention} <3\n\n*",
            color=0x2e69f2)
        emb.set_image(url=f"{random.choice(kiss_gifs)}")
        await ctx.send(embed=emb)

    @commands.command()
    async def poke(self, ctx, mem: discord.Member = None):
        if mem == None:
            mem = ctx.author
        emb = discord.Embed(
            titile="",
            description=f"{ctx.author.mention} poked {mem.mention} <3\n\n*",
            color=0x2e69f2)
        emb.set_image(url=f"{random.choice(poke_gifs)}")
        await ctx.send(embed=emb)

        
    @commands.command()
    async def highfive(self, ctx, mem: discord.Member = None):
        if mem == None:
            mem = ctx.author
        emb = discord.Embed(
            titile="",
            description=f"{ctx.author.mention} highfive {mem.mention} <3\n\n*",
            color=0x2e69f2)
        emb.set_image(url=f"{random.choice(highfive_gifs)}")
        await ctx.send(embed=emb)

    @commands.command()
    async def punch(self, ctx, mem: discord.Member = None):
        if mem == None:
            mem = ctx.author
        emb = discord.Embed(
            titile="",
            description=f"{ctx.author.mention} Punched {mem.mention} <3\n\n*",
            color=0x2e69f2)
        emb.set_image(url=f"{random.choice(punch_gifs)}")
        await ctx.send(embed=emb)


    @commands.command()
    async def slap(self, ctx, mem: discord.Member = None):
        if mem == None:
            mem = ctx.author
        emb = discord.Embed(
            titile="",
            description=f"{ctx.author.mention} Slaped {mem.mention} <3\n\n*",
            color=0x2e69f2)
        emb.set_image(url=f"{random.choice(slap_gifs)}")
        await ctx.send(embed=emb)

    @commands.command()
    async def smirk(self, ctx, mem: discord.Member = None):
        if mem == None:
            mem = ctx.author
        emb = discord.Embed(
            titile="",
            description=f"{ctx.author.mention} smirked {mem.mention} <3\n\n*",
            color=0x2e69f2)
        emb.set_image(url=f"{random.choice(smirk_gifs)}")
        await ctx.send(embed=emb)



    
    
    

def setup(client):
    client.add_cog(Action(client))
    print(">>> action load ho gaya !!!!!!!!!")


#`pat`,  `cuddle`, `kiss`, `bonk`, `kill`, `punch`, `handhold`, `highfive`, `feed`, `nom`, `slap`, `pout`, `smug`, `tickle`, `poke`, `blush`