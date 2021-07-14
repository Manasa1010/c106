import pandas as pd
import plotly.express as px
import numpy as np

df=pd.read_csv("Size of TV,_Average time spent watching TV in a week (hours).csv")
#print(df)

size_of_tv=df["Size of TV"].tolist()
average_time=df["Average time spent watching TV in a week (hours)"].tolist()

print(average_time)

fig=px.scatter(x=size_of_tv,y=average_time)
fig.show()

correlation=np.corrcoef(x=size_of_tv,y=average_time)
print(correlation[0,1])