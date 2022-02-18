import discord
from discord import colour
from discord.ext import commands
import requests
import requests

url = "https://sameer-kumar-aztro-v1.p.rapidapi.com/"
headers = {
    'x-rapidapi-host': "sameer-kumar-aztro-v1.p.rapidapi.com",
    'x-rapidapi-key': "52c4165dc4msh25ad16f273bccb8p1c3002jsnb6f45071252d"
    }


class horoscope(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.senpai_id = 888414036662833164

    @commands.command()
    async def horoscope(self, ctx,msg):
        if msg == None:
            await ctx.reply("SIGN IS REQUIRED IN FORM OF STRING \n List of possible values of \"sign\":Aries\nTaurus\nGemini\nCancer\nLeo\nVirgo\nLibra\nScorpio\nSagittarius\nCapricorn\nAquarius\nPisces")
        querystring = {"sign":f"{msg}","day":"today"}
        response = requests.request("POST", url, headers=headers, params=querystring).json()


        date_range=response['date_range']
        current_date=response['current_date']
        description=response['description']
        compatibility=response['compatibility']
        mood=response['mood']
        color=response['color']
        lucky_number=response['lucky_number']
        lucky_time=response['lucky_number']

        embed=discord.Embed(title="Horoscope", description=f"Todays horoscope for {msg}")
        embed.add_field(name="Sign", value=f"{msg}",inline=True)
        embed.add_field(name="Date Range", value=f"{date_range}")
        embed.add_field(name="current_date", value=f"{current_date}")
        embed.add_field(name="😀", value=f"{description}")
        embed.add_field(name="Compatibility", value=(f"{compatibility}॰C"))
        embed.add_field(name="Mood", value=f"{mood}")
        embed.add_field(name="Color", value=f"{color}")
        embed.add_field(name="lucky_number", value=(f"{lucky_number}"))
        embed.add_field(name="lucky_time", value=f"{lucky_time}")

        await ctx.send(embed=embed)
    


def setup(client):
    client.add_cog(horoscope(client))
    print(">>> horoscope load ho gaya !!!!!!!!!")

# sign
# STRING
# aquarius
# REQUIRED
# List of possible values of \"sign\":

# Aries
# Taurus
# Gemini
# Cancer
# Leo
# Virgo
# Libra
# Scorpio
# Sagittarius
# Capricorn
# Aquarius
# Pisces
# day
# STRING
# today
# REQUIRED
# Possible values for \"day\":

# today
# yesterday
# tomorrow
