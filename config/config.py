import os

# ============================================================
# SECRETS — កំណត់ទាំងនេះជា environment variables ក្នុង Railway
# កុំសរសេរ tokens ផ្ទាល់ក្នុងកូដនេះឱ្យសោះ!
# ============================================================
BOT_TOKEN: str = os.environ.get("BOT_TOKEN", "")
SPOTIFY_ID: str = os.environ.get("SPOTIFY_ID", "")
SPOTIFY_SECRET: str = os.environ.get("SPOTIFY_SECRET", "")

BOT_PREFIX = os.environ.get("BOT_PREFIX", "$")

EMBED_COLOR = 0x4dd4d0

SUPPORTED_EXTENSIONS = ('.webm', '.mp4', '.mp3', '.avi', '.wav', '.m4v', '.ogg', '.mov')

MAX_SONG_PRELOAD = 5  # អតិបរមា ២៥

COOKIE_PATH = "/config/cookies/cookies.txt"

GLOBAL_DISABLE_AUTOJOIN_VC = False

VC_TIMEOUT = 600  # វិនាទី
VC_TIMOUT_DEFAULT = True
ALLOW_VC_TIMEOUT_EDIT = True

STARTUP_MESSAGE = "កំពុងចាប់ផ្តើម Bot..."
STARTUP_COMPLETE_MESSAGE = "ការចាប់ផ្តើមបានជោគជ័យ"

NO_GUILD_MESSAGE = 'កំហុស៖ សូមចូលទៅក្នុងប៉ុស្តិ៍សំឡេង (Voice Channel) ឬបញ្ចូលពាក្យបញ្ជាក្នុងឆាតក្រុម'
USER_NOT_IN_VC_MESSAGE = "កំហុស៖ សូមចូលទៅក្នុងប៉ុស្តិ៍សំឡេងដែលកំពុងសកម្ម ដើម្បីប្រើប្រាស់ពាក្យបញ្ជា"
WRONG_CHANNEL_MESSAGE = "កំហុស៖ សូមប្រើប្រាស់ប៉ុស្តិ៍បញ្ជាដែលបានកំណត់"
NOT_CONNECTED_MESSAGE = "កំហុស៖ Bot មិនទាន់បានភ្ជាប់ទៅកាន់ប៉ុស្តិ៍សំឡេងណាមួយឡើយ"
ALREADY_CONNECTED_MESSAGE = "កំហុស៖ បានភ្ជាប់ទៅកាន់ប៉ុស្តិ៍សំឡេងរួចរាល់ហើយ"
CHANNEL_NOT_FOUND_MESSAGE = "កំហុស៖ រកមិនឃើញប៉ុស្តិ៍សំឡេងទេ"
DEFAULT_CHANNEL_JOIN_FAILED = "កំហុស៖ មិនអាចចូលទៅកាន់ប៉ុស្តិ៍សំឡេងលំនាំដើមបានទេ"
INVALID_INVITE_MESSAGE = "កំហុស៖ តំណភ្ជាប់ការអញ្ជើញមិនត្រឹមត្រូវ"

ADD_MESSAGE = "ដើម្បីបន្ថែម Bot នេះទៅកាន់ម៉ាស៊ីនបម្រើ (Server) របស់អ្នក សូមចុច [ទីនេះ]"

INFO_HISTORY_TITLE = "បទចម្រៀងដែលបានចាក់៖"
MAX_HISTORY_LENGTH = 10
MAX_TRACKNAME_HISTORY_LENGTH = 15

SONGINFO_UPLOADER = "អ្នកបង្ហោះ៖ "
SONGINFO_DURATION = "រយៈពេល៖ "
SONGINFO_SECONDS = "វិនាទី"
SONGINFO_LIKES = "ការចូលចិត្ត៖ "
SONGINFO_DISLIKES = "ការមិនចូលចិត្ត៖ "
SONGINFO_NOW_PLAYING = "កំពុងចាក់"
SONGINFO_QUEUE_ADDED = "បានបន្ថែមទៅក្នុងជួរចាក់ (Queue)"
SONGINFO_SONGINFO = "ព័ត៌មានបទចម្រៀង"
SONGINFO_ERROR = "កំហុស៖ គេហទំព័រមិនគាំទ្រ ឬមាតិកាត្រូវបានរឹតត្បិតអាយុ។"
SONGINFO_PLAYLIST_QUEUED = "បានបន្ថែមបញ្ជីចាក់ (Playlist) ទៅក្នុងជួររួចរាល់ :page_with_curl:"
SONGINFO_UNKNOWN_DURATION = "មិនស្គាល់"

