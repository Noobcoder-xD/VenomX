
from os import getenv

from dotenv import load_dotenv

load_dotenv("config.env")


API_HASH = getenv("API_HASH", "ef7435f8daa6bfe1611eb01f7e0a4778")
API_ID = int(getenv("API_ID", "28037022"))
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001649838443]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID", "-1001959134296") or 0)
BOT_VER = "0.1.0@main"
BRANCH = getenv("BRANCH", "main")
CHANNEL = getenv("CHANNEL", "VenomOwners")
CMD_HANDLER = getenv("CMD_HANDLER", ".")
DB_URL = getenv("DATABASE_URL", "mongodb+srv://developervro:developerrapuka@cluster9.gcj9754.mongodb.net/?retryWrites=true&w=majority&appName=Cluster9")
GIT_TOKEN = getenv("GIT_TOKEN", "")
GROUP = getenv("GROUP", "Venom_Chatz")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
PMPERMIT_PIC = getenv("PMPERMIT_PIC", "https://te.legra.ph/file/0b373de1c657129297c39.jpg")
REPO_URL = getenv("REPO_URL", "https://github.com/venombolteop/VenomX")
STRING_SESSION1 = getenv("STRING_SESSION1", "BQHBxJYAET5o0twQ0SkaRCWzylcP8jflfStXtDtDiP1FP9deC-CW6fDsFUhKXh2RaDWMqz0uzwveCC04P3DnC-co48BfSsouxbtDLrEdsCajkDFOfVzjb2dr7zXNQskrAKYoJaiIG3VSHUTVKibeioH42fSEKao4UIV9LhzeDqAlKh2ZHUcDRV_Leayela8fIDAmNkD6G3BW3pkDwsabtrKpl81Pb2OyHNacI55PvsPWhEc_tsw25bLAk0iDjSPfZb1RGU0Lor1t0nuzWOPZKzWSXL2DbhcYtk48Zc6KMYo34UUhXrspSLdOT0hYbZtoHxLJRzjKDbwySoInGYUD8WuQ1SNVVAAAAAGksOwYAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5822700831").split()))
