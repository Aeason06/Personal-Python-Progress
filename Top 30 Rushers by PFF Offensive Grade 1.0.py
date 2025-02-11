# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 21:07:19 2025

@author: austi
"""

import pandas as pd
import matplotlib.pyplot as plt
rush_path = #file path

rush_data = pd.read_csv(rush_path)

min_attempts = 100

filtered_rush_data = rush_data[rush_data['attempts'] >= min_attempts]

rush_data_sorted = filtered_rush_data.sort_values(by = 'grades_offense', ascending = False)

names = list(rush_data_sorted['player'].head(30))
o_grade = list(rush_data_sorted['grades_offense'].head(30))
teams = list(rush_data_sorted['team_name'].head(30))
attempts = list(rush_data_sorted['attempts'].head(30))

team_colors = {
    'ARZ' : '#97233F',
    'ATL' : 'black',
    'BLT' : '#241773',
    'BUF' : '#00338D',
    'CAR' : '#0085CA',
    'CHI' : '#0B162A',
    'CIN' : '#FB4F14',
    'CLV' : '#311D00',
    'DAL' : '#041E42',
    'DEN' : '#FB4F14',
    'DET' : '#0076B6', 
    'GB' : '#203731',
    'HST' : '#03202F',
    'IND' : '#002C5F',
    'JAX' : '#006778',
    'KC' : '#E31837',
    'LV' : 'black',
    'LAC' : '#0080C6',
    'LA' : '#003594',
    'MIA' : '#008E97',
    'MIN' : '#4F2683',
    'NE' : '#002244',
    'NO' : '#D3BC8D',
    'NYG' : '#0B2265',
    'NYJ' : '#125740',
    'PHI' : '#004C54',
    'PIT' : 'black',
    'SF' : '#AA0000',
    'SEA' : '#002244',
    'TB' : '#D50A0A',
    'TEN' : '#4B92DB',
    'WAS' : '#5A1414'
    }

colors = [team_colors.get(team, 'grey')for team in teams]
plt.bar(names, o_grade, color = colors)
plt.title('Top 30 Rushers by PFF Offensive Grade (2024 min. 100 attempts)')
plt.xlabel("""Players""")
plt.ylabel('Offensive Grades')

plt.ylim(bottom = 70)
plt.xticks(rotation = 315, ha = 'left', fontsize = 7)

plt.show()
