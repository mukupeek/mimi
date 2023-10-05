import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


# @bot.command()
# async def helper(ctx):
#  embed = discord.Embed(title="Список команд", description="Список доступных команд бота", color=discord.Color.blue())
#
#     embed.add_field(name="!post", value="Создаёт пост от имени бота", inline=False)
#     embed.add_field(name="!ping", value="Пинг Понг", inline=False)
#
#     await ctx.send(embed=embed)


@bot.event
async def on_member_remove(member):
    message = '***Пока пока*** :( ' + member.mention
    channel = bot.get_channel(1038151796180402257)
    await channel.send(message)


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
        member = payload.member
        if payload.emoji.name == '✅':
            num = [1038199925189640323, 1037845308517924885, 1037845381188435969, 1038199922379464776,
                   1038213629318799360,
                   1038464914718724248]
            for draw in range(len(num)):
                await payload.member.add_roles(discord.utils.get(guild.roles, id=num[draw]))
            await reaction.remove(user=payload.member)
            message_to_hi = '***Привет привет, милый котик :3*** ' + member.mention
            channel_to_hi = bot.get_channel(1038151796180402257)
            await channel_to_hi.send(message_to_hi)

    match payload.message_id:
        case 1038519665040838677:
            await verif()
        case 1038579472800153610:
            await boys_and_girls()
        case 1038576815456931900:
            await like()


@bot.event
async def on_raw_reaction_remove(payload):
    guild = bot.get_guild(payload.guild_id)
    payload.member = guild.get_member(payload.user_id)

    async def boys_and_girls():
        match payload.emoji.name:
            case '9742purple1wiii':
                await payload.member.remove_roles(discord.utils.get(guild.roles, id=1038546463447334962))
            case '2298purple2wiii':
                await payload.member.remove_roles(discord.utils.get(guild.roles, id=1038546466278481940))

    async def like():
        match payload.emoji.name:
            case '3908purple0wiii':
                await payload.member.remove_roles(discord.utils.get(guild.roles, id=1038522325366218772))
            case '9742purple1wiii':
                await payload.member.remove_roles(discord.utils.get(guild.roles, id=1038545540532670466))
            case '2298purple2wiii':
                await payload.member.remove_roles(discord.utils.get(guild.roles, id=1038545547428110346))
            case '9742purple3wiii':
                await payload.member.remove_roles(discord.utils.get(guild.roles, id=1038544599611871232))
            case '8948purple4wiii':
                await payload.member.remove_roles(discord.utils.get(guild.roles, id=1038545538523615282))
            case '4267purple5wiii':
                await payload.member.remove_roles(discord.utils.get(guild.roles, id=1038545535868620940))
            case '9470purple6wiii':
                await payload.member.remove_roles(discord.utils.get(guild.roles, id=1038545531779166309))
            case '5490purple7wiii':
                await payload.member.remove_roles(discord.utils.get(guild.roles, id=1038545552935235604))
            case '9127purple8wiii':
                await payload.member.remove_roles(discord.utils.get(guild.roles, id=1038545558220062730))
            case '9127purple9wiii':
                await payload.member.remove_roles(discord.utils.get(guild.roles, id=1038545555799937084))

    match payload.message_id:
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
    embedVar = discord.Embed(description=z[6:100000000000], color=0xe6e6fa)
    if len(ctx.message.attachments) > 0:
        for sex in range(len(ctx.message.attachments)):
            y = ctx.message.attachments[sex].url
            embedVar.set_image(url=y)

        await ctx.send(embed=embedVar)
        await ctx.message.delete()
    else:
        await ctx.send(embed=embedVar)
        await ctx.message.delete()


# Add realization more than 1 pic
# Guildsg

bot.run("MTAzOTk3OTMxMDYyODQ4MzEyNA.GkJ5F1.u3Bp503Vi4LOX6oAUa3ztQ2udyCx8-DEkYRVs")
