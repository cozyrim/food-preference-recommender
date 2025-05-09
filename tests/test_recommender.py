import pandas as pd
from recommender import recommend_food_qlearning

def test_recommend():
    df = pd.DataFrame({
        '식단': ['A', 'B', 'C'],
        '선호도': [10, -5, 0],
        '칼로리': [100, 200, 300]
    })
    rec = recommend_food_qlearning(df, episodes=10)
    assert rec in df['식단'].values