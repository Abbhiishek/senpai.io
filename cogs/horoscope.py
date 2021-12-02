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
        response = requests.request("POST", url, headers=headers, params=querystring)
        data=response.json()
        embed=discord.Embed(title="Horoscope", description=f"Todays horoscope for {msg}", colour=discord.colour.random())
        embed.add_field(name="Sign", value=f"{msg}",inline=True)
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