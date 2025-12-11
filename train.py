import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

df=pd.read_csv("Rainfall.csv")
X=df[["Humidity","Temperature","WindSpeed","CloudCover"]]
y=df["Rainfall_mm"]

model=RandomForestRegressor().fit(X,y)
pickle.dump(model,open("model.pkl","wb"))
