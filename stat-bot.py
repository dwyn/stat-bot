import os
import random
import discord
import asyncio

token = os.getenv("DISCORD_TOKEN")
my_guild = os.getenv("DISCORD_GUILD")

intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == my_guild:
            break

    print(
        f"{client.user} is connected to the following guild:\n"
        f"{guild.name}(id: {guild.id})"
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    message_content = message.content.lower()

    if "flip a coin" or "fac " in message_content:
        rand_int = random.randint(0, 1)
        if rand_int == 0:
            results = "Heads"
        else:
            results = "Tails"

        await message.channel.send(f"woooowww :open_mouth: {message.author} really just asked me to flip a coin :rolling_eyes:")
        await asyncio.sleep(0.5)  # waits for 500 milliseconds
        await message.channel.send("Flipping the coin...")
        await asyncio.sleep(1.0)  # waits for 500 milliseconds
        await message.channel.send("The coin has landed...")
        await asyncio.sleep(1.25)  # waits for 500 milliseconds
        await message.channel.send(results + "!   [happy? q:upside_down:]")

client.run(token)
