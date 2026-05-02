import discord
from config import config
from discord.ext import commands
from discord.ext.commands import has_permissions
from musicbot import utils
from musicbot.audiocontroller import AudioController
from musicbot.utils import guild_to_audiocontroller, guild_to_settings


class General(commands.Cog):
    """ បណ្តុំនៃពាក្យបញ្ជា (Commands) សម្រាប់បញ្ជា Bot នៅក្នុង Server របស់អ្នក។

            លក្ខណៈសម្បត្តិ (Attributes):
                bot: ឧទាហរណ៍នៃ bot ដែលកំពុងអនុវត្តពាក្យបញ្ជា។
    """

    def __init__(self, bot):
        self.bot = bot

    # តក្កវិជ្ជាត្រូវបានបំបែកទៅជា uconnect() សម្រាប់ការប្រើប្រាស់ទូទៅ
    @commands.command(name='connect', description=config.HELP_CONNECT_LONG, help=config.HELP_CONNECT_SHORT, aliases=['c'])
    async def _connect(self, ctx):  # ឈ្មោះ channel គោលដៅ: str
        current_guild = utils.get_guild(self.bot, ctx.message)
        audiocontroller = utils.guild_to_audiocontroller[current_guild]
        await audiocontroller.uconnect(ctx)

    @commands.command(name='disconnect', description=config.HELP_DISCONNECT_LONG, help=config.HELP_DISCONNECT_SHORT, aliases=['dc'])
    async def _disconnect(self, ctx, guild=False):
        current_guild = utils.get_guild(self.bot, ctx.message)
        audiocontroller = utils.guild_to_audiocontroller[current_guild]
        await audiocontroller.udisconnect()

    @commands.command(name='reset', description=config.HELP_DISCONNECT_LONG, help=config.HELP_DISCONNECT_SHORT, aliases=['rs', 'restart'])
    async def _reset(self, ctx):
        current_guild = utils.get_guild(self.bot, ctx.message)

        if current_guild is None:
            await ctx.send(config.NO_GUILD_MESSAGE)
            return
        await utils.guild_to_audiocontroller[current_guild].stop_player()
        await current_guild.voice_client.disconnect(force=True)

        guild_to_audiocontroller[current_guild] = AudioController(
            self.bot, current_guild)
        await guild_to_audiocontroller[current_guild].register_voice_channel(ctx.author.voice.channel)

        await ctx.send("{} បានភ្ជាប់ទៅកាន់ {}".format(":white_check_mark:", ctx.author.voice.channel.name))

    @commands.command(name='changechannel', description=config.HELP_CHANGECHANNEL_LONG, help=config.HELP_CHANGECHANNEL_SHORT, aliases=['cc'])
    async def _change_channel(self, ctx):
        current_guild = utils.get_guild(self.bot, ctx.message)

        vchannel = await utils.is_connected(ctx)
        if vchannel == ctx.author.voice.channel:
            await ctx.send("{} បានភ្ជាប់ទៅកាន់ {} រួចរាល់ហើយ".format(":white_check_mark:", vchannel.name))
            return

        if current_guild is None:
            await ctx.send(config.NO_GUILD_MESSAGE)
            return
        await utils.guild_to_audiocontroller[current_guild].stop_player()
        await current_guild.voice_client.disconnect(force=True)

        guild_to_audiocontroller[current_guild] = AudioController(
            self.bot, current_guild)
        await guild_to_audiocontroller[current_guild].register_voice_channel(ctx.author.voice.channel)

        await ctx.send("{} បានប្តូរទៅកាន់ {}".format(":white_check_mark:", ctx.author.voice.channel.name))

    @commands.command(name='ping', description=config.HELP_PING_LONG, help=config.HELP_PING_SHORT)
    async def _ping(self, ctx):
        await ctx.send("Pong (កំពុងដំណើរការ)")

    @commands.command(name='setting', description=config.HELP_SHUFFLE_LONG, help=config.HELP_SETTINGS_SHORT, aliases=['settings', 'set'])
    @has_permissions(administrator=True)
    async def _settings(self, ctx, *args):

        sett = guild_to_settings[ctx.guild]

        if len(args) == 0:
            await ctx.send(embed=await sett.format())
            return

        args_list = list(args)
        args_list.remove(args[0])

        response = await sett.write(args[0], " ".join(args_list), ctx)

        if response is None:
            await ctx.send("`កំហុស: រកមិនឃើញការកំណត់ (Setting)`")
        elif response is True:
            await ctx.send("ការកំណត់ត្រូវបានធ្វើបច្ចុប្បន្នភាព!")

    @commands.command(name='addbot', description=config.HELP_ADDBOT_LONG, help=config.HELP_ADDBOT_SHORT)
    async def _addbot(self, ctx):
        embed = discord.Embed(title="អញ្ជើញ Bot", description=config.ADD_MESSAGE +
                              "(https://discordapp.com/oauth2/authorize?client_id={}&scope=bot>)".format(self.bot.user.id))

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(General(bot))
