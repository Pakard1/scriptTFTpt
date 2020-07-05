import re
import time
import pandas as pd
import imageio
from imageio import imread
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from tabulate import tabulate
from numpy import genfromtxt
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import table 


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)  # Optional argument, if not specified will search path.

players = ['ArtourBabaevsky', 'EGN Rodrigues', 'Nyxer TFT', 'FTW AïM', 'Kuzma is High', 'Kilnae', 'Jitonce', 'Batata', 'EGN Renygp xD',
            'Drunkiris']

players_positions = {}
players_positions = pd.DataFrame(columns = ['Rank','Player', 'Tier', 'LP', 'Wins', 'Top4', 'Played', 'Win Rate %', 'Top4 Rate %' ])

for player in players:
    driver.get('https://lolchess.gg/profile/euw/' + player)
    #print("-------------------------------------")
    #print("\n")
    #print(player)
    #print("\n")

    player_tier = driver.find_element_by_class_name("profile__tier__summary__tier")
    player_lp = driver.find_element_by_class_name("profile__tier__summary__lp")
    #print(f"Tier: {player_tier.text} - {player_lp.text}")
    #print(f"{player_lp.text}")

    player_rank_region = driver.find_element_by_class_name("rank-region")
    position_player = player_rank_region.text.replace("#", "")
    #print(f"Rank: {player_rank_region.text}")

    player_wins = driver.find_element_by_class_name("profile__tier__wins")
    wins = [int(s) for s in player_wins.text.split() if s.isdigit()]
    #print(f"Wins: {wins[0]}")

    player_top4 = driver.find_element_by_class_name("profile__tier__tops")
    top4 = [int(s) for s in player_top4.text.split() if s.isdigit()]
    #print(f"Top4: {top4[0]}")

    player_played = driver.find_element_by_class_name("profile__tier__plays")
    played = [int(s) for s in player_played.text.split() if s.isdigit()]
    #print(f"Played: {played[0]}")

    player_winrate = driver.find_element_by_class_name("profile__tier__winrate_10")
    #winrate = [int(s) for s in player_winrate.text.split() if s.isdigit()]
    winrate = re.findall("\d*\.?\d+", player_winrate.text)
    #print(f"Win Rate: {winrate[0]}%")

    player_toprate = driver.find_element_by_class_name("profile__tier__toprate")
    #toprate = [int(s) for s in player_toprate.text.split() if s.isdigit()]
    toprate = re.findall("\d*\.?\d+", player_toprate.text)
    #print(f"Top4 Rate: {toprate[1]}%")

    player_avg_rank = driver.find_element_by_class_name("profile__tier__avg_rank")
    #avg_rank = [int(s) for s in player_avg_rank.text.split() if s.isdigit()]
    avg_rank = re.findall("\d*\.?\d+", player_avg_rank.text)
    #print(f"Avg. Rank: #{avg_rank}")

    
    new_row = {'Rank': position_player, 'Player': player, 'Tier': player_tier.text, 
                'LP': player_lp.text, 'Wins': wins[0], 'Top4': top4[0], 'Played': played[0],
                'Win Rate %': winrate[0], 'Top4 Rate %': toprate[1] }

    #players_positions.insert(-1, position_player, player) 
    players_positions = players_positions.append(new_row, ignore_index=True)
    
    #print(f"mydataframe: {mydataframe}")
    #print(f"player_positions: {players_positions}")
    #print(f"{position_player}, {player}")

    time.sleep(5) # Let the user actually see something!

#print(positions)

players_positions_teste= players_positions.to_csv('teste.csv', index=False)

players_positions['Rank'] = players_positions['Rank'].replace(',','', regex=True)
players_positions['Rank'].astype(str).astype(int)
players_positions['Rank'] = pd.to_numeric(players_positions['Rank'])
#data['Rank'] = pd.to_numeric(data['Rank'], errors='coerce')
#data.dtypes

players_positions.sort_index(inplace=True)
players_positions.sort_values(by ='Rank' , ascending=True, inplace=True)
players_positions.set_index('Rank', inplace=True)
#players_positions.reset_index(drop=True, inplace=True)

players_positions_sorted = players_positions.to_csv('listarank.csv', index=False)

players_positions_np = genfromtxt('listarank.csv', delimiter=',')

ax = players_positions.plot()
fig = ax.get_figure()
fig.savefig('ranktftpt.png')


ax = plt.subplot(111, frame_on=False) # no visible frame
ax.xaxis.set_visible(False)  # hide the x axis
ax.yaxis.set_visible(False)  # hide the y axis

table(ax, players_positions)  # where df is your data frame

plt.savefig('mytable.png')

table_Data = tabulate(players_positions, headers='keys', tablefmt='psql')

#print("-------------------------------------")
#print("\n")
#print(tabulate(players_positions, headers='keys', tablefmt='psql'))
print(table_Data)
#print("\n")
#print(players_positions)

driver.quit()