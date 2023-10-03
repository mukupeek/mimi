import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=discord.Intents.all())
msg = None


# def reaction_add(message):
#     message.add_reaction('✅')
#
#
# reaction_add(1038519665040838677)


# @bot.command()
# async def add_reactions(ctx):
#     global msg
#     msg = 1038519665040838677
#     emoji = '✅'
#     await ctx.message.add_reaction(emoji)


@bot.event
async def on_raw_reaction_add(payload):
    channel = bot.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    guild = bot.get_guild(payload.guild_id)
    reaction = discord.utils.get(message.reactions, emoji=payload.emoji.name)

    # only work if it is the client
    if payload.member.id == bot.user.id:
        return

    # verif
    async def like():
        match payload.emoji.name:
            case '3908purple0wiii':
                await payload.member.add_roles(discord.utils.get(guild.roles, id=1038522325366218772))
            case '9742purple1wiii':
                await payload.member.add_roles(discord.utils.get(guild.roles, id=1038545540532670466))
            case '2298purple2wiii':
                await payload.member.add_roles(discord.utils.get(guild.roles, id=1038545547428110346))
            case '9742purple3wiii':
                await payload.member.add_roles(discord.utils.get(guild.roles, id=1038544599611871232))
            case '8948purple4wiii':
                await payload.member.add_roles(discord.utils.get(guild.roles, id=1038545538523615282))
            case '4267purple5wiii':
                await payload.member.add_roles(discord.utils.get(guild.roles, id=1038545535868620940))
            case '9470purple6wiii':
                await payload.member.add_roles(discord.utils.get(guild.roles, id=1038545531779166309))
            case '5490purple7wiii':
                await payload.member.add_roles(discord.utils.get(guild.roles, id=1038545552935235604))
            case '9127purple8wiii':
                await payload.member.add_roles(discord.utils.get(guild.roles, id=1038545558220062730))
            case '9127purple9wiii':
                await payload.member.add_roles(discord.utils.get(guild.roles, id=1038545555799937084))

    async def boys_and_girls():
        match payload.emoji.name:
            case '9742purple1wiii':
                await payload.member.add_roles(discord.utils.get(guild.roles, id=1038546463447334962))
            case '2298purple2wiii':
                await payload.member.add_roles(discord.utils.get(guild.roles, id=1038546466278481940))

    async def verif():
        if reaction.emoji == '✅':
            num = [1038199925189640323, 1037845308517924885, 1037845381188435969, 1038199922379464776,
                   1038213629318799360,
                   1038464914718724248]
            for draw in range(len(num)):
                await payload.member.add_roles(discord.utils.get(guild.roles, id=num[draw]))
                await reaction.clear()

    match payload.message_id:
        case 1038519665040838677:
            await verif()
        case 1038579472800153610:
            await boys_and_girls()
        case 1038576815456931900:
            await like()


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


@bot.command()
async def post(ctx):
    z = ctx.message.content

    await ctx.send(z[6:100000000000])
    await ctx.message.delete()


bot.run("MTAzOTk3OTMxMDYyODQ4MzEyNA.G-UM8H.grlMoEL9psu3MuhHrkrOILMAUax7JHmhFa3nrU")
