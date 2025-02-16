# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 12:46:07 2025

@author: austi
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

data_path = r"C:\Users\austi\Downloads\2024 nfl drive data.xls.xlsx"

team_data = pd.read_excel(data_path)

points = list(team_data['points'].head(32))
start = list(team_data['start'].head(32))
teams = list(team_data['team'].head(32))
labels = team_data['team']
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

for i in range (len(points)):
    x_random = np.random.uniform(-0.04, 0.05)
    y_random = np.random.uniform(0, 0.03)
    text = plt.text(points[i] + x_random, start[i] + y_random, labels[i], fontsize = 7, ha = 'right', va = 'bottom')

colors = [team_colors.get(team, 'grey')for team in teams]
plt.scatter(points, start, color = colors)
plt.title('Starting Field Position VS Average Points Per Drive (PPD)')

plt.xlabel('PPD')
plt.ylabel('Avg. Starting Field Position')
plt.text(2.35, 26.55, 'Data from Pro Football Refrence, Austin Eason', fontsize = 6)
plt.show()



