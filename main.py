import panda as pd 

url = https://raw.githubusercontent.com/treinholdt/ML-Adventures/refs/heads/main/daily_fruit_sales.csv

df = pd.read_csv(url)
print(df.head())
