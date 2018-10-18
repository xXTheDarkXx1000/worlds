import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_message(message):
    source_message = ".."
    searched = re.search(r"!!give.*riidefi.*(\d.*)", source_message)
    if searched and searched.group(0):
     send_message("Thanks, %s for $%s!" % (sender.name, searched.group(0)))
client.run('NTAxNDUwODAzOTY2Mzc3OTk0.DqZnmA.C0Q-jEFZRLoz0B90g2ZBBQAHa0A')
