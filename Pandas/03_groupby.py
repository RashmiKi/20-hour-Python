import pandas as pd

df =  pd.read_csv(r"C:\Users\Rashmi\Downloads\weather_by_cities.csv")

city = df.groupby("city")
print(city.max())