import re
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)  # Optional argument, if not specified will search path.

players = ['ArtourBabaevsky', 'Kuzma is High'] #, 'EGN Rodrigues', 'Nyxer TFT', 'FTW AïM'

data = {}
df = pd.DataFrame(data, columns = ['Position','Player'])

for player in players:
    driver.get('https://lolchess.gg/profile/euw/' + player)
    print("-------------------------------------")
    print("\n")
    print(player)
    print("\n")

    player_tier = driver.find_element_by_class_name("profile__tier__summary__tier")
    player_lp = driver.find_element_by_class_name("profile__tier__summary__lp")
    print(f"Tier: {player_tier.text} - {player_lp.text}")
    #print(f"{player_lp.text}")

    player_rank_region = driver.find_element_by_class_name("rank-region")
    print(f"Rank: {player_rank_region.text}")

    player_wins = driver.find_element_by_class_name("profile__tier__wins")
    wins = [int(s) for s in player_wins.text.split() if s.isdigit()]
    print(f"Wins: {wins[0]}")

    player_top4 = driver.find_element_by_class_name("profile__tier__tops")
    top4 = [int(s) for s in player_top4.text.split() if s.isdigit()]
    print(f"Top4: {top4[0]}")

    player_played = driver.find_element_by_class_name("profile__tier__plays")
    played = [int(s) for s in player_played.text.split() if s.isdigit()]
    print(f"Played: {played[0]}")

    player_winrate = driver.find_element_by_class_name("profile__tier__winrate_10")
    #winrate = [int(s) for s in player_winrate.text.split() if s.isdigit()]
    winrate = re.findall("\d*\.?\d+",player_winrate.text)
    print(f"Win Rate: {winrate[0]}%")

    player_toprate = driver.find_element_by_class_name("profile__tier__toprate")
    #toprate = [int(s) for s in player_toprate.text.split() if s.isdigit()]
    toprate = re.findall("\d*\.?\d+",player_toprate.text)
    print(f"Top4 Rate: {toprate[1]}%")

    player_avg_rank = driver.find_element_by_class_name("profile__tier__avg_rank")
    #avg_rank = [int(s) for s in player_avg_rank.text.split() if s.isdigit()]
    avg_rank = re.findall("\d*\.?\d+",player_avg_rank.text)
    print(f"Avg. Rank: #{avg_rank[0]}")

    position_player = player_rank_region.text.replace("#", "")

    #positions.update({player, position_player}) 

    print(f"{position_player}, {player}")

    
    time.sleep(5) # Let the user actually see something!

#print(positions)

print("-------------------------------------")
print("\n")
print(df)

driver.quit() 
