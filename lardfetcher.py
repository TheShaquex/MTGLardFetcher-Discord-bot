import discord
import random
import re

# Precompile the regular expression pattern
command_pattern = re.compile(r"\{\{.*?\}\}")

# Create a Discord client with intents
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Load the image links from the archive into a set
with open("image_links.txt", "r") as f:
    image_links = set(f.read().splitlines())

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    # Check if the message contains {{ and }} in the correct order
    if command_pattern.search(message.content):
        # Choose a random image link from the set
        random_link = random.choice(list(image_links))

        # Reply to the message with the random image link
        await message.reply(random_link)

# Put your own bot token inside the ''
client.run('TOKEN GOES HERE')