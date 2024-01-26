import configparser

import discord
from discord.ext import commands
from discord.ui import View, Button

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
channel_ava = None
channel_chat = None
channel_for_news = None
ava_id = 0


@bot.command()
async def helper(ctx):
    embed = discord.Embed(title="Список команд", description="Список доступных команд бота", color=discord.Color.blue())
    embed.add_field(name="!post", value="Создаёт пост от имени бота", inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def settings(ctx):
    embed = discord.Embed(title="Настройка", description=" Список доступных комманд для настройки",
                          color=discord.Color.red())
    embed.add_field(name="!post", value="Создаёт пост от имени бота", inline=False)
    view = View(timeout=None)
    embed.add_field(name="Каналы", value="Изменить каналы", inline=False)
    button1 = Button(label="!post", style=discord.ButtonStyle.green)
    view.add_item(button1)
    button2 = Button(label="Каналы", style=discord.ButtonStyle.green)
    view.add_item(button2)

    async def button_callback1(interaction):
        guild = bot.get_guild(interaction.guild_id)
        embed1 = discord.Embed(title="!post", description="")
        await interaction.response.send_message(embed=embed1)

    async def button_callback2(interaction):
        guild = bot.get_guild(interaction.guild_id)
        embed2 = discord.Embed(title="Каналы")
        embed2.add_field(name="Новостной канал", value="", inline=False)
        embed2.add_field(name="Канал уведомлений", value="", inline=False)
        await interaction.response.send_message(embed=embed2)

    button1.callback = button_callback1
    button2.callback = button_callback2
    await ctx.send(embed=embed, view=view)


@bot.event
async def on_ready():
    global channel_ava
    global channel_for_news
    global channel_chat
    global ava_id
    ch_ava = int(config["Guild"]["ch_ava"])
    news = int(config["Guild"]["news"])
    chat = int(config["Guild"]["chat"])
    channel_ava = bot.get_channel(ch_ava)
    channel_for_news = bot.get_channel(news)
    channel_chat = bot.get_channel(chat)
    ava_id = int(config["Guild"]["ava_id"])
    return channel_chat, channel_ava, channel_for_news, ava_id


@bot.event
async def on_member_remove(member):
    message = '***Пока пока*** :( ' + member.mention
    await channel_chat.send(message)


@bot.event
async def on_raw_reaction_add(payload):
    channel = bot.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    guild = bot.get_guild(payload.guild_id)
    reaction = discord.utils.get(message.reactions, emoji=payload.emoji.name)
    # only work if it is the client
    if payload.member.id == bot.user.id:
        return

    # verification
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

    async def verification():
        member = payload.member
        if payload.emoji.name == '✅':
            num = [1038199925189640323, 1037845308517924885, 1037845381188435969, 1038199922379464776,
                   1038213629318799360,
                   1038464914718724248]
            for draw in range(len(num)):
                await payload.member.add_roles(discord.utils.get(guild.roles, id=num[draw]))
            await reaction.remove(user=payload.member)
            message_to_hi = '***Привет привет, добро пожаловать в наши ряды!*** ' + member.mention
            await channel_chat.send(message_to_hi)

    match payload.message_id:
        case 1038519665040838677:
            await verification()
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
async def post(ctx, *args):
    i = 0
    view = View(timeout=None)
    z = ctx.message.content
    user_role = ctx.author.top_role.id
    index_start_for_web = 1000000000
    if user_role == 1037854733458735216:
        if args.count('Кнопки:'):
            # url = None
            # if args.count('Ссылка:'):
            #     index_start_for_web = args.index('Ссылка:')
            #     index = z.index('Ссылка:')
            #     url = str(args[index_start_for_web + 1])
            #     z = z[:index]
            i = 1
            index = args.index('Кнопки:')
            message = args[index + 1: index_start_for_web]
            index_start = z.index('Кнопки:')
            # index_for_callback = message.index('Текст:')
            z = z[:index_start]
            for cake in range(0, len(message), 4):
                exec(f"button{cake} = Button(label=message[cake], style=discord.ButtonStyle.grey, emoji=message[cake "
                     f"+ 2])")
                exec(f"view.add_item(button{cake})")

                async def button_callback(interaction):
                    guild = bot.get_guild(interaction.guild_id)
                    # await interaction.user.add_roles(discord.utils.get(guild.roles, id=int(message[cake + 3])))
                    await interaction.response.send_message('Поздравляю! Теперь ты часть гильдии <3' + interaction.user.
                                                            mention)

                exec(f"button{cake}.callback = button_callback")

        embed = discord.Embed(description=z[6:100000000000], color=0xe6e6fa)
        url = ('https://media.discordapp.net/attachments/1038149636126425118/1160935185450287164/iiiko.png?ex=65367825'
               '&is=65240325&hm=5e0f6029fbcf7a2903f2f70c3569f4ef2be46971ce650cc37de49ac084f46bd9&=&width=612&height'
               '=612')
        embed.set_thumbnail(url=url)
        if len(ctx.message.attachments) > 0:
            for sex in range(len(ctx.message.attachments)):
                y = ctx.message.attachments[sex].url
                embed.set_image(url=y)

        if i == 0:
            await ctx.send(embed=embed)
            await ctx.message.delete()
        else:
            await ctx.send(view=view, embed=embed)
            view.clear_items()
            await ctx.message.delete()

    else:
        embed = discord.Embed(description='Товарищь, у тебя нет прав на эту команду :(', color=0xe6e6fa)
        await ctx.send(embed=embed)
        await ctx.message.delete()


# @bot.event
# async def on_presence_update(before, after):
#     print(0)
#     if after.id == ava_id:
#         print(1)
#         if isinstance(before.activity, discord.activity.Streaming):
#             print(4)
#             await channel_ava.send('Стрим закончился, всем спасибо, что пришли!')
#         if isinstance(after.activity, discord.activity.Streaming):
#             print(2)
#             if after.activity.twitch_name is not None:
#                 print(3)
#                 twitch_link = after.activity.url
#                 await channel_ava.send(
#                     'Лидер запустила стрим! Скорее сюда: ' + twitch_link + 'Не забудьте печеньки с чаем!')
#         if isinstance(after.activity, discord.activity.Game):
#             print(1)
#             print(channel_ava)
#             await channel_ava.send('Лидер играет в ' + after.activity.name + '. Присоединяйтесь!')


# CheckList:
# View for !post and public settings
# Add realization more than 1 pic in post command
# Guilds ( text )
# Twitch.tv alert ( needs to test )

config = configparser.ConfigParser()
config.read("settings.ini")
token = config["Bot"]["BOT_TOKEN"]
bot.run(token)
