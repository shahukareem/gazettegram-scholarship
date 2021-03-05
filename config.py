#general config
PERSIST_DB = "persist.sqlite3"

# URL items
GAZETTE_BASE_URL = "https://www.gazette.gov.mv/"
IULAAN_SEARCH_URL = "iulaan/search/"

IULAAN_TYPES = {
    "all": "all",
    "jobs": "vazeefaa",
    "tenders": "masakkaiy",
    "training": "thamreenu",
}


# telegram config
# update channel stuff with details
TG_TOKEN = "botXXX:XXX"
TG_CHAT_ID = "@mvgazette_scholarship"
TG_URL_SEND = "https://api.telegram.org/{}/sendMessage".format(TG_TOKEN)
TG_URL_ME = "https://api.telegram.org/{}/getMe".format(TG_TOKEN)
TG_ADMIN_CHATID = 000

