# Import modules
import pandas as pd
import requests

# Collecting summoner ID
# 소환사 ID 수집
api_key = "RGAPI-ee56b8a5-02a0-42d8-84ec-fad9c0c9f0fc"
sum_name = "Hide on bush"
sum_url = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + sum_name + "?api_key=" + api_key
r_sumid = requests.get(sum_url)
acc_id = r_sumid.json()["accountId"] #Unique summoner ID

# Collect recent match data (champions used)
match_url = "https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/" + acc_id + "?api_key=" + api_key
r_match = requests.get(match_url)
champ_history = r_match.json()["matches"]
print(champ_history)