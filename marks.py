import pandas as pd
import plotly.express as px
import numpy as np

df=pd.read_csv("Student Marks vs Days Present.csv")
#print(df)

marks_per=df["Marks In Percentage"].tolist()
days_present=df["Days Present"].tolist()

fig=px.scatter(x=marks_per,y=days_present)
fig.show()

correlation=np.corrcoef(x=marks_per,y=days_present)
print("correlation between marks and days present is "+str(correlation[0,1]))