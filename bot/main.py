from BotLogic import sword
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import os
import discord
from discord.ext import commands
from time import *
import random
import time
import requests


again = False
# Переменная intents - хранит привилегии бота
intents = discord.Intents.all()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
bot = commands.Bot(command_prefix=':)', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def sword(ctx):
    for attachment in ctx.message.attachments:
        amogus = "./" + attachment.filename
        await attachment.save(amogus)
        await ctx.channel.send(sword(amogus))
        os.remove(amogus)

bot.run("MTExMjgyNzA3ODA3Nzg0OTYwMA.GOkiMw.5ib2jpTdU1K2w6MXMr7F3-sNC_q0hiR3LNmAS0")