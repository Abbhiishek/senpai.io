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

url = "https://weatherapi-com.p.rapidapi.com/current.json"



headers = {
    'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
    'x-rapidapi-key': "52c4165dc4msh25ad16f273bccb8p1c3002jsnb6f45071252d"
    }


class weather(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.senpai_id = 888414036662833164

    @commands.command()
    async def weather(self, ctx , msg):
        
        querystring = {"q":f"{msg}"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        weathere=discord.Embed(
             title="Weather Informations ",
            description=f"Weather information for the {msg}",
            color=discord.Colour.random()
        )
        weathere.set_thumbnail(url= response.current.condition.icon)
        weathere.add_field(name="Location", value=response.location.name)
        weathere.add_field(name="Region", value=response.location.region)
        weathere.add_field(name="Country", value=response.location.country)
        weathere.add_field(name="Tempertaure", value=f"{response.current.temp_c}॰C")
        weathere.add_field(name="Condition", value=response.current.condition.text)
        weathere.add_field(name="Wind speed", value=f"{response.current.wind_kph}Kph")
        weathere.add_field(name="Wind Degree", value=f"{response.current.wind_degree} toward {response.current.vwind_dir}")
        weathere.add_field(name="Humidity", value=response.current.humidity)
        weathere.add_field(name="Feels ", value=response.current.feelslike_c)
        
        

        await ctx.send(embed=weathere)


def setup(client):
    client.add_cog(weather(client))
    print(">>> weather load ho gaya !!!!!!!!!")

# {2 items
# "location":{8 items
# "name":"Kolkata"
# "region":"West Bengal"
# "country":"India"
# "lat":22.57
# "lon":88.37
# "tz_id":"Asia/Kolkata"
# "localtime_epoch":1638330237
# "localtime":"2021-12-01 9:13"
# }
# "current":{23 items
# "last_updated_epoch":1638329400
# "last_updated":"2021-12-01 09:00"
# "temp_c":21
# "temp_f":69.8
# "is_day":1
# "condition":{...}3 items
# "wind_mph":6.9
# "wind_kph":11.2
# "wind_degree":350
# "wind_dir":"N"
# "pressure_mb":1016
# "pressure_in":30
# "precip_mm":0
# "precip_in":0
# "humidity":83
# "cloud":0
# "feelslike_c":21
# "feelslike_f":69.8
# "vis_km":2
# "vis_miles":1
# "uv":6
# "gust_mph":11.4
# "gust_kph":18.4
# }
# }