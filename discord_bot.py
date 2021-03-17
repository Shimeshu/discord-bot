# bot.py
import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands
import pyjokes
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
    print(guild.members)

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    social = [	
    			"Whatsapp\nhttps://web.whatsapp.com/",
    			"Discord\nhttps://www.discord.com/channels/@me/",
    			"Facebook\nhttps://www.facebook.com/",
    			"Twitter\nhttps://www.twitter.com/",
    			"Wikipedia\nhttps://www.wikipedia.org/",
    			"Youtube\nhttps://www.youtube.com/",
    			"Vimeo\nhttps://www.vimeo.com/",
    			"Quora\nhttps://www.quora.com/",
    			"Instagram\nhttps://www.instagram.com/",
    			"Social Link Doesn't Exist"
    			]
    music = ["https://youtu.be/cykH36IbhUQ",
    		"https://youtu.be/zzwRbKI2pn4",
    		"https://youtu.be/T8qZ-t6c49w",
    		"https://youtu.be/0Cyvhz1GmRI",
    		"https://youtu.be/jEJI6Nf1aWU",
    		"https://youtu.be/7mFvyrNHZRY",
    		"https://youtu.be/PMCu0JtizCk",
    		"https://youtu.be/JHUrRSBtUNE",
    		"https://youtu.be/uJ6WU-u4i3w",
    		"https://youtu.be/hGf8rOwFzvo",
    		"https://youtu.be/icH1SyiTk94",
    		"https://youtu.be/icH1SyiTk94",
    		"https://youtu.be/GOkJguI8kYc",
    		"https://youtu.be/a3B2glol4IU",
    		"https://youtu.be/BiVyN2ftrrs",
    		"https://youtu.be/xutBFUf3LoU",
    		"https://youtu.be/YysFgoGIMkY",
    		"https://youtu.be/Ki4_Fc3XoSk",
    		"https://youtu.be/jDn2bn7_YSM",
    		"https://youtu.be/gdZLi9oWNZg"]
    
    cmds = {
    	"/j": pyjokes.get_joke(),
    	"/m": random.choice(music)
    }
    if message.content == "/j":
    	await message.channel.send(cmds["/j"])
    if message.content == "/m":
    	await message.channel.send(cmds["/m"])
    if message.content == "/s W":
    	await message.channel.send(social[0])
    if message.content == "/s D":
    	await message.channel.send(social[1])
    if message.content == "/s F":
    	await message.channel.send(social[2])
    if message.content == "/s T":
    	await message.channel.send(social[3])
    if message.content == "/s Wiki":
    	await message.channel.send(social[4])
    if message.content == "/s Y":
    	await message.channel.send(social[5])
    if message.content == "/s V":
    	await message.channel.send(social[6])
    if message.content == "/s Q":
    	await message.channel.send(social[7])
    if message.content == "/s I":
    	await message.channel.send(social[8])
    if message.content == "/s S":
    	await message.channel.send(social[9])
    if message.content == "/h":
    	await message.channel.send('''
TECHY BOT Commands:

General
/v			Validation
/a			About
/m 			Gives Music Links
/j 			Sends Jokes
school                  Gives the School Website

Social
/s W		Whatsapp
/s D		Discord
/s Q		Quora
/s F		Facebook
/s T		Twitter
/s Wiki		Wikipedia
/s Y		Youtube
/s V		Vimeo
/s I		Instagram

More Commands are Coming Soon!!
    		''')
    if message.content == ("hi" or "hello"):
    	await message.channel.send("Hello! Nice to meet You, Bro!")
    if message.content == "/v":
    	await message.channel.send("Validation will be added soon!!")
    if message.content == "/a":
    	await message.channel.send('''
NAME  -> TECHY BOT
OWNER -> TECH_FURY#4530
GUILD -> BOT_SERVER
    		''')
    if message.content == ("good morning" or "good night" or "good evening" or "good afternoon"):
        await message.channel.send(str(message.content).capitalize())
    if message.content == 'apology':
        await message.channel.send("I extremely apology for whatever I said! Very Sorry for that!")
    if message.content == 'school':
        await message.channel.send("https://www.donboscopatna.com/")
    

client.run(TOKEN)

'''
if message.content == 'school':
    response = cmds['school']
    await message.channel.send(response)
if message.content == 'discord':
    response = cmds['discord']
    await message.channel.send(response)
if message.content == 'whatsapp':
    response = cmds['whatsapp']
    await message.channel.send(response) 
if message.content == 'tell me a joke':
    response = cmds['jokes']
    await message.channel.send(response)
if message.content == 'apology':
    await message.channel.send("I extremely apology for whatever I said! Very Sorry for that!")

if 'hello' in str(message.content).lower():
	if 'an' in str(message.content).lower():
		await message.channel.send("Hello Anurag!")
	if 'ag' in str(message.content).lower():
		await message.channel.send("Hello, Atharva Gamer!")
	if 'sh' in str(message.content).lower():
		await message.channel.send("Hello, Shimeshu!")
if str(message.content).lower() == 'hi':
	await message.channel.send("Hello, Anurag!")   
'''
