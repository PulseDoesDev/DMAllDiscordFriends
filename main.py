import discord

client = discord.Client()

@client.event
async def on_ready():
  for user in client.user.friends:
    try:
      await user.send('')
      print(f"messaged: {user.name}")
    except Exception as e:
       print(f"couldnt message: {user.name} - {e}")
client.run('', bot=False)

