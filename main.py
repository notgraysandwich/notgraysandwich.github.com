# This example requires the 'message_content' intent.

import asyncio
import time
import discord
import random
from keep_alive import keep_alive
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
timerStarted=False
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    global timerStarted
    global start_time
    if message.author == client.user:
        return

    if message.content.startswith('$accuracy'):
        if timerStarted==True:
            end_time = time.time()
            duration = end_time - start_time
            await message.channel.send("Total time:")
            await message.channel.send(duration)
            await message.channel.send("You missed by:")
            await message.channel.send(+abs(10-(duration)))
            timerStarted=False

        else:
            await message.channel.send('type $accuracy after exactly 10 seconds.')
            start_time = time.time()
            timerStarted=True
    if message.content.startswith('$test'):
        await message.channel.send('screw you')
        time.sleep(10)
        await message.channel.send('lol')
    if message.content.startswith('$recursion'):
        await message.channel.send('?say $recursion')
    if message.content.startswith('$reactiontest'):
        wait_time = random.uniform(0.9, 4.1)
        await asyncio.sleep(wait_time)  # Use asyncio.sleep for async sleep
        sent_message = await message.channel.send("Click the reaction!")
        emoji = '\N{WHITE HEAVY CHECK MARK}'  # Emoji character code for check mark
        await sent_message.add_reaction(emoji)
        start_time_reaction = time.time()
        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == emoji and reaction.message == sent_message

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=10.0, check=check)
            end_time_reaction = time.time()
            await message.channel.send("Your reaction time: {:.2f} seconds".format(end_time_reaction - start_time_reaction-0.2))
        except asyncio.TimeoutError:
            await message.channel.send("You did not react in time.")
keep_alive()
client.run('MTIzNzYxNjYwNzk3NTU3MTU2Nw.GLhAw5.UfhYpnR76HnJ82RslAWhciuA9ZcPDBXBhGzWRA')
