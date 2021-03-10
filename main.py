import discord

client = discord.Client()

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send('')
      print(f"messaged: {user.name}")
    except:
       print(f"couldnt message: {user.friends}")
client.run('', bot=False)

