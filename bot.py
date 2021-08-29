import discord
import os
client = discord.Client()
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd)
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    servers = len(client.guilds)
    members = 0
    for guild in client.guilds:
        members += guild.member_count - 1
    await client.change_presence(activity = discord.Activity(
        type = discord.ActivityType.watching,
        name = f'{members} members'
    ))
client.run("your token")