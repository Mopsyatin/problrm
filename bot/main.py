from flask import Flask, render_template, request, redirect
import discord
from discord.ext import commands
from time import *
import random
import time
import requests
from flask_sqlalchemy import SQLAlchemy

####################################################################################################

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app )

####################################################################################################

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable =False)
    picture = db.Column(db.String(100), nullable =False)
    points = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f'<User {self.name}>'
    
####################################################################################################

black_list = []

####################################################################################################

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


####################################################################################################

@bot.command()
async def add(ctx, plant: str ="tree", user: discord.Member = None):
    if user == None:
        user = ctx.author
    names = user.name
    if names in black_list:
        await ctx.channel.send("you are on the black list, if you do not agree with this decision, then write to the [e-mail]")
    else:

        if plant == "tree":
            point = 8

        elif plant == "bush":
            point = 5

        elif plant == "cactus":                   
            point = 3
            
        elif plant == "algae":
            point = 3

        elif plant == "flower":
            point = 3

        
        
        with app.app_context():

            missing = User.query.filter_by(name = names).first()
            if   missing == None: 
                user = User(name= names, picture= user.avatar.url, points= point)
                db.session.add(user)
                db.session.commit()
                await ctx.channel.send("All okay")
            else:
                us = User.query.filter_by(name = names).first()
                point += us.points
                updated = User.query.filter_by(name = names).update(dict(points = point ))
                db.session.commit()
                await ctx.channel.send("All okay")
                

                

            
                
                
            
        

        
    
    



   

    
  






















####################################################################################################
@bot.command()
async def plant(ctx):
    await ctx.channel.send("select your action", view = plant())

####################################################################################################

bot.run("MTExMjgyNzA3ODA3Nzg0OTYwMA.GyeDu9.zJYYTbnWCuNSLQZkgG5KF5jG73rtK8mn171Q4A")