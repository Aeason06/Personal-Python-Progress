# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 15:25:40 2025

@author: austi
"""

import nfl_data_py as nfl
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import urllib.request
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from PIL import Image

#import play by play data
pbp = nfl.import_pbp_data([1999])

#set pass and rush == 1 because that gets data for plays where 1 pass or rush was attempted
pbp_rp = pbp[(pbp['pass'] == 1) | (pbp['rush'] == 1)]

#.dropna is a pandas function that gets rid of rows with missing values from specified columns
pbp_rp = pbp_rp.dropna(subset = ['epa', 'posteam', 'defteam'])

#pass_epa is table sorted by posteam containing mean passing epa and renames epa to pass_epa
pass_epa = pbp_rp[(pbp_rp['pass'] == 1)].groupby('posteam')['epa'].mean().reset_index().rename(columns = {'epa' : 'pass_epa'})
#sorts pass_epa table 
pass_epa.sort_values('pass_epa', ascending = False)

rush_epa = pbp_rp[(pbp_rp['rush'] == 1)].groupby('posteam')['epa'].mean().reset_index().rename(columns = {'epa' : 'rush_epa'})
rush_epa.sort_values('rush_epa', ascending = False)

#merges pass_epa and rush_epa into one table sorted by posteam
epa = pd.merge(pass_epa, rush_epa, on = 'posteam')

logos = nfl.import_team_desc()[['team_abbr', 'team_logo_espn']]

logo_paths = []
team_abbr = []

#reusable logo pathing code using team abbreviations 
if not os.path.exists('logos'):
    os.makedirs('logos')

for team in range(len(logos)):
    urllib.request.urlretrieve(logos['team_logo_espn'][team], f'logos/{logos["team_abbr"][team]}.tif')
    logo_paths.append(f'logos/{logos["team_abbr"][team]}.tif')
    team_abbr.append(logos['team_abbr'][team])
    
data = {'team_abbr' : team_abbr, 'logo_path' : logo_paths}
logo_data = pd.DataFrame(data)

#join epa data with logo data have to specify right and left because posteam and team_abbr contain same data but have diff names
epa_with_logos = pd.merge(epa, logo_data, left_on = 'posteam', right_on = 'team_abbr')

#CREATE PLOT
plt.rcParams['figure.figsize'] = [10, 7]
plt.rcParams['figure.autolayout'] = True

def getImage(path, size=(100, 100)):  # Adjust size to your preferred dimensions
    # Open image with PIL
    img = Image.open(path)
    img = img.resize(size, Image.Resampling.LANCZOS)  # Resize image
    return OffsetImage(np.array(img), zoom = 0.4)

x = epa_with_logos['pass_epa']
y = epa_with_logos['rush_epa']
paths = epa_with_logos['logo_path']

fig, ax = plt.subplots()

for x0, y0, path in zip(x, y, paths):
    ab = AnnotationBbox(getImage(path), (x0, y0), frameon = False)
    ax.add_artist(ab)

print(epa_with_logos)
plt.xlim(-0.25, 0.35)
plt.ylim(-0.35, 0.15)
plt.title('Average Pass vs Rush Epa (1999)')
plt.xlabel('Pass EPA')
plt.ylabel('Rush EPA')
plt.text(0.22, -0.39, 'Data from nfl_data_py, plot by Austin Eason', fontsize = 6)
plt.show()

