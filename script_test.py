import re, time, os, os.path, six, email, smtplib, ssl, imghdr
from pathlib import Path
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from tabulate import tabulate
import matplotlib.pyplot as plt
from pandas.plotting import table
from twilio.rest import Client
from email.message import EmailMessage
import datetime as dt

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)  # Optional argument, if not specified will search path.

players = ['ArtourBabaevsky', 'EGN Rodrigues', 'Kuzma is High', 'Nyxer TFT', 'FTW AïM', 'Kilnae', 'Jitonce' , 'Batata', 'EGN Renygp xD', 'Drunkiris', 'ZOOLEXisTOP'] #'Nyxer TFT', 'FTW AïM', 'Kilnae', 'Jitonce' , 'Batata', 'EGN Renygp xD', 'Drunkiris', 'ZOOLEXisTOP'
                                                                    
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

    time.sleep(1) # Let the user actually see something!

#print(positions)
driver.quit()

players_positions['Rank'] = players_positions['Rank'].replace(',','', regex=True)
players_positions['Rank'].astype(str).astype(int)
players_positions['Rank'] = pd.to_numeric(players_positions['Rank'])
#data['Rank'] = pd.to_numeric(data['Rank'], errors='coerce')
#data.dtypes

players_positions.sort_index(inplace=True)
players_positions.sort_values(by ='Rank' , ascending=True, inplace=True)
players_positions.set_index('Rank', inplace=True)
#players_positions.reset_index(drop=True, inplace=True)

table_Data = tabulate(players_positions, headers='keys', tablefmt='psql')

#print("-------------------------------------")
print("\n")
#print(tabulate(players_positions, headers='keys', tablefmt='psql'))
print(table_Data)
#print("\n")
#print(players_positions)

players_positions_sorted = players_positions.to_csv('listarank.csv', index=False)
data = pd.read_csv('listarank.csv', delimiter=',')


#file_path = "D:\Pythonprojects\tftptscript\listarank.csv"

dirname = os.getcwd()
filename = 'listarank'
suffix = '.csv'

file_path = Path(dirname, filename).with_suffix(suffix)

while not os.path.exists(file_path):
    time.sleep(1)

if os.path.isfile(file_path):
    data = pd.read_csv('listarank.csv', delimiter=',')
else:
    raise ValueError("%s isn't a file!" % file_path)

data["Date"] = pd.Series([dt.datetime.now().date()] * len(data))

def render_mpl_table(data, col_width=3.5, row_height=0.625, font_size=14,
                     header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color='w',
                     bbox=[0, 0, 1, 1], header_columns=0,
                     ax=None, **kwargs):
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')

    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)

    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    for k, cell in six.iteritems(mpl_table._cells):
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
    return ax

render_mpl_table(data, header_columns=0, col_width=3.5)
plt.savefig('listarank.png')
plt.savefig('listarank.jpeg')

pw = os.environ.get('gmailpw_py')

port = 465  # For starttls
smtp_server = 'smtp.gmail.com'
sender_email = 'tftrankpt.py@gmail.com'
password = pw 

msg = EmailMessage()
msg['Subject'] = 'Lista Rank TFT PT'
msg['From'] = 'tftrankpt.py@gmail.com'
msg['To'] = 'onun.nuno@gmail.com'
msg.set_content('Lista Rank TFT PT')

with open('listarank.jpeg', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

msg.add_attachment(file_data, maintype = 'image', subtype = file_type, filename = file_name)

with smtplib.SMTP_SSL(smtp_server, port) as server:
    server.login(sender_email, password)
    server.send_message(msg)

os.remove('D:/Pythonprojects/tftptscript/listarank.csv')
os.remove('D:/Pythonprojects/tftptscript/listarank.jpeg')
os.remove('D:/Pythonprojects/tftptscript/listarank.png')

