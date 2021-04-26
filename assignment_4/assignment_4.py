# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:22:07 2020

@author: SC
"""
import seaborn as sns
import pandas as pd
import plotly.express as px
import numpy as np

# task (a) scatter plot matrix
sns.set(style="ticks")

teacher_data = pd.read_csv('DataWeierstrass.csv',delimiter=';')

sns_plot = sns.pairplot(teacher_data,hue="professor",diag_kind="none")
sns_plot.fig.suptitle("Best Teacher scatter plot matrix", y=1.08)
sns_plot.savefig("scatter_plot.png")


# task (b) parallel coordinates


saved_column =  np.arange(122)
m = 0
for row in teacher_data.professor:
    saved_column[m] = int(row.replace('prof', ''))
    m += 1
 

n = 0
saved_column_lect =  np.arange(122)
for row in teacher_data.lecture:

    saved_column_lect[n] = int(row.replace('lecture', ''))
    n += 1
    

teacher_data.insert(1, "professor_new", saved_column, True) 
teacher_data.insert(2, "lecture_new", saved_column_lect, True) 
del teacher_data['professor']
del teacher_data['lecture']


fig = px.parallel_coordinates(teacher_data, color="professor_new", labels={"professor_new": "professor",
                "lecture_new": "lecture", "participants": "participants",
                "professional expertise": "professional expertise", "motivation": "motivation", "clear presentation": "clear presentation","overall impression": "overall impression"},
                             color_continuous_scale=px.colors.diverging.RdBu,title="best teacher parallel coordinates")

fig.show()