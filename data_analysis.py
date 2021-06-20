import pandas as pd
import plotly.express as pl

student_data = pd.read_csv('./hwFiles/data/mobile_data.csv')

student_means = student_data.groupby(['student_id', 'level'], as_index=False)['attempt'].mean()
fig = pl.scatter(student_means, x='student_id', y='level', color='attempt')

fig.show()