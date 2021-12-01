import discord
from discord import client
from discord.ext import commands
import requests
import requests

url = "https://acobot-brainshop-ai-v1.p.rapidapi.com/get"
headers = {
    'x-rapidapi-host': "acobot-brainshop-ai-v1.p.rapidapi.com",
    'x-rapidapi-key': "52c4165dc4msh25ad16f273bccb8p1c3002jsnb6f45071252d"
    }
class chatty(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.senpai_id = 888414036662833164

    @commands.Cog.listener()
    async def on_message(self , msg,):
            if msg.author == client.User:
                return
            else:
                querystring = {"bid":"178","key":"sX5A2PcYZbsN5EY6","uid":"mashape","msg":f"{msg}"}
                response = requests.request("GET", url, headers=headers, params=querystring)
                res=response.json()
                
                await msg.reply(res["cnt"])




def setup(client):
    client.add_cog(chatty(client))
    print(">>> chat bot load ho gaya !!!!!!!!!")