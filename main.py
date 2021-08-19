import discord, os
from discord.ext import commands
from discord_components import DiscordComponents


intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix='!', intents=intents)
client.remove_command('help')


@client.event
async def on_ready():
    DiscordComponents(client)
    print(f'Launched: {client.user.name} // {client.user.id}')


for filename in os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cogs')):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f'Loaded: cog.{filename[:-3]}')




client.run('YOUR BOT TOKEN')