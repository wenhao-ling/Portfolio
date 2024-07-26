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


# 2nd blackjack attempt
class blackjackview(discord.ui.View):
    def __init__(self, deck: list):
        super().__init__()
        self.deck = deck
        self.start = True
        self.bot_stand = False
        self.bot_value = []
        self.won = ""
        self.bot_died = False
        self.died = False
        self.value = []

    def bot_hit(self):
        card = random.randint(1,sum(self.deck))
        for j in range(len(self.deck)): 
            card -= self.deck[j]
            if card <= 0:
                self.bot_value.append(j+1) # no need to minus 1 since j starts from 0
                break
        self.deck[j] -= 1 
    def player_hit(self):
        card = random.randint(1,sum(self.deck))
        for j in range(len(self.deck)): 
            card -= self.deck[j]
            if card <= 0: 
                self.value.append(j+1) # no need to minus 1 since j starts from 0
                break
        self.deck[j] -= 1
    def checks(self):
        if sum(self.bot_value) < 21:
            pass
        elif sum(self.bot_value) == 21 and sum(self.value) != 21:
            return 'died' # since player lost
        elif sum(self.bot_value) > 21: # ded
            if 11 in self.bot_value:
                self.bot_value[self.bot_value.index(11)] = 1 # if about to die, ace become 1
                # no need for while loop, since 1 ace changing will make value <21
                print("ace used")
            else:
                return 'bot_died'
        if sum(self.value) < 21:
            pass
        elif sum(self.value) == 21 and sum(self.bot_value) != 21:
            return 'bot_died' # since bot lost
        elif sum(self.value) > 21:
            if 11 in self.value:
                self.value[self.value.index(11)] = 1
                print("ace used")
            else:
                return 'died'
        
        if self.stand and self.bot_stand:
            if sum(self.value) > sum(self.bot_value):
                return 'bot_died'
            elif sum(self.value) < sum(self.bot_value):
                return 'died'

    @discord.ui.button(label="Deal Cards", style = discord.ButtonStyle.green)
    async def start(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Dealing Cards!")
        for i in range(2):
            self.bot_hit()
            self.player_hit()
        
        print(self.value, self.bot_value)
        await interaction.channel.send(f"Your cards are: {self.value}")

    @discord.ui.button(label="Hit", style = discord.ButtonStyle.blurple)
    async def hit(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("You clicked Hit!")

        self.player_hit()

        # bot ai
        if (sum(self.bot_value) < 17 or (sum(self.bot_value) < 20 and random.randint(0,1))) and not self.bot_stand:
            print("bot hit")
            self.bot_hit()
        else:
            self.bot_stand = True
            print("bot stand")

        print(self.value, self.bot_value)

        # died check
        if self.checks() == 'died':
            self.died = True
        elif self.checks() == 'bot_died':
            self.bot_died = True

        if self.bot_died:
            self.won = "You"
        elif self.died:
            self.won = "I"

        if self.won == "Tie":
            print("Tie!")
            await interaction.channel.send("Tie!")
        elif  self.won != "": 
            await interaction.channel.send(f"{self.won} won!")
            await interaction.channel.send("To restart, call the !blackjack function again!")
            await interaction.channel.send(f"The bot's cards are: {self.bot_value}") 

        await interaction.channel.send(f"Your cards are: {self.value}")


    @discord.ui.button(label="Stand", style = discord.ButtonStyle.blurple)  # DO THIS TMR 26/7/2024
    async def stand(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("You clicked Stand!")

        # bot ai
        while self.bot_stand != True:
            if (sum(self.bot_value) < 17 or (sum(self.bot_value) < 20 and random.randint(0,1))) and not self.bot_stand:
                print("bot hit")
                self.bot_hit()
            else:
                self.bot_stand = True
                print("bot stand")

        print(self.value, self.bot_value)

        # died check
        if self.checks() == 'died':
            self.died = True
        elif self.checks() == 'bot_died':
            self.bot_died = True

        if self.bot_died:
            self.won = "You"
        elif self.died:
            self.won = "I"
        else:
            self.won = "Tie"

        if self.won == "Tie":
            await interaction.channel.send("Tie!")
        elif  self.won != "": 
            await interaction.channel.send(f"{self.won} won!")
            await interaction.channel.send("To restart, call the !blackjack function again!")
            await interaction.channel.send(f"The bot's cards are: {self.bot_value}") 

        await interaction.channel.send(f"Your cards are: {self.value}")        
        
@bot.command(name = "blackjack", help = "Play blackjack with me!")
async def blackjack(ctx):
    deck = [4,4,4,4,4,4,4,4,4,12,4] # value of each card is based on the index, values in each index is the number of cards
    await ctx.reply(content = "Blackjack", view=blackjackview(deck))


bot.run(TOKEN)
