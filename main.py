import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
bot.remove_command("help")

@bot.event
async def on_ready():
	print("Logged in.")

@bot.event
async def on_member_join(member):
	for channel in member.guild.channels:
		if channel.name == "general":
			await channel.send("Welcome " + member.mention + " to the server!")
			return

@bot.event
async def on_member_remove(member):
	for channel in member.guild.channels:
		if channel.name == "general":
			await channel.send("Sadly, " + member.name + " just left the server.")
			return

async def decade(ctx):
    return ctx.author.id == 234109055554158593

bot.run(str(os.environ.get("BOT_TOKEN")))