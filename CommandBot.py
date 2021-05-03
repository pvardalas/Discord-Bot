import discord
from discord.ext import commands
import random
import os
import youtube_dl


client = commands.Bot(command_prefix= '-')

OWNERID = 372703407276032020


ffmpeg_options = {
    'options': '-vn'
}

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name="-play"))
    print('Bot is ready...')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')



@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command(aliases=["anonymiseme"])
async def anonymise(ctx, *, message):
    await ctx.channel.purge(limit=1)
    await ctx.send(f'{message}')

@client.command(name="ban")
async def removecommandnotforuse(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mbed = discord.Embed(
        title = f"Banned {member}",
        description = f"{member} has been banned from the server because {reason} ... Bye Bye"
    )
    if ctx.author.guild_permissions.ban_members:
        if member.guild_permissions.administrator:
            await ctx.send("You can't ban a moderator...")
        else:
            await guild.ban(user=member)
            await ctx.send(embed=mbed)
            
    else:
        await ctx.send("You do not have the permission to ban a member.")






@client.command(name="unban")
@commands.has_permissions(ban_members=True)
async def unremovecommandnotforuse(ctx, *, member):


    banned_users = await ctx.guild.bans()

    member_name, member_disc = member.split('#')
    for banned_entry in banned_users:
        user = banned_entry.user
#
##        guild = ctx.guild
        mbed = discord.Embed(
            title = f"Unbanned {user}",
            description = f"{user.name} has been forgiven and can come back to the server... :)"
        )
#
        if (user.name, user.discriminator) == (member_name, member_disc):
##            if ctx.author.guild_permissions.ban_members:
            await ctx.send(embed=mbed)
            await ctx.guild.unban(user)
            return
# #           else:
#  #              await ctx.send("You do not have the permision to unban a user...")
    await ctx.send(member + " is not banned...")
            

    
    






@client.command(name="kick")
async def tempremovecommandnotforuse(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mbed = discord.Embed(
        title = f"Kicked {member}",
        description = f"{member} has been kicked from the server because {reason} ... Bye Bye :)"
    )
    if ctx.author.guild_permissions.ban_members:
        await ctx.send(embed=mbed)
        await guild.kick(member)

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.reload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.command(name="lock")
async def locknotforuse(ctx):

    islocked = True

@client.command(name="unlock")
async def unlocknotforuse(ctx):

    islocked = False
    ctx.send("works")


@client.event
async def on_message(message):
    await client.process_commands(message)
    if ".unlock" == message.content:
        await message.delete()
    else:
        return

    

#@client.event
#async def on_message(message):
#    if message.author.id == 372703407276032020:
#        return
#    else:
#        await ctx.delete()
#        await ctx.channel.send(f'{message}')



#    if message.author.bot:
#        return
#    else:
#        await message.channel.send(f'{message.author.name} said {message.content}')


@client.command(pass_context=True)
async def chnick(ctx, member: discord.Member, nick):
    await ctx.channel.purge(limit=1)
    await member.edit(nick=nick)

@client.command(name="react")
async def reacthere(ctx, condition=None, *args):



    message = ' '.join(args)
    if message == "":
        message = None



    if condition == None and message == None:
        await ctx.send("Please provide a type and a message first. Usage: .react <type> <message>. The valid types are: vote. More types coming soon...")
    elif condition == None and message != None:
        await ctx.send("Please provide a type first... Valid types are: vote. More types coming soon...")
    elif message == None and condition != None:
        await ctx.send("There is no message to react... Add a message to react on...")
    elif condition == "vote" and message != None:
        msg = await ctx.send(f"Vote: {message}")
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")
    elif condition == "test" and message != None:
        await ctx.send("test")
    elif condition != "vote" or "test" and message != None:
        await ctx.send("This type is not valid. Please provide a valid type... Valid types are: vote. More types coming soon...")
    




client.run('ODM4NTAzNTc0MTM2ODE1Njg4.YI8DTg.i2BhZaq2EQIgf_VeLn8qOK9in5M')