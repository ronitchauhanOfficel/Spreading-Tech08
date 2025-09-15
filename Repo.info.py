Repo.info py 

import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['23990215'])
API_HASH = environ['905c0a26b0a16257c909587314a5df83']
BOT_TOKEN = environ['8400559379:AAH5BWNo-pdrj0Uc2dpj4vF_bzKPT4JdEe0']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://telegra.ph/file/7e56d907542396289fee4.jpg https://telegra.ph/file/9aa8dd372f4739fe02d85.jpg https://telegra.ph/file/adffc5ce502f5578e2806.jpg https://telegra.ph/file/6937b60bc2617597b92fd.jpg https://telegra.ph/file/09a7abaab340143f9c7e7.jpg https://telegra.ph/file/5a82c4a59bd04d415af1c.jpg https://telegra.ph/file/323986d3bd9c4c1b3cb26.jpg https://telegra.ph/file/b8a82dcb89fb296f92ca0.jpg https://telegra.ph/file/31adab039a85ed88e22b0.jpg https://telegra.ph/file/c0e0f4c3ed53ac8438f34.jpg https://telegra.ph/file/eede835fb3c37e07c9cee.jpg https://telegra.ph/file/e17d2d068f71a9867d554.jpg https://telegra.ph/file/8fb1ae7d995e8735a7c25.jpg https://telegra.ph/file/8fed19586b4aa019ec215.jpg https://telegra.ph/file/8e6c923abd6139083e1de.jpg https://telegra.ph/file/0049d801d29e83d68b001.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(spreadingtech) if id_pattern.search(spreadingtech) else admin for admin in environ.get('SPREADING_TECH', '').split()]
CHANNELS = [int(https://t.me/movie_requast_channel06) if id_pattern.search(https://t.me/movie_requast_channel06) else ch for ch in environ.get('Bollywood_Hollywood_webseries_ movie', '0').split()]
auth_users = [int(https://t.me/spreadingtechofficel) if id_pattern.search(https://t.me/spreadingtechofficel) else user for user in environ.get('SPREADING_TECH', '').split()]
AUTH_USERS = (https://t.me/spreadingtechofficel + SPREADING_TECH) if auth_users else []
auth_channel = environ.get('https://t.me/movie_requast_channel06')
auth_grp = environ.get('https://t.me/gorupsupport_chat')
AUTH_CHANNEL = int(https://t.me/movie_requast_channel06) if auth_channel and id_pattern.search(https://t.me/movie_requast_channel06) else None
AUTH_GROUPS = [int(https://t.me/gorupsupport_chat) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('arun', "arun")
DATABASE_NAME = environ.get('arun', "arun")
COLLECTION_NAME = environ.get('referalmoney', 'Telegram_files')

# Others
LOG_CHANNEL = int(environ.get('https://t.me/Movie_Log_channel06', 0))
SUPPORT_CHAT = environ.get('https://t.me/gorupsupport_chat', 'spreadingtech')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "False")), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "⚡<b>File uploaded by [Bollywood_Hollywood_webseries_ movie ™](https://t.me/Hindi_movie_channel_06)</b>⚡\n\n🎦 <b>File Name: </b> ➥  <i>{file_caption}</i>\n⚙️ <b>Size: </b><i>{file_size}</i>\n\n                ❤️<b>WE LOVE YOU</b>❤️\n🔥  ↭ <b>Join Now [Spreading Tech 😎™](https://t.me/spreadingtechofficel)</b> ↭  🔥")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Your Query: {query}</b> \n‌‌‌‌IMDb Data by: @spreadingtech08 \n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10 \n\n♥️ we are nothing without you ♥️ \n\n💛 Please Share Us 💛\n\n⚠️Click on the button 👇 below to get your query privately")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), False)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('https://t.me/movie_requast_channel06', https://t.me/Movie_Log_channel06))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('https://t.me/Hindi_movie_channel_06', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "True")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('https://t.me/Hindi_movie_channel_06', "False")), False)

#spreading_tech Configs
FLOOD = int(environ.get("FLOOD", "10"))
SPREADING_MODE = bool(environ.get("SPREADING_MODE"))
#Add user id of the user in this field those who you want to be Authentic user for file renaming features
spreading_tech = [int(spreadingtech) if id_pattern.search(spreadingtech) else spreadingtech for spreadingtech in environ.get('SPREADING_TECH', '').split()]
SPREADING_TECH= (spreading_tech+ ADMINS) if spreading_tech else []
REQ_CHANNEL = int(environ.get('https://t.me/movie_requast_channel06'))

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

