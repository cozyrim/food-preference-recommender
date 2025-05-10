import pandas as pd
from recommender import recommend_food_qlearning

def test_recommend():
    df = pd.DataFrame({
        '식단':['X','Y'], '카테고리':['밥','국'],
        '선호도':[0,0], '칼로리':[100,200]
    })
    fb={'X':'like'}
    rec = recommend_food_qlearning(df, user_feedback=fb, episodes=10)
    assert rec in df['식단'].values