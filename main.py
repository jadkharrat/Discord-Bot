import discord
import os
import requests
import json
from keep_online import keep_online

my_secret = os.environ['TOKEN'] #save discord token 
client = discord.Client() #create a client to connect ot discord

def chuck_joke(): #function that returns jokes using API
  url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"

  headers = {
      'accept': "application/json",
      'x-rapidapi-host': "matchilling-chuck-norris-jokes-v1.p.rapidapi.com",
      'x-rapidapi-key': "7b4e645c77msh81ccc748c293f03p142097jsn5bfdb7460eb0"
      }
  
  response = requests.request("GET", url, headers=headers)
  json_data = json.loads(response.text)
  joke = json_data['value']
  return(joke)

def dad_joke(): #another function that returns jokes using different API
  url = "https://dad-jokes.p.rapidapi.com/random/joke"

  headers = {
      'x-rapidapi-host': "dad-jokes.p.rapidapi.com",
      'x-rapidapi-key': "7b4e645c77msh81ccc748c293f03p142097jsn5bfdb7460eb0"
      }
  
  response = requests.request("GET", url, headers=headers)
  json_data = json.loads(response.text)
  setup = json_data['body'][0]['setup']
  punchline = json_data['body'][0]['punchline']
  return(setup + " " + punchline)

def btc_price(): #function that returns Bitcoin price using Coinmarketcap API
  url = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"
  parameters = {'slug' : 'bitcoin', 'convert' : 'USD'}
  headers = {'X-CMC_PRO_API_KEY' : '90130b7e-8a50-4e47-8da5-ba1d5c056101', 'accept' : 'application/json'}
  response = requests.request("GET", url, params = parameters, headers = headers)
  json_data = json.loads(response.text)
  price = json_data['data']['1']['quote']['USD']['price']
  return("Bitcoin price: $" + str("{:.2f}".format(price)))
  
@client.event
async def on_ready(): #check if the bot works
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message): #check the messages and do the right task
    if message.author == client.user: #check if the message is from the bot and do nothing
        return
      
    if message.content == ".hi":
      await message.channel.send("Hello! " + str(message.author.mention) + " :relaxed:")
      
    if message.content.startswith('.chuck'):
        joke = chuck_joke()
        await message.channel.send(joke)

    if message.content.startswith('.joke'):
        joke1 = dad_joke()
        await message.channel.send(joke1)

    if message.content.startswith('.btc'):
        p = btc_price()
        await message.channel.send(p)

keep_online() #keep the bot online using uptimerobot
client.run(my_secret) #run the bot
