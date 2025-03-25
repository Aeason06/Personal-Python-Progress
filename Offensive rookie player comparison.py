# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 19:35:35 2025

@author: austi
"""

import nfl_data_py as nfl
#import data
ngs_wr = nfl.import_ngs_data('receiving', years= list(range(2016, 2025)))
ngs_rb = nfl.import_ngs_data('rushing', years= list(range(2016, 2025)))
ngs_qb = nfl.import_ngs_data('passing', years= list(range(2016, 2025)))
draft = nfl.import_draft_picks(list(range(2016,2025)))
#sort and clean data tables
wr_table = ngs_wr[['player_display_name', 'receptions', 'yards', 'rec_touchdowns', 'season', 'week', 'player_position']]
wr_table = wr_table.dropna(subset = ['player_display_name', 'receptions', 'yards', 'rec_touchdowns', 'season'])
wr_table = wr_table.rename(columns = {'rec_touchdowns' : 'td', 'receptions' : 'rec', 'player_display_name': 'name', 'yards':'yrd'})

rb_table = ngs_rb[['player_display_name', 'rush_yards', 'avg_rush_yards', 'rush_touchdowns', 'season', 'week']]
rb_table = rb_table.dropna(subset = ['player_display_name', 'rush_yards', 'avg_rush_yards', 'rush_touchdowns'])
rb_table = rb_table.rename(columns = {'player_display_name' : 'name', 'rush_yards' : 'yrd', 'avg_rush_yards' : 'ypa', 'rush_touchdowns' : 'td'})

qb_table = ngs_qb[['player_display_name', 'pass_yards', 'pass_touchdowns', 'season', 'week']]
qb_table = qb_table.dropna(subset = ['player_display_name', 'pass_yards', 'pass_touchdowns', 'season', 'week'])
qb_table = qb_table.rename(columns = {'player_display_name' : 'name', 'pass_yards' : 'yrd', 'pass_touchdowns' : 'td'})
#input
player = str(input('Enter players first and last name (ex: Tyreek Hill, Mark Andrews, Bucky Irving, Bo Nix): '))

#base value so hold will always start off valid
start = 999999
#turn data into lists for for loops
wr_names = list(wr_table['name'])
rb_names = list(rb_table['name'])
qb_names = list(qb_table['name'])
#wr and te section
if player in wr_names:
    print('Rookie seasons within 150 recieving yards and 12 receptions of '+ player + ' since 2016:' )
    #turn data into lists for for loops
    yards = list(wr_table['yrd'])
    catch = list(wr_table['rec'])
    tdown = list(wr_table['td'])
    season = list(wr_table['season'])
    week = list(wr_table['week'])
    pos = list(wr_table['player_position'])
    
    #loop through seasons for input player and find their oldest season by getting the smallest index
    #Get rookie season
    for index in range(len(wr_names)):
        if wr_names[index] == player and week[index] == 0:
            hold = (index, wr_names[index], yards[index], catch[index], tdown[index], season[index], week[index], pos[index])
            if hold[0] < start:
                input_rookie = hold
                start = hold[0]
    #set lists to correlate players with draft year 
    draft_n = list(draft['pfr_player_name'])
    draft_y = list(draft['season'])
    #first compare stats, then find name in draft names and set i to that index, lastly check if draft year[index] == the season that the player put up similar stats and if so print them
    for index in range(len(wr_names)):
        if (abs(yards[index] - input_rookie[2]) <= 150 and abs(catch[index] - input_rookie[3]) <= 12 and input_rookie[7] == pos[index]):
            if wr_names[index] in draft_n:
                i = draft_n.index(wr_names[index])
                if season[index] == draft_y[i]:
                    similar = (wr_names[index], str(yards[index])+' yd', str(catch[index])+' rec', str(tdown[index])+' td', season[index])
                    print(similar)
#rb section
elif player in rb_names:
    print('Rookie seasons within 150 rush yards and 4 tds of '+ player + ' since 2016:' )
    yards = list(rb_table['yrd'])
    tdown = list(rb_table['td'])
    season = list(rb_table['season'])
    week = list(rb_table['week'])
    
    for index in range(len(rb_names)):
        if rb_names[index] == player and week[index] == 0:
            hold = (index, rb_names[index], yards[index], tdown[index], season[index], week[index])
            if hold[0] < start:
                input_rookie = hold
                start = hold[0]
    draft_n = list(draft['pfr_player_name'])
    draft_y = list(draft['season'])
    for index in range(len(rb_names)):
        if (abs(yards[index] - input_rookie[2]) <= 150 and abs(tdown[index] - input_rookie[3]) <= 4):
            if rb_names[index] in draft_n:
                i = draft_n.index(rb_names[index])
                if season[index] == draft_y[i]:
                    similar = (rb_names[index], str(yards[index])+' yd', str(tdown[index])+' td', season[index])
                    print(similar)
#qb section
elif player in qb_names:
    print('Rookie seasons within 400 pass yards and 4 tds of '+ player + ' since 2016:' )
    yards = list(qb_table['yrd'])
    tdown = list(qb_table['td'])
    season = list(qb_table['season'])
    week = list(qb_table['week'])
    
    for index in range(len(qb_names)):
        if qb_names[index] == player and week[index] == 0:
            hold = (index, qb_names[index], yards[index], tdown[index], season[index], week[index])
            if hold[0] < start:
                input_rookie = hold
                start = hold[0]
    draft_n = list(draft['pfr_player_name'])
    draft_y = list(draft['season'])
    for index in range(len(qb_names)):
        if (abs(yards[index] - input_rookie[2]) <= 400 and abs(tdown[index] - input_rookie[3]) <= 4):
            if qb_names[index] in draft_n:
                i = draft_n.index(qb_names[index])
                if season[index] == draft_y[i]:
                    similar = (qb_names[index], str(yards[index])+' pass yd', str(tdown[index])+' td', season[index])
                    print(similar)
else:
    print('Invalid input. Inputs are case sensitive. Players drafted prior to 2016 can cause issues.')