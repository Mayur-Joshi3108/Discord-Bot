#importing discord.py library
import discord
from discord.ext.commands import Bot
from random import choice

bot = Bot("!") 

# client = discord.Client()

with open("compliments.txt" , "r") as file:
    complimentList = list(file)

def getCompliment():
    return choice(complimentList) 

@bot.event                   #Indicates that on_ready() comes under client event
async def on_ready():
    print("We have logged in")        

@bot.event
async def on_message(message):
    print(message.author, message.content, message.channel)
    if message.content[0] != '!' :
        if message.author != bot.user:
            await message.channel.send(message.content + " " + str(message.author)) #await is for the program to wait till the message.send is completed
    await bot.process_commands(message)


@bot.command(pass_context=True)
async def compliment(ctx, member:discord.Member):
    complimentToSend = getCompliment()
    complimentToSend += member.mention
    await ctx.send(complimentToSend)

#Running the bot
bot.run("NzYxODg2NTc2NzU3MTc4Mzc5.X3hIKw._l6WKrVOzE8GwoPPCmUbp0T16OM")