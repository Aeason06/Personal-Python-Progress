# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 09:40:38 2025

@author: austi
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image

data_path = r"C:\Users\austi\Downloads\panthers scoring sheet un-edited.xls.xlsx"
image_path = r"C:\Users\austi\OneDrive\Desktop\nfl team logos\CAR.png"
scoring_data = pd.read_excel(data_path)

min_points = 80

filtered_scoring_data = scoring_data[scoring_data['Pts'] >= min_points]
colors = ['#0085CA', '#BFC0BF', '#101820']

points = list(filtered_scoring_data['Pts'])
names = list (filtered_scoring_data['Player'])

labels = [f"{name} ({point})" for name, point in zip(names, points)]

fig, ax = plt.subplots()

ax.pie(points, labels = labels, colors = colors, wedgeprops={'edgecolor': 'white', 'linewidth': 2})

img = Image.open(image_path)
image_array = np.array(img)

image_box = OffsetImage(image_array, zoom = 0.8)
ab = AnnotationBbox(image_box, (0, 0), frameon = False)
ax.add_artist(ab)

plt.title('Carolina Panthers All Time Leading Scorers (min. 80 points)')
plt.text(0.6, -1.25, 'Data from pro football reference, plot by Austin Eason', fontsize = 7)
plt.show()