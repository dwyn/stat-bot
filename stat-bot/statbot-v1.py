# Import necessary modules
import os
import random
import disnake
import asyncio
from disnake.ext import commands
from disnake import Button, ButtonStyle

# Retrieve the bot's token and guild name from environment variables
token = os.getenv("DISCORD_TOKEN")
my_guild = os.getenv("DISCORD_GUILD")

# Initialize the default intents for the bot
intents = disnake.Intents.default()
# Ensure the bot can receive messages
intents.messages = True

# Create a bot instance with a command prefix of "$" and the specified intents
bot = commands.Bot(command_prefix="$", intents=intents)

# Event that triggers when the bot is ready
@bot.event
async def on_ready():
    # Print a message indicating the bot's username
    print(f'We have logged in as {bot.user}')

# Event that triggers when a message is received
@bot.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == bot.user:
        return

    # Convert the message content to lowercase and remove any leading/trailing spaces
    message_content = message.content.lower().strip()

    # Check if the message content is "flip a coin" or "fac"
    if message_content == "flip a coin" or message_content == "fac":
        # Generate a random integer (0 or 1) to determine the coin flip result
        rand_int = random.randint(0, 1)
        # If the random integer is 0, the result is "Heads", otherwise it's "Tails"
        if rand_int == 0:
            results = "Heads"
        else:
            results = "Tails"

        # Send a series of playful messages indicating the coin flip process
        await message.channel.send(f"woooowww :open_mouth: {message.author} really just asked me to flip a coin :rolling_eyes:")
        await asyncio.sleep(0.5)
        await message.channel.send("Flipping the coin...")
        await asyncio.sleep(1.0)
        await message.channel.send("The coin has landed...")
        await asyncio.sleep(1.25)
        await message.channel.send(results + "!   [happy? :upside_down:]")

    # Process any commands in the message
    await bot.process_commands(message)

# Command that responds with "Hello!" when invoked
@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

# Command that sends a message with a button to start a workflow
@bot.command()
async def start(ctx):
    # Create a button labeled "Start Workflow"
    button = Button(style=ButtonStyle.primary, label="Start Workflow")
    # Send the button to the channel
    await ctx.send("Click the button to start the workflow.", components=[button])

# Event that triggers when a button is clicked
@bot.event
async def on_button_click(interaction):
    # Check if the clicked button's label is "Start Workflow"
    if interaction.component.label == "Start Workflow":
        # Prompt the user to upload an image file
        await interaction.response.send_message("Please upload an image file.")
        # Define a check function to wait for an image file upload from the user
        def check(m):
            return m.author == interaction.user and m.attachments

        # Wait for the user to upload an image
        image_message = await bot.wait_for('message', check=check)
        # Thank the user for the image and prompt them to enter their Xbox gamertag
        await interaction.channel.send("Thank you for the image. Please enter your Xbox gamertag.")
        # Wait for the user to enter their gamertag
        gamer_tag_message = await bot.wait_for('message', check=lambda m: m.author == interaction.user)
        gamer_tag = gamer_tag_message.content
        # Confirm receipt of the gamertag and complete the workflow
        await interaction.channel.send(f"Received your gamertag: {gamer_tag}. Workflow complete!")

# Run the bot using the specified token
bot.run(token)
