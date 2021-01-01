# Import modules
import pandas as pd
import requests

# Collecting summoner ID
# 계정 ID 수집
api_key = "RGAPI-ee56b8a5-02a0-42d8-84ec-fad9c0c9f0fc"
sum_name = "Hide on bush"
sum_url = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + sum_name + "?api_key=" + api_key
r_sumid = requests.get(sum_url)
acc_id = r_sumid.json()["accountId"] # Unique account ID

# Collect recent match data (champions used)
# 최근 게임 전적 호출
match_url = "https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/" + acc_id + "?api_key=" + api_key
r_match = requests.get(match_url)
champ_history = r_match.json()["matches"]
print(champ_history) # Champions used on recent matches 

# Collect summoner ID for players in each league
# 각 티어별 소환사들의 소환사 ID를 수집
challenger_url = "https://kr.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/?api_key=" + api_key

r_challenger = requests.get(challenger_url)

chal_df = pd.DataFrame(r_challenger.json())

chal_df.reset_index(inplace=True)
chal_entries_df = pd.DataFrame(dict(chal_df["entries"])).T
chal_df = pd.concat([league_df, chal_entries_df], axis = 1)

chal_df = chal_df.drop(["index", "queue", "name", "leagueId", "entries", "rank"], axis = 1)
chal_df.info()
chal_df.to_csv('챌린져_데이터.csv', index = False, encoding = "cp949") # csv 파일로 중간 저장

# grandmaster_url = "https://kr.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/?api_key=" + api_key
# r_grandmaster = requests.get(grandmaster_url)
# gm_df = pd.DataFrame(r_grandmaster.json())


