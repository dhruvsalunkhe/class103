import pandas as pd

import plotly.express as px

df = pd.read_csv('data.csv')

figure = px.scatter(df,x="Per capita",y="InternetUsers",size="Population",color="Country",size_max=30)
figure.show()