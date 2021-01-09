#Benson Discord Bot
#Last Editted: 2021-01-08
#Tutorial used: https://www.youtube.com/watch?v=SPTfmiYiuok
import discord
from keep_alive import keep_alive
from replit import db
import os
import random

client = discord.Client()
TOKEN = os.getenv('TOKEN')

#TODO: Move these messages into a separate file that init's them into the database 
helpMessage = ""
hotMessages = ["That's hot!",
  "That's HOT brudda!!",
  "Yes, very very hot!",
  "🔥🔥🔥",
  "Not hot at all friend.",
  "Not hot, very cold."]
jesusMessages = ["You need JESUS!",
  "You need JESUS. I have his phone number. It's 911",
  "You need JESUS. Let me call Jesus for you.",
  "You need Jesus, friend."]
mentionMessages = ["You called baby-girl? 😉",
  "Hello baby-girl",
  "Hi 👋",
  "What's up baby-girl?",
  "What's up?"]
sudokuMessages = ""

def add_msg_to_db(message):
  #Accepts commands in the form: !benson add key value
  msg = message.content.strip("!benson add ")
  msg = msg.split(' ', 1)
  key = msg[0]
  value = msg[1]

  if key in db.keys():
    key = db[key]
    key.append(value)
    db[key] = key
  else:
    raise KeyError("No matched key found in the database")



def botMentioned(message):
  if client.user in message.mentions:
    return True
  return False

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
  #Do not reply to bot's own messages
  if message.author == client.user:
    return

  #TODO:Top Lane Impact, Sudoku, deez nuts, man of culture commands and a help command

  #Bot commands
  hots = ["hot", "Hot", "HOT", "hawt", "H O T"]
  if message.content.startswith("!benson"):
    command = message.content.split("!benson ")
    if (len(command) == 1):
      await message.channel.send(random.choice(mentionMessages))
    else:
      command = command[1]
      if (command == "help"):
        #TODO
        await message.channel.send(helpMessage)
      elif (command == "hot"):
        await message.channel.send(random.choice(hotMessages))
      elif (command == "jesus"):
        await message.channel.send(random.choice(jesusMessages))
      else:
        await message.channel.send("Sorry friendo. That's not a valid command.\nType \"!benson help\" for a list of commands")

  #Bot Replies
  elif botMentioned(message) and any((x in message.content) for x in hots):
    #Message contains a variant of "hot"
    #List Comprehension Help: https://stackoverflow.com/questions/19211828/
    await message.channel.send(random.choice(hotMessages))

  #Bot Mentioned
  elif client.user in message.mentions:
    mentionMessages.append(f'Hi {message.author.name}! 👋')
    await message.channel.send(random.choice(mentionMessages))

  # 1/100 chance of just saying any random message
  else:
    if random.randint(0, 100) == 69:
      print("ding ding random message time!!")
      randomMessages = hotMessages + jesusMessages + sudokuMessages
      await message.channel.send(random.choice(randomMessages))
  #print(message.mentions)
  #print(message.content)

keep_alive()  #call the webserver
client.run(TOKEN)