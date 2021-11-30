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

import requests



headers = {
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com",
    'x-rapidapi-key': "52c4165dc4msh25ad16f273bccb8p1c3002jsnb6f45071252d"
    }

class coviddata(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.senpai_id = 888414036662833164

    @commands.command()
    async def covidall(self, ctx):
        url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/"
        response = requests.request("GET", url, headers=headers)
        await ctx.send(response.text)
    @commands.command()
    async def countryiso(self, ctx):
        url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/countries-name-ordered"
        response = requests.request("GET", url, headers=headers)
        await ctx.send(response.text)
    @commands.command()
    async def covidindia(self, ctx):
        url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/countries"
        response = requests.request("GET", url, headers=headers)
        await ctx.send(response.text)
    @commands.command()
    async def covidc(self, ctx, msg ,iso ):
        url =f"https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/country-report-iso-based/{msg}/{iso}"
        response = requests.request("GET", url, headers=headers)
        await ctx.send(response.text)
    @commands.command()
    async def covids(self, ctx):
        url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/api-covid-data/reports/ind"
        response = requests.request("GET", url, headers=headers)
        await ctx.send(response.text)


def setup(client):
    client.add_cog(coviddata(client))
    print("covid data loaded")