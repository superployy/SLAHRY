import discord
from discord.ext import commands
from musicbot import linkutils, utils


class Button(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        # FIX: guard against DMs (no guild)
        if message.guild is None:
            return
        if message.author == self.bot.user:
            return

        sett = utils.guild_to_settings.get(message.guild)
        if sett is None:
            return

        button_name = sett.get('button_emote')
        if not button_name:
            return

        host = linkutils.identify_url(message.content)
        guild = message.guild
        emoji = discord.utils.get(guild.emojis, name=button_name)

        if host in (linkutils.Sites.YouTube, linkutils.Sites.Spotify, linkutils.Sites.Spotify_Playlist):
            if emoji:
                await message.add_reaction(emoji)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, reaction):
        serv = self.bot.get_guild(reaction.guild_id)
        if serv is None:
            return

        sett = utils.guild_to_settings.get(serv)
        if sett is None:
            return

        button_name = sett.get('button_emote')
        if not button_name:
            return

        if reaction.emoji.name != button_name:
            return

        # FIX: was Sites.Spotify.Spotify_Playlist (wrong attribute access)
        channels = serv.text_channels
        message = None

        for chan in channels:
            if chan.id == reaction.channel_id:
                if reaction.member == self.bot.user:
                    return

                try:
                    if reaction.member.voice.channel is None:
                        return
                except Exception:
                    msg = await chan.fetch_message(reaction.message_id)
                    await msg.remove_reaction(reaction.emoji, reaction.member)
                    return

                message = await chan.fetch_message(reaction.message_id)
                await message.remove_reaction(reaction.emoji, reaction.member)
                break

        if message is None:
            return

        current_guild = utils.get_guild(self.bot, message)
        if current_guild is None:
            return

        audiocontroller = utils.guild_to_audiocontroller.get(current_guild)
        if audiocontroller is None:
            return

        url = linkutils.get_url(message.content)
        host = linkutils.identify_url(url)

        if host in (linkutils.Sites.Spotify, linkutils.Sites.Spotify_Playlist, linkutils.Sites.YouTube):
            await audiocontroller.process_song(url)


def setup(bot):
    bot.add_cog(Button(bot))
