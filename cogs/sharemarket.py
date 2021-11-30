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


url = "https://zirra.p.rapidapi.com/v1/companies"

headers = {
    'x-rapidapi-host': "zirra.p.rapidapi.com",
    'x-rapidapi-key': "52c4165dc4msh25ad16f273bccb8p1c3002jsnb6f45071252d"
    }

response = requests.request("GET", url, headers=headers)


class sharemarket(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.senpai_id = 888414036662833164

    @commands.command()
    async def sharemarket(self, ctx):
        await ctx.send(response.text)


def setup(client):
    client.add_cog(sharemarket(client))
    print(">>> sharemarket load ho gaya !!!!!!!!!")
