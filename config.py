import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "14411702"))
API_HASH = getenv("API_HASH", "6f8aaf5bd4f6538f06bc31ee67460f99")
BOT_TOKEN = getenv("BOT_TOKEN", "5983601762:AAFDanO3qNTw4atWbxUYbWVzCpb64XOc6gU")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://userbot:userbot@cluster0.iweqz.mongodb.net/test?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001583255537"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "『˹𝑳𝒐𝒗𝒆𝒓 ✘ ℳ𝓾𝓼𝓲c‌˼』")
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "7133633146").split()))
SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL", "https://t.me/ABOUT_LOVER_ll")
SUPPORT_GROUP = getenv(
    "SUPPORT_GROUP", "https://t.me/THE_CHATTING1_0")

DURATION_LIMIT_MIN = int(
    getenv("DURATION_LIMIT", "59006")
)

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "10998")
)

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Lover-Music/Lovermusicc",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

GIT_TOKEN = getenv("GIT_TOKEN", None)

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")

AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", "False")

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "6"))

GITHUB_REPO = getenv("GITHUB_REPO", "https://t.me/shubhamsah1")

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "5ffc4fd3cae949cf93d8b5b8ffcc9f9f")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "c2c196935b1d41c082bf981321190ea7")

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "50"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5")
)

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
STRING1 = getenv("STRING_SESSION", "BQAZyAwD0iFjrKzHwWOIFvZ7CfFrc8TzIlPbQkEE8-Ie7LZEQo5UgJlYPWEvNVtCOIymzXbJhbSBD9zvntSctT2I43uJb9R-H05MnwZKCSzQeX7r71uukjbQwwtsMDuzEaxaDZtytr9ThS0MgHslvnMhI8iAckEYb177VgNYSiqRTQhNaii5ytwWAs-uzr8LbZE67n6o7aEujTOftziCOk-R4F23_wpmngfeOmAgpUgMKz4J098txv6ttKvMSDmykcnpmpKbZQypzRHOJHNQfOpL3ZZrjNNdX-yflojiQPkbAPI6VI6RRKsG1EXUZ3qgAMmHi0QNj2fp1kRe8fluI6I5AAAAAXkyTnUA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
AMBOT = [
    "🔎",
    "🔍",
    "🧪",
    "ᴘʟꜱ ᴡᴀɪᴛ..",
    "ᴘʀᴏᴄᴇꜱꜱɪɴɢ..",
]

START_IMG_URL = getenv("START_IMG_URL", "https://graph.org/file/f234fa4e140eb1b85d185.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://graph.org/file/f234fa4e140eb1b85d185.jpg")
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = getenv("STATS_IMG_URL", "https://graph.org/file/f234fa4e140eb1b85d185.jpg")
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )
