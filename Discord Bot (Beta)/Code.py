import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# intents = discord.Intents.default()
# intents.members = True
# intents.message_content = True
# intents.presences = True
bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all()) # requires ! before any command

@bot.event 
async def on_ready():
    general = await bot.fetch_channel(1222170376335921182)
    await general.send("I have arrived!")

@bot.command(name = "99", help = "Responds with a random quote from Brooklyn 99")
# now will be called when !99 is said in chat
# help = sets the description for the !help command for THIS particular command (help only exists for discord bot, not client)
async def nine_nine(ctx):    # ctx stands for context (for the command), COMPULSARY ONLY FOR COMMANDS, holds data such as channel and guild
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name = "roll_dice", help = "Simulates rolling dice.")
async def roll(ctx, number_of_dice: int, number_of_sides: int): # : int basically converts the variable taken to integer, similar to int()
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(", ".join(dice))
# call the roll dice function by doing: !roll_dice 2, 4. NOT !roll_dice(2,4)
# you can also use !help roll_dice to see the arguments taken

@bot.command(name = "create_channel", help = "Creates a new text channel. Only for developers")
@commands.has_role("developer") # only role called "developer" can use this command
async def create_channel(ctx, channel_name):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name = channel_name) # check if channel exist / theres another channel with the same name
    if not existing_channel: 
        print(f"Creating a new channel: {channel_name}")
        await guild.create_text_channel(channel_name)

@bot.command(name = "say", help = "Make the bot anything you want!")
async def say_this(ctx, stuff = commands.parameter(description="For multiple words, connect them with quotation marks as such: 'words'")): 
    # gives the parameter help description as well
    await ctx.send(stuff)

@bot.event
async def on_command_error(ctx, error): 
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send("You do not have the correct role for this command.")

bot.run(TOKEN)
