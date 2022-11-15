import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=discord.Intents.all())


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
    if payload.message_id == 1038519665040838677 and reaction.emoji == '✅':
        roleid = 1038199925189640323
        role = discord.utils.get(guild.roles, id=roleid)
        await payload.member.add_roles(role)
        roleid = 1037845308517924885
        role = discord.utils.get(guild.roles, id=roleid)
        await payload.member.add_roles(role)
        roleid = 1037845381188435969
        role = discord.utils.get(guild.roles, id=roleid)
        await payload.member.add_roles(role)
        roleid = 1038199922379464776
        role = discord.utils.get(guild.roles, id=roleid)
        await payload.member.add_roles(role)
        roleid = 1038213629318799360
        role = discord.utils.get(guild.roles, id=roleid)
        await payload.member.add_roles(role)
        roleid = 1038464914718724248
        role = discord.utils.get(guild.roles, id=roleid)
        await payload.member.add_roles(role)
    # Boys
    if payload.message_id == 1038579472800153610 and payload.emoji.name == '9742purple1wiii':
        roleid = 1038546463447334962
        role = discord.utils.get(guild.roles, id=roleid)
        await payload.member.add_roles(role)

    if payload.message_id == 1038579472800153610 and payload.emoji.name == '2298purple2wiii':
        roleid = 1038546466278481940
        role = discord.utils.get(guild.roles, id=roleid)
        await payload.member.add_roles(role)
    # игры

    if payload.message_id == 1038576815456931900 and payload.emoji.name == '3908purple0wiii':
        roleid = 1038522325366218772
        role = discord.utils.get(guild.roles, id=roleid)
        await payload.member.add_roles(role)

    if payload.message_id == 1038576815456931900 and payload.emoji.name == '9742purple1wiii':
        roleid = 1038545540532670466
        role = discord.utils.get(guild.roles, id=roleid)
        await payload.member.add_roles(role)

    if payload.message_id == 1038576815456931900 and payload.emoji.name == '2298purple2wiii':
        roleid = 1038545547428110346
        role = discord.utils.get(guild.roles, id=roleid)
        await payload.member.add_roles(role)

    if payload.message_id == 1038576815456931900 and payload.emoji.name == '9742purple3wiii':
        roleid = 1038544599611871232
        role = discord.utils.get(guild.roles, id=roleid)
        await payload.member.add_roles(role)

    if payload.message_id == 1038576815456931900 and payload.emoji.name == '8948purple4wiii':
        roleid = 1038545538523615282
        role = discord.utils.get(guild.roles, id=roleid)
        await payload.member.add_roles(role)

    # увлечения

    if payload.message_id == 1038576815456931900 and payload.emoji.name == '4267purple5wiii':
        roleid = 1038545535868620940
        role = discord.utils.get(guild.roles, id=roleid)
        await payload.member.add_roles(role)

    if payload.message_id == 1038576815456931900 and payload.emoji.name == '9470purple6wiii':
        roleid = 1038545531779166309
        role = discord.utils.get(guild.roles, id=roleid)
        await payload.member.add_roles(role)

    if payload.message_id == 1038576815456931900 and payload.emoji.name == '5490purple7wiii':
        roleid = 1038545552935235604
        role = discord.utils.get(guild.roles, id=roleid)
        await payload.member.add_roles(role)

    if payload.message_id == 1038576815456931900 and payload.emoji.name == '9127purple9wiii':
        roleid = 1038545555799937084
        role = discord.utils.get(guild.roles, id=roleid)
        await payload.member.add_roles(role)

    if payload.message_id == 1038576815456931900 and payload.emoji.name == '9127purple8wiii':
        roleid = 1038545558220062730
        role = discord.utils.get(guild.roles, id=roleid)
        await payload.member.add_roles(role)


# @bot.event
# async def on_raw_reaction_delete(payload):
#     channel = bot.get_channel(payload.channel_id)
#     message = await channel.fetch_message(payload.message_id)
#     guild = bot.get_guild(payload.guild_id)
#     reaction = discord.utils.get(message.reactions, emoji=payload.emoji.name)
#
#     # only work if it is the client
#     if payload.member.id == bot.user.id:
#         return
#     # игры
#     if payload.message_id == 1038576815456931900 and reaction.emoji == bot.get_emoji(1038547964622274682):
#         roleid = 1038522325366218772
#         role = discord.utils.get(guild.roles, id=roleid)
#         await reaction.remove(payload.member)
#     if payload.message_id == 1038576815456931900 and reaction.emoji == bot.get_emoji(1038547861643735060):
#         roleid = 1038545540532670466
#         role = discord.utils.get(guild.roles, id=roleid)
#         await reaction.remove(payload.member)
#     if payload.message_id == 1038576815456931900 and reaction.emoji == bot.get_emoji(1038547871642964049):
#         roleid = 1038545547428110346
#         role = discord.utils.get(guild.roles, id=roleid)
#         await reaction.remove(payload.member)
#     if payload.message_id == 1038576815456931900 and reaction.emoji == bot.get_emoji(1038547881688301588):
#         roleid = 1038544599611871232
#         role = discord.utils.get(guild.roles, id=roleid)
#         await reaction.remove(payload.member)
#     if payload.message_id == 1038576815456931900 and reaction.emoji == bot.get_emoji(1038547893562376343):
#         roleid = 1038545538523615282
#         role = discord.utils.get(guild.roles, id=roleid)
#         await reaction.remove(payload.member)
#     # увлечения
#
#     if payload.message_id == 1038576815456931900 and reaction.emoji == bot.get_emoji(1038547909366530059):
#         roleid = 1038545535868620940
#         role = discord.utils.get(guild.roles, id=roleid)
#         await reaction.remove(payload.member)
#     if payload.message_id == 1038576815456931900 and reaction.emoji == bot.get_emoji(1038547921915875398):
#         roleid = 1038545531779166309
#         role = discord.utils.get(guild.roles, id=roleid)
#         await reaction.remove(payload.member)
#     if payload.message_id == 1038576815456931900 and reaction.emoji == bot.get_emoji(1038547934658174976):
#         roleid = 1038545552935235604
#         role = discord.utils.get(guild.roles, id=roleid)
#         await reaction.remove(payload.member)
#     if payload.message_id == 1038576815456931900 and reaction.emoji == bot.get_emoji(1038547945483677726):
#         roleid = 1038545555799937084
#         role = discord.utils.get(guild.roles, id=roleid)
#         await reaction.remove(payload.member)
#     if payload.message_id == 1038576815456931900 and reaction.emoji == '✅':
#         roleid = 1038545558220062730
#         role = discord.utils.get(guild.roles, id=roleid)
#         await reaction.remove(payload.member.role)


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


@bot.command()
async def post(ctx):
    z = ctx.message.content

    await ctx.send(z[6:100000000000])
    await ctx.message.delete()


bot.run("MTAzOTk3OTMxMDYyODQ4MzEyNA.GJji52.totfueHXMSLoAtaGZ0AcfOPikhgirJeQCoxt38")
