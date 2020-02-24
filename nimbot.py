import os
import random
from discord.ext import commands
from dotenv import load_dotenv
from datetime import datetime
import pytz

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='nim')
async def play_nim(ctx):
    await ctx.send("Still working on it, kiddo.")

@bot.command(name ="coin")
async def flip_coin(ctx):
    await ctx.send(random.choice(["Heads", "Tails"]))

@bot.command(name ="avg")
async def avg(ctx, a,b)
    await ctx.send(sum(a,b)/2)

@bot.command(name ="time")
async def time(ctx):
    time_zone_NJ = pytz.timezone('US/Eastern')
    now = datetime.now(time_zone_NJ)
    current_time = now.strftime("%H:%M:%S")
    await ctx.send(current_time)

bot.run(token)

