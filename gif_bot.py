# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot

import discord
import gifs
import key

#####data###############
TOKEN = key.key
########################

#####functions##########


def print_commands():
    string = "Gifs: "
    for _ in gifs.commands:
        string = string + _ + ", "
    return string


########################


client = discord.Client()


@client.event
async def on_ready():
    print('Bot is Online!')


@client.event
async def on_message(message):

    if message.content.startswith('!gifs'):
        await message.channel.send(print_commands())

    if message.content.startswith(gifs.here_we_go_again.command):
        await message.channel.send(gifs.here_we_go_again.link)

    if message.content.startswith(gifs.addict.command):
        await message.channel.send(gifs.addict.link)


try:
    client.run(TOKEN)
except discord.HTTPException as e:
    if e.status == 429:
        print("The Discord servers denied the connection for making too many requests")
        print("Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests")
    else:
        raise e
