import discord
from discord.ext import commands
import os
import random
import math
import datetime
import calendar
import time

bot = commands.Bot(command_prefix="!")
bot.remove_command("help")

last = calendar.timegm(time.gmtime()) - 300

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

@bot.event
async def on_message(message):
	global last
	now = calendar.timegm(time.gmtime())
	mollie = "mollie" in message.content.lower()
	if now - 900 >= last or (now - 300 >= last and mollie):
		last = calendar.timegm(time.gmtime())
		channel = message.channel
		s = open("messages.txt", "r")
		m = s.readlines()
		l = []
		for i in range(0, len(m) - 1):
			x = m[i]
			z = len(x)
			a = x[: z - 1]
			l.append(a)
		l.append(m[i + 1])
		reply = random.choice(l)
		await channel.send(reply)

bot.run(str(os.environ.get("BOT_TOKEN")))