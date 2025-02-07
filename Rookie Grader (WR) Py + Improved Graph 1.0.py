"""
Austin's Post Draft NFL Prospect Grader (WR)

"""
import matplotlib.pyplot as plt
import numpy as np

NAME = str(input("Player name: "))
height = int(input("Height in inches: "))
weight = int(input("Weight in pounds: "))
speed = float(input("40 yd dash time: "))
TAR = int(input("Total targets for season: "))
REC = int(input("Total receptions for season: "))
YDS = int(input("Total receiving yards for season: "))
YAC_REC = float(input("YAC/REC for season: "))
YPRR = float(input("YPRR for season: "))
draft_pick = int(input("What draft pick was this player: "))

HW_Ratio = weight/height 
Catch_P = REC/TAR
YPC = YDS/REC
NAME_LENGTH = len(NAME)

def assign_score(HW_Ratio):
    if HW_Ratio >= 2.9:
        return 10
    elif 2.83 <= HW_Ratio < 2.9: 
        return 9
    elif 2.75 <= HW_Ratio < 2.83:
        return 8
    elif 2.68 <= HW_Ratio < 2.75:
        return 7
    elif 2.60 <= HW_Ratio < 2.75:
        return 6
    elif 2.53 <= HW_Ratio < 2.60:
        return 5
    elif 2.45 <= HW_Ratio < 2.53:
        return 4
    elif 2.38 <= HW_Ratio < 2.45:
        return 3
    elif 2.30 <= HW_Ratio < 2.38:
        return 2
    elif 2.23 <= HW_Ratio < 2.30:
        return 1
    else:
        return 1
HW_SCORE = (assign_score(HW_Ratio))

def assign_score(speed):
    if speed <= 4.2:
        return 10
    elif 4.2 < speed <= 4.25:
        return 9
    elif 4.25 < speed <= 4.3:
        return 8
    elif 4.3 < speed <= 4.35:
        return 7
    elif 4.35 < speed <= 4.4:
        return 6
    elif 4.4 < speed <= 4.45:
        return 5
    elif 4.45 < speed <= 4.5:
        return 4
    elif 4.5 < speed <= 4.55:
        return 3
    elif 4.55 < speed <= 4.6:
        return 2
    elif 4.65 < speed <= 4.7:
        return 1
    else:
        return 1
SPEED_SCORE = (assign_score(speed))

def assign_score(Catch_P):
    if Catch_P >= 0.8:
        return 10
    elif 0.77 <= Catch_P < 0.8:
        return 9
    elif 0.73 <= Catch_P < 0.77:
        return 8
    elif 0.70 <= Catch_P < 0.73:
        return 7
    elif 0.67 <= Catch_P < 0.70:
        return 6
    elif 0.64 <= Catch_P < 67:
        return 5
    elif 0.6 <= Catch_P < 0.64:
        return 4 
    elif 0.57 <= Catch_P < 0.6:
        return 3 
    elif 0.54 <= Catch_P < 0.57:
        return 2
    elif 0.5 <= Catch_P < 0.54:
        return 1
    else:
        return 1
CATCH_P_SCORE = (assign_score(Catch_P))

def assign_score(YPC):
    if YPC >= 16:
        return 10
    elif 15.25 <= YPC < 16:
        return 9
    elif 14.5 <= YPC < 15.25:
        return 8
    elif 13.75 <= YPC < 14.5:
        return 7
    elif 13 <= YPC < 13.75:
        return 6
    elif 12.25 <= YPC < 13:
        return 5
    elif 11.5 <= YPC < 12.25:
        return 4
    elif 10.75 <= YPC < 11.5:
        return 3
    elif 10 <= YPC < 10.75:
        return 2
    elif 9.25 <= YPC < 10:
        return 1
    else:
        return 1
YPC_SCORE = (assign_score(YPC))

def assign_score(YAC_REC):
    if YAC_REC >= 7:
        return 10
    elif 6.25 <= YAC_REC < 7:
        return 9
    elif 5.75 <= YAC_REC < 6.25:
        return 8 
    elif 5.25 <= YAC_REC < 5.75:
        return 7
    elif 4.75 <= YAC_REC < 5.25:
        return 6
    elif 4.25 <= YAC_REC < 4.75:
        return 5
    elif 3.75 <= YAC_REC < 4.25:
        return 4
    elif 3.25 <= YAC_REC < 3.75:
        return 3
    elif 2.75 <= YAC_REC < 3.25:
        return 2
    elif 2.25 <= YAC_REC < 2.75:
        return 1
    else:
        return 1
YAC_REC_SCORE = (assign_score(YAC_REC))

def assign_score(YPRR):
    if YPRR >= 3:
        return 10
    elif 2.87 <= YPRR < 3:
        return 9
    elif 2.74 <= YPRR < 2.87:
        return 8
    elif 2.61 <= YPRR < 2.74:
        return 7
    elif 2.48 <= YPRR < 2.61:
        return 6
    elif 2.35 <= YPRR < 2.48:
        return 5
    elif 2.22 <= YPRR < 2.35:
        return 4
    elif 2.09 <= YPRR < 2.22:
        return 3
    elif 1.96 <= YPRR < 2.09:
        return 2
    elif 1.83 <= YPRR < 1.96:
        return 1
    else:
        return 1
YPRR_SCORE = (assign_score(YPRR))

ADJ_HW_SCORE = HW_SCORE * 0.05
ADJ_SPEED_SCORE = SPEED_SCORE * 0.1
ADJ_CATCH_P_SCORE = CATCH_P_SCORE * 0.1
ADJ_YPC_SCORE = YPC_SCORE * 0.2
ADJ_YAC_REC_SCORE = YAC_REC_SCORE * 0.25
ADJ_YPRR_SCORE = YPRR_SCORE * 0.3

FINAL_SCORE = ADJ_HW_SCORE + ADJ_SPEED_SCORE + ADJ_CATCH_P_SCORE + ADJ_YPC_SCORE + ADJ_YAC_REC_SCORE + ADJ_YPRR_SCORE

print("Final score:", FINAL_SCORE)

x = [draft_pick]
y = [FINAL_SCORE]

fig, ax = plt.subplots()

ax.scatter(x,y)

ax.set_xlim(256, 1)
ax.set_ylim(4, 10)

#these lines plot the permanent points. Add the length of the name times 2.8 to draft pick and add 0.1 to final score for name placment
plt.scatter(5, 9.3, color = 'orange')
plt.text(5 + (13 * 2.8), 9.4, """Ja'Marr Chase""", fontsize = 7)

plt.scatter(177, 9.05, color = 'blue')
plt.text(177 + (10 * 2.8), 9.15, "Puka Nacua", fontsize = 7)

plt.scatter(32, 7.6, color = 'navy')
plt.text(32 + (12 * 2.8), 7.7, """N'Keal Harry""", fontsize = 7)

# to adjust for smaller names multiply draft pick by 2.8
plt.text(draft_pick + (NAME_LENGTH * 2.8), FINAL_SCORE + 0.1, str(NAME), fontsize = 7)


plt.xlabel("Draft Pick")
plt.ylabel("Calculated Score")
plt.title("Will This Receiver be Good in the NFL?")

xx = np.random.randint(0, 256, 0)
yy = np.random.randint(4, 10, 0)

plt.scatter(xx, yy)

plt.plot([256, 1], [9.3, 7.5], color = 'red')

plt.show