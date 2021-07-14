import csv
import plotly.express as px
import numpy as np

coffee=[]
sleep=[]
f=open("cups of coffee vs hours of sleep.csv")
csv_reader=csv.DictReader(f)
#print(csv_reader)

for row in csv_reader:
    coffee.append(float(row["Coffee in ml"]))
    sleep.append(float(row["sleep in hours"]))

fig=px.scatter(x=coffee,y=sleep)
fig.show()

correlation=np.corrcoef(x=coffee,y=sleep)
print(f"correlation between coffee and sleep is {correlation[0,1]}")