import discord

client = discord.Client()

@client.event
async def on_message(message):
    #Per the discord.py docs this is to not have the bot respond to itself
    if message.author == client.user:
        return
    #If the bot sees the command """ we will respond with our message string
    if message.content.startswith('!test'):
        msg = '{0.author.mention}, this is the test function!'.format(message)
        await client.send_message(message.channel, msg)

    for value in message.role_mentions:
        if str(value) == "Overwatch":
            msg = "Wrenbot says: Working so no."
            await client.send_message(message.channel, msg)
            return
        # else:
            # print("Doesn't work.")


    check = message.content.split()

    if "Overwatch" in check:
        msg = 'Wrenbot says: Working so no.'
        await client.send_message(message.channel, msg)

    elif "OW" in check:
        msg = 'Wrenbot says: Sleeping so no.'
        await client.send_message(message.channel, msg)

    # for value in message.role_mentions:
        # if value == "Overwatch":
            # msg = "This works."
            # await client.send_message(message.channel, msg)

    # try "if xxx in xxxxxxxxx: do this"
@client.event
async def wrenbot(message):
    if message.author == client.user:
        return

    for value in message.role_mentions:
        if value == "Overwatch":
            print(value)
        else:
            print("Not working.")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run("MzEzNTI3MDU2MDIzNDIwOTI4.C_0row.JV4sBf22Ret-8HC1ES4Q0dbc9sE")
