import pandas as pd


df0 = pd.read_csv('FoodDataFrame.csv', encoding='utf-8')

df = df0[['식품명', '에너지']].rename(
    columns={'식품명':'식단', '에너지': '칼로리'})

df['선호도'] = 0

df.to_csv('FoodDataFrame.csv', index=False, encoding='utf-8')