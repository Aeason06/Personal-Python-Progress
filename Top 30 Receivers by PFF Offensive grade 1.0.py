"""
CODING WITH CSV AND EXCEL
"""
# Always use pandas when doing someithng with csv of xlsx
import pandas as pd
import matplotlib.pyplot as plt
# Get path from file explorer and paste it here. place "r" in front of path to prevent errors later.
rec_path = r"C:\Users\austi\OneDrive\Desktop\receiving_summary_2024_WR_priority.csv"

# This reads whole file. All rows and columns. Use "read_excel" if using a xlsx file.
rec_data = pd.read_csv(rec_path)

# "usecols" allows you to choose which column to use and ".head" allows you to decide how many rows from the top you want to use ".tail" would do the opposite.
# rec_data = pd.read_csv(path, usecols = ['player'])

# Try to find a way to only use players with min 35 targets

names = list(rec_data['player'].head(30))
o_grade = list(rec_data['grades_offense'].head(30))
teams = list(rec_data['team_name'].head(30))

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
plt.title('Top 30 Receivers by PFF Offensive Grade (2024 min. 25 TGT)')
plt.xlabel("""WR's""")
plt.ylabel('Offensive Grades')

plt.ylim(bottom = 75)
plt.xticks(rotation = 315, ha = 'left', fontsize = 7)

plt.show()

