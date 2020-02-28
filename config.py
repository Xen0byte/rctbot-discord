import os
import platform
import json

#Heroku
if 'DYNO' in os.environ:
    HEROKU_DEPLOYED = True
else:
    HEROKU_DEPLOYED = False

# load local config, platform for dev purposes
if 'Windows' in platform.system():
    CONFIG_FILE = 'dev_config.json'
else:
    CONFIG_FILE = 'config.json'

if os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE) as CONFIG:
        CONFIG = json.load(CONFIG)
        try:
            CONFIG_DISCORD = CONFIG['DISCORD']
            CONFIG_HON = CONFIG['HON']
            CONFIG_GOOGLE = CONFIG['GOOGLE']
            
            if HEROKU_DEPLOYED:
                CONFIG_HEROKU = CONFIG['HEROKU']
                HEROKU_APP_NAME = CONFIG_HEROKU['APP_NAME'] # TO DO: finish this and clean up
        except:
            raise Exception('Invalid configuration file or missing keys.')
else:
    raise Exception(f'Missing configuration file {CONFIG_FILE} in directory.')

#Discord
DISCORD_TOKEN = CONFIG_DISCORD['TOKEN']
DISCORD_NOTES_CHANNEL_ID = CONFIG_DISCORD['NOTES_CHANNEL_ID']
DISCORD_ANNOUNCEMENTS_CHANNEL_ID = CONFIG_DISCORD['ANNOUNCEMENTS_CHANNEL_ID']
DISCORD_FORUMS_ROLE_ID = CONFIG_DISCORD['FORUMS_ROLE_ID']
DISCORD_BUGS_CHANNEL_ID = CONFIG_DISCORD['BUGS_CHANNEL_ID']
DISCORD_BOT_LOG_CHANNEL_ID = CONFIG_DISCORD['BOT_LOG_CHANNEL_ID']
DISCORD_WHITELIST_IDS = CONFIG_DISCORD['WHITELIST_IDS']

DISCORD_DM_COMMANDS = ['report', 'notes'] #TO DO: replace with a decorator (guild_only and dm_allowed)

#Heroes of Newerth
HON_USER_AGENT = CONFIG_HON['USER_AGENT']
HON_NAEU_MASTERSERVER = CONFIG_HON['NAEU_MASTERSERVER']
HON_NAEU_RC_MASTERSERVER = CONFIG_HON['NAEU_RC_MASTERSERVER']
HON_NAEU_TC_MASTERSERVER = CONFIG_HON['NAEU_TC_MASTERSERVER']
HON_NAEU_RC_OS_PART = CONFIG_HON['NAEU_RC_OS_PART']
HON_NAEU_TC_OS_PART = CONFIG_HON['NAEU_TC_OS_PART']
HON_REGION = CONFIG_HON['REGION']
HON_s2_n = CONFIG_HON['s2_n']
HON_s2_g = CONFIG_HON['s2_g']
HON_ALT_DOMAIN = CONFIG_HON['ALT_DOMAIN']
HON_CAT_PASSWORD = CONFIG_HON['CAT_PASSWORD']
HON_FORUM_USER = CONFIG_HON['FORUM_USER']
HON_FORUM_USER_MD5_PASSWORD = CONFIG_HON['FORUM_USER_MD5_PASSWORD']
HON_FORUM_USER_ACCOUNT_ID = CONFIG_HON['FORUM_USER_ACCOUNT_ID']
HON_FORUM_ANNOUNCEMENTS_THREAD_ID = CONFIG_HON['FORUM_ANNOUNCEMENTS_THREAD_ID']
HON_FORUM_RCT_BUGS_SUBFORUM_ID = CONFIG_HON['FORUM_RCT_BUGS_SUBFORUM_ID']
HON_FORUM_CREATE_ALL_THREADS = CONFIG_HON['FORUM_CREATE_ALL_THREADS']
HON_FORUM_SCREENSHOT_LIMIT = CONFIG_HON['FORUM_SCREENSHOT_LIMIT']

#Google
GOOGLE_CLIENT_SECRET_FILE = CONFIG_GOOGLE['CLIENT_SECRET_FILE']
GOOGLE_SCOPES = CONFIG_GOOGLE['SCOPES']