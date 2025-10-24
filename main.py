import discord
from dotenv import load_dotenv
import os
from discord.ext import commands
import logging

handler = logging.FileHandler(filename='discordbot.log', mode='w', encoding='utf-8')

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Ready! Ich bin {bot.user}.')


@bot.event
async def on_message(message):
    channel = message.channel

    if message.author == bot.user:
        return
    
    if 'hallo' in message.content.lower():
        await channel.send(f'Hallo, {message.author}!')

    if 'banana' in message.content.lower():
        await message.delete()
        #channel = message.channel
        await channel.send(f'Hey, {message.author}! Dieser Begriff ist nur für die Schüler*innen der DA geeignet.')

    await bot.process_commands(message)


bot.run(token, log_handler=handler, log_level=logging.DEBUG)

