import asyncio
import os
import sys
from dotenv import load_dotenv
load_dotenv()

import discord
from discord.ext import commands

# Fix import path so 'config' package is always found
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import config
from musicbot import utils
from musicbot.utils import guild_to_audiocontroller, guild_to_settings

initial_extensions = [
    'musicbot.commands.music',
    'musicbot.commands.general',
    'musicbot.plugins.button',
]

# py-cord uses discord.Bot / commands.Bot; intents required for modern Discord
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
intents.guilds = True
intents.members = True

bot = commands.Bot(
    command_prefix=config.BOT_PREFIX,
    case_insensitive=True,
    intents=intents,
)


async def register(guild):
    await utils.register(bot, guild)

    sett = guild_to_settings[guild]

    try:
        await guild.me.edit(nick=sett.get('default_nickname'))
    except Exception:
        pass

    if config.GLOBAL_DISABLE_AUTOJOIN_VC:
        return

    vc_channels = guild.voice_channels

    if sett.get('vc_timeout') == False:
        if sett.get('start_voice_channel') is None:
            try:
                await guild_to_audiocontroller[guild].register_voice_channel(guild.voice_channels[0])
            except Exception as e:
                print(e)
        else:
            for vc in vc_channels:
                if vc.id == sett.get('start_voice_channel'):
                    try:
                        await guild_to_audiocontroller[guild].register_voice_channel(vc)
                    except Exception as e:
                        print(e)


@bot.event
async def on_ready():
    print(config.STARTUP_MESSAGE)
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Game(name="Music, type {}help".format(config.BOT_PREFIX))
    )
    for guild in bot.guilds:
        await register(guild)
        print("Joined {}".format(guild.name))
    print(config.STARTUP_COMPLETE_MESSAGE)


@bot.event
async def on_guild_join(guild):
    print(guild.name)
    await register(guild)


def main():
    config.ABSOLUTE_PATH = os.path.dirname(os.path.abspath(__file__))
    config.COOKIE_PATH = config.ABSOLUTE_PATH + config.COOKIE_PATH

    if not config.BOT_TOKEN:
        print("Error: No bot token! Set the BOT_TOKEN environment variable.")
        sys.exit(1)

    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f"Failed to load extension {extension}: {e}")

    bot.run(config.BOT_TOKEN, reconnect=True)


if __name__ == '__main__':
    main()
