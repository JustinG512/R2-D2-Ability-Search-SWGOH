import discord
import requests
import os

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
YOUR_CHANNEL_ID = os.getenv('CHANNEL_ID')

intents = discord.Intents.default()
intents.members = True  # enable the privileged gateway intent

client = discord.Client(intents=discord.Intents.default())

client.run(TOKEN)
