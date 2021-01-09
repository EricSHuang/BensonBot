import discord
import os
import random

client = discord.Client()
TOKEN = os.getenv('TOKEN')

hot = ["That's hot!"]

def botCalled(message):
  """Takes the message and returns whether or not the bot was requested/referenced"""
  if client.user in message.mentions:
    return True
  
  if message.content.startswith("!benson"):
    return True
  
  return False

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  #Bot commands
  if botCalled(message):
    await message.channel.send("You called baby-girl? 😉")
  
  #Bot Replies
  hots = ["hot", "HOT", "hawt", "H O T"]
  if "hot" in message.content:

  # 1/100 chance of just saying any stupid message (Surprisingly realistic)
  if random.randint(0, 100) == 69:
    await message.channel.send("That's hot!")
  #print(message.mentions)
  #print(message.content)

  return

client.run(TOKEN)