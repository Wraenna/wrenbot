import discord
import asyncio
from discord.ext.commands import Bot

my_bot = Bot(command_prefix="@")
client = discord.Client()

@my_bot.event
async def on_read():
    print("Client logged in")

@my_bot.command()
async def hello(*args):
    return await my_bot.say("Hello, world!")

@my_bot.command()
async def Overwatch(*args):
    return await my_bot.say("Wrenbot says: Working so no.")

my_bot.run("MzEzNTI3MDU2MDIzNDIwOTI4.C_0row.JV4sBf22Ret-8HC1ES4Q0dbc9sE")
