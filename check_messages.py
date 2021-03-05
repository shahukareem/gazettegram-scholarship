import config_private as config
import requests

def get_updates():
    r = requests.post(f"https://api.telegram.org/{config.TG_TOKEN}/getUpdates")
    return r.json()


if __name__ == "__main__":
   print(get_updates())