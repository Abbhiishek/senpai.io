import discord
from discord import embeds
from discord.ext import commands
import random
from decouple import config
import weeby

token = config('token')
my_weeby = weeby.Weeby(token)
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
            await ctx.send(embed=actionemb)


  
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
    async def roast(self, ctx, mem: discord.Member = None):
        if mem == None:
            mem = ctx.author
        emb = discord.Embed(
            titile="",
            description=f"{ctx.author.mention} Roasted {mem.mention} <G\n\n*",
            color=0x2e69f2)
        emb.set_image(url = my_weeby.get_gif().gif(type="roast"))
        await ctx.send(embed=emb)
    @commands.command()
    async def wave(self, ctx, mem: discord.Member = None):
        if mem == None:
            mem = ctx.author
        emb = discord.Embed(
            titile="",
            description=f"{ctx.author.mention} waved {mem.mention} <G\n\n*",
            color=0x2e69f2)
        emb.set_image(url = my_weeby.get_gif().gif(type="wave"))
        await ctx.send(embed=emb)
    @commands.command()
    async def bore(self, ctx):
        
        emb = discord.Embed(
            titile="",
            description=f"{ctx.author.mention} is bored !",
            color=0x2e69f2)

        emb.set_image(url = my_weeby.get_gif().gif(type="bored"))

        await ctx.send(embed=emb)
    @commands.command()
    async def angry(self, ctx, mem: discord.Member = None):
        if mem == None:
            mem = ctx.author
        
            emb = discord.Embed(
                titile="",
                description=f"{ctx.author.mention} is angry !",
                color=0x2e69f2)
            emb.set_image(url = my_weeby.get_gif().gif(type="angry"))
            await ctx.send(embed=emb)
        else:
            emb = discord.Embed(
                titile="",
                description=f"{ctx.author.mention} is angry! with {mem.mention}",
                color=0x2e69f2)
            emb.set_image(url = my_weeby.get_gif().gif(type="angry"))
            await ctx.send(embed=emb)

    @commands.command()
    async def confused(self, ctx):
        
        emb = discord.Embed(
            titile="",
            description=f"{ctx.author.mention} is confused !",
            color=0x2e69f2)
        emb.set_image(url = my_weeby.get_gif().gif(type="confused"))
        await ctx.send(embed=emb)

    @commands.command()
    async def simp(self, ctx, mem: discord.Member = None):
        if mem == None:
            mem = ctx.author
            emb = discord.Embed(
                    titile="",
                    description=f"{ctx.author.mention} simps on {mem.mention} <3",
                    color=0x2e69f2)
            emb.set_image(url = my_weeby.get_gif().gif(type="simp")) 
        else:
            emb = discord.Embed(
            titile="",
            description=f"{ctx.author.mention} simps <3",
            color=0x2e69f2)
            emb.set_image(url = my_weeby.get_gif().gif(type="simp"))
        await ctx.send(embed=emb)
    @commands.command()
    async def lyr(self, ctx):
        await ctx.send(my_weeby.get_json_response().lyrics(track="f{ctx}"))


    @commands.command()
    async def hug(self, ctx, mem: discord.Member = None):
        if mem == None:
            mem = ctx.author
            emb = discord.Embed(
                titile="",
                description=f"{ctx.author.mention} hugged someone unknown <3",
                color=0x2e69f2)
            emb.set_image(url = my_weeby.get_gif().gif(type="hug"))
        else:
            emb = discord.Embed(
                titile="",
                description=f"{ctx.author.mention} hugged {mem.mention} <3",
                color=0x2e69f2)
            emb.set_image(url = my_weeby.get_gif().gif(type="hug"))
        await ctx.send(embed=emb)
    @commands.command()
    async def kiss(self, ctx, mem: discord.Member = None):
        if mem == None:
            mem = ctx.author
            emb = discord.Embed(
                titile="",
                description=f"{ctx.author.mention} kissed someone in space <3",
                color=0x2e69f2)
            emb.set_image(url=my_weeby.get_gif().gif(type="kiss"))
        else:
            emb = discord.Embed(
            titile="",
            description=f"{ctx.author.mention} kissed {mem.mention} <3",
            color=0x2e69f2)
        emb.set_image(url=my_weeby.get_gif().gif(type="kiss"))
        await ctx.send(embed=emb)
    @commands.command()
    async def poke(self, ctx, mem: discord.Member = None):
        if mem == None:
            mem = ctx.author
        emb = discord.Embed(
            titile="",
            description=f"{ctx.author.mention} poked {mem.mention} <3\n\n*",
            color=0x2e69f2)
        emb.set_image(url=my_weeby.get_gif().gif(type="poke"))
        await ctx.send(embed=emb)

        
    @commands.command()
    async def highfive(self, ctx, mem: discord.Member = None):
        if mem == None:
            mem = ctx.author
        emb = discord.Embed(
            titile="",
            description=f"{ctx.author.mention} highfive {mem.mention} <3\n\n*",
            color=0x2e69f2)
        emb.set_image(url=my_weeby.get_gif().gif(type="highfive"))
        await ctx.send(embed=emb)

    @commands.command()
    async def punch(self, ctx, mem: discord.Member = None):
        if mem == None:
            mem = ctx.author
        emb = discord.Embed(
            titile="",
            description=f"{ctx.author.mention} Punched {mem.mention} <3\n\n*",
            color=0x2e69f2)
        emb.set_image(url=my_weeby.get_gif().gif(type="punch"))
        await ctx.send(embed=emb)


    @commands.command()
    async def slap(self, ctx, mem: discord.Member = None):
        if mem == None:
            mem = ctx.author
        emb = discord.Embed(
            titile="",
            description=f"{ctx.author.mention} Slaped {mem.mention} <3\n\n*",
            color=0x2e69f2)
        emb.set_image(url=my_weeby.get_gif().gif(type="slap"))
        await ctx.send(embed=emb)

    @commands.command()
    async def smirk(self, ctx, mem: discord.Member = None):
        if mem == None:
            mem = ctx.author
        emb = discord.Embed(
            titile="",
            description=f"{ctx.author.mention} smirked {mem.mention} <3\n\n*",
            color=0x2e69f2)
        emb.set_image(url=my_weeby.get_gif().gif(type="smirk"))
        await ctx.send(embed=emb)

    @commands.command()
    async def syri(self, ctx, mem: discord.Member = None):
        syri = ["लिख दूंगा शायरी मैं शेर सुनने के लिए देखो हस कर हाज़िर हूं मात खाने के लिए। \n सुना है के जुगनू मरते चांद के चेहरे पे तुम जरूरी हो मगर ये आजमाने के लिए ।",
        "जिसका नाम सुनते ही डर जाते हैं लोग उसी का दीदार पाने को घर जाते हैं लोग। \n यूं ही इश्क को बदनाम नहीं किया करते मोहब्बत में भी कितने सुधर जाते हैं लोग ।",
        "मै ग़ज़ल में हर अशार मलाल के रख दूंगा मेरी जान मुझे सीने से निकाल के रख दूंगा ।",
        "बदनसीब मेरा इश्क़, करार तक ना पहुंचा उसकी यारी नसीब हुई प्यार तक ना पहुंचा ।",
        "किसकी बातों का यकीन किया जाए कुछ लोग तो कास्मे तोड़ कर चले गए।",
        "चलती हवाओं का रुख मोड़ कर जाना खूब आता है तुमको दिल तोड़ कर जाना \n तुम रोज मिलो जान यह ख्वाहिश है मेरी बस हर बार एक निशानी छोड़कर जाना ।",
        "खामोशी का है समां यहां कोई अपना नही मेरे अपनों ने ये कहा यहां कोई अपना नही ।",
        "मैं उसके सारे जवाब रखता हूं वो हर पल सवालों की किताब रखती है वो कहती है कि भूल गई है मुझको मगर वो मेरे सांसो तक का हिसाब रखती है ।",
        "जब कोई नहीं साथ में भगवान काम आता है सच मानो तो रोटी, कपड़ा, मकान काम आता है नफ़रत को मिटाकर दोस्ती निभाते चली यारों क्योंकि मुसीबत में इंसान के इंसान काम आता है ।",
        "तेरे इश्क का पन्ना पढ़ते-पढ़ते मेरा science maths बर्बाद हुआ । हार गया जो मोहब्बत में शायर बन कर आबाद हुआ ।",
        "वह मुस्काती बहुत है मुझे सताती बहुत है शायर की महबूबा है ना इसलिए तो इतराती बहुत है।",
        "शायर हूं सो मुझपे आशिकी का इल्जाम है अब जो भी जैसा है ये बन्दा सरेआम है चाहे तुम बेशरम कह लो या बेहया मुझको फर्क नही पड़ता 'स्वराज' का नाम ही 'बदनाम' है ।",
        "आज अपनी कहानी तुमको बताते हैं यारों वह बेवफाई सीख के हम पर आजमाते हैं यारों । \nमसला यह कि मैं आशिक भी और शायर भी महफिल में दिल-ए-बात कहकर पछताते हैं यारों । \nक्या इश्क़ करेंगे आज कल के आशिक कल वादा करके आज भूल जाते हैं यारों । \nउसे देखकर लगा के चांद ज़मीं पे उतरा है उसे देखने ये जुगनू घर जाते हैं यारों ।",
        "एक तू नाचीज़ है जो जिंदगी से डर जाता है आशिक वो भी है जो सरहद पर मर जाता है।\nमजहब के खेल में इंसानियत मिटाने वालों\nकोई ऐसा खेल खेलो जिसमें सर जाता है।\nनए पंख मिले हैं मुझको औकात दिखाते हो परिंदा जब थकता है जमीन पर उतर जाता है।\nमैं तो उससे मिलने उसके शहर तक जा पहुंचा वो देखता भी नहीं और सामने से गुजर जाता है।\nबाप जब तक जवान हैं बच्चे साथ रहते हैं\nपेड़ जब बूढ़ा हो जाए हर पत्ता बिखर जाता है।\nशौक और जरूरत मैं कुछ तो यारी होगी कोई घूमने तो कोई कमाने शहर जाता है।",
        "तुम अंधेरे में सनम यूं ना बाहर जाया करी सब तुम्हें देखेंगे तुम चांद को ना जलाया करो ।\nतुम्हारी जुल्फें तेरे हुस्न को पर्दा करती हैं फुर्सत में हो तो इन्हें अपने चेहरे से हटाया करो ।",
        "मुझे तुमसे इश्क करना सिखा दो जाना मगर अपनी यादों से पीछा छुड़ा तो जाना\nकिताबों से ज्यादा मैंने तुझको याद किया सब भूल जाने का तरीका तुम बता दो जाना\nमेरे गुस्ताख दिल ने तेरी तस्वीर चुराई है अगर बुरा लगे तो मनचाही सजा तो जाना तेरे जाने के बाद ही आंसू नहीं रुकते\nअपनी आवाज में कहानी सुना दो जाना\nमैं तो शायरी में तेरा नाम छुपा लेता हूं अपना नाम तुम मेरी जुबान से मिटा दो जाना ।",
        ]
        if mem == None:
            mem = ctx.author
        emb = discord.Embed(
            title=" ",
            description=f"{ctx.author.mention} नेई अर्झ किया हां {mem.mention} को ।<3\n\n*",
            color=0x2e69f2)
        emb.add_field(name=" 😊 " , value=f"{random.choice(syri)}")
        emb.set_footer(text="©Manish_swaraj X senpai.io")
        emb.set_image(url=my_weeby.get_gif().gif(type="love"))
        await ctx.send(embed=emb)



    
    
    

def setup(client):
    client.add_cog(Action(client))
    print(">>> action load ho gaya !!!!!!!!!")


#`pat`,  `cuddle`, `kiss`, `bonk`, `kill`, `punch`, `handhold`, `highfive`, `feed`, `nom`, `slap`, `pout`, `smug`, `tickle`, `poke`, `blush`
