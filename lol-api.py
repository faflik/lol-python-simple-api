import requests
import json
import time


def get_summoners_info():

    summoner_name = "japatu"
    # get api_key from https://developer.riotgames.com/
    api_key = "XXXXXXX-XXXXXXX-XXXXXX-XXXXXXX"
    # eun1, na1, jp1, la1, euw1, ru, la2, tr1, oc1, br1, kr,
    region = "eun1"

    req = "https://{}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}?api_key={}"
    url1 = req.format(region, summoner_name, api_key)
    r1 = requests.get(url1)

    dat = r1.json()['revisionDate']
    akt = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(dat/1000)))
    print("\nSummonern Name:", r1.json()['name'],
          "\nLVL: ", r1.json()['summonerLevel'],
          "\nLast activity: ", akt)

    req2 = "https://{}.api.riotgames.com/lol/champion-mastery/v4/scores/by-summoner/{}?api_key={}"
    url2 = req2.format(region, r1.json()['id'], api_key)
    r2 = requests.get(url2)
    print("Masteries ", r2.json())

    print("")


def main():
    get_summoners_info()


if __name__ == "__main__":
    main()
