import discord
from discord import colour
from discord import embeds
from discord import user
from discord import message
from discord.ext import commands
import os

class ERRORS(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.senpai_id = 888414036662833164


def setup(client):
    client.add_cog(ERRORS(client))
    print(">>> ERRORS  load ho gaya !!!!!!!!!")