HELP_ADDBOT_SHORT = "បន្ថែម Bot ទៅម៉ាស៊ីនបម្រើផ្សេងទៀត"
HELP_ADDBOT_LONG = "ផ្តល់ឱ្យអ្នកនូវតំណភ្ជាប់សម្រាប់បន្ថែម Bot នេះទៅកាន់ម៉ាស៊ីនបម្រើផ្សេងទៀតរបស់អ្នក។"
HELP_CONNECT_SHORT = "ភ្ជាប់ Bot ទៅកាន់ប៉ុស្តិ៍សំឡេង"
HELP_CONNECT_LONG = "ភ្ជាប់ Bot ទៅកាន់ប៉ុស្តិ៍សំឡេងដែលអ្នកកំពុងស្ថិតនៅ"
HELP_DISCONNECT_SHORT = "ផ្តាច់ Bot ពីប៉ុស្តិ៍សំឡេង"
HELP_DISCONNECT_LONG = "ផ្តាច់ Bot ពីប៉ុស្តិ៍សំឡេង និងបញ្ឈប់ការចាក់សំឡេង។"
HELP_SETTINGS_SHORT = "មើល និងកំណត់ការកំណត់របស់ Bot"
HELP_SETTINGS_LONG = "មើល និងកំណត់ការកំណត់របស់ Bot នៅក្នុងម៉ាស៊ីនបម្រើ។ ការប្រើប្រាស់៖ {}settings ឈ្មោះ_ការកំណត់ តម្លៃ".format(BOT_PREFIX)
HELP_HISTORY_SHORT = "បង្ហាញប្រវត្តិនៃបទចម្រៀង"
HELP_HISTORY_LONG = "បង្ហាញបទចម្រៀងចំនួន " + str(MAX_TRACKNAME_HISTORY_LENGTH) + " បទចុងក្រោយដែលបានចាក់។"
HELP_PAUSE_SHORT = "ផ្អាកតន្ត្រី"
HELP_PAUSE_LONG = "ផ្អាកការចាក់សំឡេង។ អាចបន្តការចាក់ឡើងវិញបានដោយប្រើពាក្យបញ្ជា resume។"
HELP_VOL_SHORT = "ផ្លាស់ប្តូរកម្រិតសំឡេង %"
HELP_VOL_LONG = "ផ្លាស់ប្តូរកម្រិតសំឡេងនៃការចាក់សំឡេង។"
HELP_PREV_SHORT = "ត្រឡប់ទៅបទមុន"
HELP_PREV_LONG = "ចាក់បទចម្រៀងមុនម្តងទៀត។"
HELP_RESUME_SHORT = "បន្តចាក់តន្ត្រី"
HELP_RESUME_LONG = "បន្តការចាក់សំឡេងឡើងវិញ។"
HELP_SKIP_SHORT = "រំលងបទចម្រៀង"
HELP_SKIP_LONG = "រំលងបទចម្រៀងដែលកំពុងចាក់ ហើយទៅកាន់បទបន្ទាប់នៅក្នុងជួរ។"
HELP_SONGINFO_SHORT = "ព័ត៌មានអំពីបទចម្រៀងបច្ចុប្បន្ន"
HELP_SONGINFO_LONG = "បង្ហាញព័ត៌មានលម្អិតអំពីបទចម្រៀងដែលកំពុងត្រូវបានចាក់។"
HELP_STOP_SHORT = "បញ្ឈប់តន្ត្រី"
HELP_STOP_LONG = "បញ្ឈប់ការចាក់សំឡេង និងសម្អាតជួរបទចម្រៀងទាំងអស់"
HELP_MOVE_LONG = f"{BOT_PREFIX}move [ទីតាំងចាស់] [ទីតាំងថ្មី]"
HELP_MOVE_SHORT = 'ផ្លាស់ប្តូរលំដាប់បទចម្រៀងក្នុងជួរ'
HELP_YT_SHORT = "ចាក់តំណភ្ជាប់ដែលគាំទ្រ ឬស្វែងរកលើ YouTube"
HELP_YT_LONG = "$p [តំណភ្ជាប់/ចំណងជើងវីដេអូ/ពាក្យគន្លឹះ/playlist/soundcloud/spotify/bandcamp]"
HELP_PING_SHORT = "Pong (ពិនិត្យល្បឿន)"
HELP_PING_LONG = "សាកល្បងស្ថានភាពឆ្លើយតបរបស់ Bot"
HELP_CLEAR_SHORT = "សម្អាតជួរបទចម្រៀង"
HELP_CLEAR_LONG = "សម្អាតជួរបទចម្រៀង និងរំលងបទដែលកំពុងចាក់បច្ចុប្បន្ន។"
HELP_LOOP_SHORT = "ចាក់បទដដែលឡើងវិញ (បើក/បិទ)"
HELP_LOOP_LONG = "ចាក់បទចម្រៀងដែលកំពុងចាក់ឡើងវិញ និងចាក់សោជួរចាក់។"
HELP_QUEUE_SHORT = "បង្ហាញបទចម្រៀងក្នុងជួរ"
HELP_QUEUE_LONG = "បង្ហាញចំនួនបទចម្រៀងក្នុងជួរ រហូតដល់ ១០ បទ។"
HELP_SHUFFLE_SHORT = "ច្របល់ជួរបទចម្រៀង"
HELP_SHUFFLE_LONG = "រៀបលំដាប់បទចម្រៀងក្នុងជួរឡើងវិញដោយចៃដន្យ"
HELP_CHANGECHANNEL_SHORT = "ប្តូរប៉ុស្តិ៍ Bot"
HELP_CHANGECHANNEL_LONG = "ប្តូរប៉ុស្តិ៍ Bot ទៅកាន់ប៉ុស្តិ៍សំឡេងដែលអ្នកកំពុងស្ថិតនៅ"

ABSOLUTE_PATH = ''
