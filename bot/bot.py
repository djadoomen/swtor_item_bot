import os, discord, swtor_mongo, builder
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
_TOKEN = os.getenv('DISCORD_TOKEN')
_GUILD = os.getenv('DISCORD_GUILD')
_CHANNEL = os.getenv('DISCORD_CHANNEL')

bot = commands.Bot(command_prefix='!')
guild = ''
channel = ''
amount= {}



@bot.event
async def on_ready():
    global guild
    global channel
    guild = discord.utils.get(bot.guilds, name=_GUILD)
    channel = discord.utils.get(bot.get_all_channels(), name=_CHANNEL)

    print(
    f'{bot.user.name} has connected to Discord!\n'
    f'{guild.name}(id: {guild.id})\n'
    f'{channel.name}(id: {channel.id})\n'
    )
    await channel.send('Dragi\'lous is your humble servant...')

@bot.command(name='item')
async def item_search(ctx, name_of_item: str):
    if  ctx.channel == channel:
        _description ='These are the items I found (max. 10):\nCopy and paste to search for that one item 😉\n```'
        found = swtor_mongo.search_db(name_of_item)

        for i in found:
            global amount
            amount[str(i["Name"])] = str(i["Id"])
            _description += '!item "'+(str(i['Name']) + '"\n')
        _description += '```'

        embed = discord.Embed(
            title=name_of_item,
            colour=discord.Colour.red(),
            description=_description)

        print('Amount: ' + str(len(amount)))
        for x,y in amount.items():
            print(x + " - "+ y)
        if len(amount) == 1:
            try:
                data = swtor_mongo.getOne(amount[name_of_item])
                print(amount[name_of_item])
                embed = discord.Embed(
                    title=str(data["Name"]),
                    colour=discord.Colour(int(builder.dColor(str(data["Quality"])))),
                    description='**Binds on ' + str(data["Binding"]) + '**\nDurability: **' + builder.durability(data) + '**'
                    )
                embed.set_thumbnail(url='https://swtor.donnash.nl/icn/' + data["Icon"] + '.jpg')
                embed.set_footer(text="Requires Level " + str(data["RequiredLevel"]))
                embed.add_field(name="Statistics", value= builder.stats(data), inline=True)
                embed.add_field(name="Modification Slots", value="Color Crystal: **empty**\nAugment: **empty**", inline=True)
                embed.add_field(name="Attributes", value='Quality: **' + str(data["Quality"]) + '**\nItem level : **' + str(data["ItemLevel"]) + '** \nItem rating: **' + str(data["Rating"]) + '** \nSell price: **' + str(data["Value"]) + '**', inline=False)
            except Exception as e:
                pass

        amount.clear()
        await ctx.send(content="Your search returned...", embed=embed)
bot.run(_TOKEN)
