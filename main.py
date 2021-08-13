import os
import discord
import csv
import random
import requests
import json
from keep_alive import keep_alive
from discord_webhook import DiscordWebhook, DiscordEmbed
#from discord.ext import commands
#from discord.ext import commands
#import randomstuff
#from googleapiclient.discovery import build

#myapiyou2 = os.environ['api_youtube_key']

#youtube= build('youtube', 'v3' ,developerKey=myapiyou2 )

#request = youtube.chennals().list(
  #part='statistics',
  #forUsername='Tausif al mukit Nafim'

#)
#response = request.execute()

#print(response)


#my_api = os.environ['apikey']

#with randomstuff.Client(api_key=my_api) as client:
  #joke = client.get_joke(type="any")

  #print("Category: ", joke.category) 
  #print("Joke Type: ", joke.type)
  #print("Joke: ", joke.joke) 
  #print("ID: ", joke.id) 
  #print("Safe: ", joke.safe)

  #print("Language: ", joke.lang) 

  #print("\n=== Flags ===\n")
  #print("NSFW: ", joke.flags.nsfw) 
  #print("Religious: ", joke.flags.religious)
  #print("Political: ", joke.flags.political) 
  #print("Racist: ", joke.flags.racist) 
  #print("Sexist: ", joke.flags.sexist)
  #print("Explicit: ", joke.flags.explicit) 




content= "hey guys as8 org have a new video on YouTube, check it out!!:sunglasses: @everyone"

webhook=DiscordWebhook(url="https://discord.com/api/webhooks/874106630252425306/NPvkPWunBq0LM-Xs70ARQfd4FTAnhi3C9OQxNOeTGrhms-soZRZxVs25LcLmUB-ot1wR" , content=content)

embed= DiscordEmbed(title="**Everything you need to know about The AS8 Organization (সবকিছু যা আপনার জানা দরকার)**",color=242424)

embed.set_author(name="The AS8 Organization", url="https://www.youtube.com/channel/UCjcS_VOSsg3ju2rwKZVNUnQ",icon_url="https://yt3.ggpht.com/ytc/AKedOLQ_Ty6OkI-_Dr9U4ZSDBK21dNX6MYkHa0550IrX=s88-c-k-c0x00ffffff-no-rj")

#embed.set_author(url="https://www.youtube.com/watch?v=bCTdPQUXGrU")

embed.set_footer(text="Plz share, comment and subscribe to support us")
embed.set_timestamp()
embed.add_embed_field(name="Description", value="There are available programming resources on the internet. But it is difficult to get the right guidance or mentorship.Again, most school-college students of Bangladesh are wasting their time on social media. They are not maintaining their extracurricular activities. Some of them are fascinated by programming but don't know where to start.In other countries, this is not a major problem because there are available developer communities that support new programmers at an extensive level. But in BD, there is a lack of actual developer communities.Yes, there are a few. But most of the time they are limited to a specific group of students.")
embed.add_embed_field(name="Viwes", value="90+")
embed.set_image(url="https://studio.youtube.com/channel/UCtmPcXJBdA26swynHhs8nMg/editing/images")
embed.set_thumbnail(url="https://www.youtube.com/embed/bCTdPQUXGrU")

#webhook.add_embed(embed)
#response= webhook.execute()



phrases = []
with open("phrases.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        phrases.append(row[1])


home="https://the-as8-organization.github.io/"
fb="https://www.facebook.com/as8org/"
git="https://github.com/The-AS8-organization"
youtube="https://www.youtube.com/channel/UCjcS_VOSsg3ju2rwKZVNUnQ"
insta="https://www.instagram.com/as8org/"
linkedin="https://www.linkedin.com/company/the-as8-organization/"



sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing","lost","failed"]

credit_words = ["I am made with dis.py by MD TAUSIF AL MUKIT.", "I have only one owner, MD TAUSIF AL MUKIT."]

starter_encouragements = [
  "Cheer up!:fire:",
  "Hang in there.:zap:",
  "You are a great person!:fire:",
  "Dont worry!:relaxed:",
  "Nothing to Worry!:relaxed:",
  "Calm down!:innocent:"
]

bot_hello_message= [
  ":grin:Hello there!",
  "Hi, I am Spurbot from .02.06.79 server.:sunglasses:",
  "Whats up!:metal:",
  "Hlw!:robot:",
]

user_message= [
  "Hello everyone",
  "Hi,everyone",
  "Hi,everybody",
  "Hello everybody",
  "Hlw,Spur"
]

def get_quote():
  response1 = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response1.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)
  

client = discord.Client()

@client.event
async def on_ready():
    print(f"{client.user} logged in now!")

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("*greet"):
      await message.channel.send(f":grin:Hello! How are you {message.author}")
      
  elif "*thought" in message.content:
      response = phrases[random.randint(0, len(phrases) - 1)]
      await message.channel.send(response)

  if message.content.startswith("*update_youtube"):
    webhook.add_embed(embed)
    response= webhook.execute()
    

  if message.content.startswith("*org_allinfo"):
    await message.channel.send(f"Hello! {message.author}\n Home_page=https://the-as8-organization.github.io/ \n Fb_page=https://www.facebook.com/as8org/ \n Dis=https://discord.com/invite/4aSj56xRwc \n YouTube=https://www.youtube.com/channel/UCjcS_VOSsg3ju2rwKZVNUnQ \n Linkedin=https://www.linkedin.com/company/the-as8-organization/ \n Git=https://github.com/The-AS8-organization \n insta=https://www.instagram.com/as8org/")
      
  
  if message.content.startswith("*help"):
    await message.channel.send("What do u wanna know about this org?\n if needed, type=> *org>home/fb/youtube/git/insta\n or to exit type=> *none")
  elif message.content.startswith("*org>home"):
      await message.channel.send(home)
  elif ("*org>fb") in message.content:
      await message.channel.send(fb)
  elif ("*org>git") in message.content:
      await message.channel.send(git)
  elif ("*org>youtube") in message.content:
      await message.channel.send(youtube)
  elif ("*org>insta") in message.content:
      await message.channel.send(insta)
  elif ("*org>linkedin") in message.content:
      await message.channel.send(linkedin)
  elif ("*none") in message.content:
      await message.channel.send("Ow, waiting for ur next command") 
    #break: 
  #else:
    #await message.channel.send("Sry, no info or key error")
  #else: 
    #await message.channel.send("Sry key error! or traceback error....")

  if message.content.startswith("*org_about"):
    await message.channel.send("something")              
    
  if message.content.startswith('*spur'):
    quote = get_quote()
    await message.channel.send(quote)
    
  if any (word in message.content for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))

  if any (line in message.content for line in user_message):
    await message.channel.send(random.choice(bot_hello_message))  

  if message.content.startswith("*credits"):
      await message.channel.send(random.choice(credit_words))

  if message.content.startswith("*commands"):
      await message.channel.send(":point_down:\n *greet\n *help\n *spur\n *thought\n *commands\n *org_allinfo\n *credits\n *Thnx")

  if message.content.startswith("*Thnx"):
      await message.channel.send("You ar most welcome :+1:") 

#bot = commands.Bot(command_prefix ="?")
#async def get_prefix(bot, message):
#async def get_prefix(bot, message):
#async def hello(ctx):
      


keep_alive()
my_secret = os.environ['TOKEN']
client.run(os.environ['TOKEN'])

    
