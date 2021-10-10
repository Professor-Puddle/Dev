import os
import discord
from discord.ext import commands
from keep_alive import keep_alive

#-----------------------------------
prefix = "p " #bot prefix
ownerid = 835502093246660618 #your current account's ID
adminroleid = 842775556772069406 # the role's ID
#-----------------------------------

token = os.environ['token']
bot = commands.Bot(command_prefix=prefix,help_command=None)

def noperms(var):
  return("Hello " + var.author.mention + "! Sorry, but you don't have permission to use that command.")

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the server"))
  print(f'{bot.user} is online')

@bot.command()
async def addadminto(ctx,user : discord.Member):
  if ctx.author.id == ownerid:
    role = ctx.guild.get_role(adminroleid)
    await user.add_roles(role)
    await ctx.reply("Successfully added the admin role to <@"+str(user.id)+">")
  else:
    await ctx.message.delete()
    await ctx.author.send(noperms(ctx))

@bot.command()
async def removeadminfrom(ctx,user : discord.Member):
  if ctx.author.id == ownerid:
    role = ctx.guild.get_role(adminroleid)
    await user.remove_roles(role)
    await ctx.reply("Successfully removed the admin role from <@"+str(user.id)+">")
  else:
    await ctx.message.delete()
    await ctx.author.send(noperms(ctx))

keep_alive()
bot.run(token)
