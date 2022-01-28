from contextvars import Context
from distutils import command
from email import message
from unicodedata import name
from urllib import response
import discord
import logging
from discord.ext import commands
from dotenv import load_dotenv
import os
import clima


load_dotenv() 

TOKEN = os.getenv('DISCORD_TOKEN')

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


bot = commands.Bot(command_prefix ='!')

@bot.command(name = 'suma')
async def sumar(ctx, num1,num2):
    response = int(num1 + num2)
    await ctx.send(response)

@bot.command(name = 'yo')
async def user(ctx):
    response = str(ctx.author.name)
    print(response)
    await ctx.send(response + ' XUPALO :D') 

@bot.command(name = 'temperatura')
async def user(ctx):
    response = clima.temperatura()
    response = str(response["main"]["temp"])
    print(response)
    user = str(ctx.author.name)
    RESPUESTA = user + ':  hacen  ' +response + "°G"
    await ctx.send(RESPUESTA) 




bot.run(TOKEN)