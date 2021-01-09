import discord
from keep_alive import keep_alive
import os
import random

#Tutorial used: https://www.youtube.com/watch?v=SPTfmiYiuok
client = discord.Client()
TOKEN = os.getenv('TOKEN')

hotMessages = ["That's hot!",
  "That's HOT brudda!!",
  "Yes, very very hot!",
  "🔥🔥🔥"]
jesusMessages = ["You need JESUS!",
  "You need JESUS. I have his phone number. It's 911",
  "You need JESUS. Let me call Jesus for you.",
  "You need Jesus, friend."]
sudoku = ""

def botCalled(message):
  """Takes the message and returns whether or not the bot was requested/referenced"""
  if client.user in message.mentions:
    return True
  
  if message.content.startswith("!benson"):
    return True
  
  return False

#def botCommands(message):


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
  #Do not reply to bot's own messages
  if message.author == client.user:
    return


  #Bot commands
  if botCalled(message):
    await message.channel.send("You called baby-girl? 😉")
  


  #Bot Replies
  #Message contains a variant of "hot"
  hots = ["hot", "Hot", "HOT", "hawt", "H O T"]
  # List Comprehension Help: https://stackoverflow.com/questions/19211828/using-any-and-all-to-check-if-a-list-contains-one-set-of-values-or-another
  if any((x in message.content) for x in hots):
    await message.channel.send(random.choice(hotMessages))


  # 1/100 chance of just saying any stupid message
  if random.randint(0, 100) == 69:
    print("ding ding random message time!!")
    allMessages = hotMessages + jesusMessages
    await message.channel.send(random.choice(allMessages))
  #print(message.mentions)
  #print(message.content)

keep_alive()  #call the webserver
client.run(TOKEN)