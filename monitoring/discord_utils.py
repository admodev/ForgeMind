import os
import discord

from gpu_monitoring import GetGPUStatus
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID", 0))

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")

    channel = bot.get_channel(CHANNEL_ID)

    if channel:
        await channel.send("The bot is online, all hail the almighty!")
    else:
        print(f"Channel not found. Checked ID: {CHANNEL_ID}")

@bot.command()
async def status(ctx):
    await ctx.send("The server status is: statushere")

@bot.command()
async def gpustatus(ctx):
    await ctx.send(f"The GPU Status is: {GetGPUStatus()}")

bot.run(BOT_TOKEN)

