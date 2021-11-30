import discord
from discord import embeds
from discord.ext import commands
import random
import json
import requests
from discord import utils
from discord.user import User
from random import choice
from decouple import config
import requests

headers = {
    'x-rapidapi-host': "yahoo-weather5.p.rapidapi.com",
    'x-rapidapi-key': "52c4165dc4msh25ad16f273bccb8p1c3002jsnb6f45071252d"
    }

class weather(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.senpai_id = 888414036662833164

    @commands.command()
    async def weather(self, ctx , msg):
        url = "https://yahoo-weather5.p.rapidapi.com/weather"

        querystring = {"location":f"{msg}","format":"json","u":"c"}
        response = requests.request("GET", url, headers=headers, params=querystring)

        await ctx.send(response.text)


def setup(client):
    client.add_cog(weather(client))
    print(">>> weather load ho gaya !!!!!!!!!")
