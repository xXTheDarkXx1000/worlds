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
    if message.content.startswith('!!give-money @riidefi#4002'):
        await client.send_message(message.channel,'Hey Thanks for giving me 100$ <@%s>!'  %(message.author.id))
    if message.content.startswith('!!give-money riidefi#4002'):
        await client.send_message(message.channel,'Hey Thanks for giving me 100$ <@%s>!'  %(message.author.id))
    if message.content.startswith('!!give-money riidefi'):
        await client.send_message(message.channel,'Hey Thanks for giving me 100$ <@%s>!'  %(message.author.id))
client.run('NTAxNDUwODAzOTY2Mzc3OTk0.DqZnmA.C0Q-jEFZRLoz0B90g2ZBBQAHa0A')
