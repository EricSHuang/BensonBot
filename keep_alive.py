#"Fake" webserver to fool repl.it to continuously run the discord bot
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hello, this is the web server."

def run():
  app.run(host='0.0.0.0', port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()