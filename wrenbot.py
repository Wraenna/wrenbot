""" -----------------------------------------
Wrenbot - an autoresponder for Discord

This bot is designed to respond automatically
whenever the role for Overwatch is mentioned
in any given server.

Things to update: Call the name of the role
properly instead of the hack-y way using
str(value).
----------------------------------------- """
import discord
import string

client = discord.Client()

@client.event
async def on_message(message):

    mentions_list = message.mentions
    message_content = message.content.lower()
    message_content = message_content.translate(message_content.maketrans("","", string.punctuation))
    message_content = message_content.split()
    #Per the discord.py docs this is to not have the bot respond to itself
    if message.author == client.user:
        return
    #Autoresponder for pinging Overwatch.
    for value in message.role_mentions:
        if str(value) == "Overwatch":
            msg = "Wrenbot says: Working so no."
            await client.send_message(message.channel, msg)
            return

    #Autoresponder if Wren is pinged
    for username in mentions_list:
        if str(username) == "Synchronise#0768":
            msg = "Pretend I made a sick pun here."
            await client.send_message(message.channel, msg)
            return

    for word in message_content:
        if word == "rando" or word == "randos":
            msg = "To the other players, YOU are the rando!"
            await client.send_message(message.channel, msg)
            return
        elif word == "gigantic":
            msg = "See you on the airship!"
            await client.send_message(message.channel, msg)
            return
        elif word == "rip":
            msg = "rip in peperony and chease"
            await client.send_message(message.channel, msg)
            return

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run("TOKENID")
