# 추천 알고리즘 (Q-learning) 모듈
import numpy as np
import random
import pandas as pd


def recommend_food_qlearning(df, user_feedback: dict, alpha=0.1, gamma=0.9, epsilon=0.2, episodes=1000):
    items = df['식단'].tolist()
    n = len(items)
    q_table = np.zeros((n, 2))

    # 초기 보상 세팅 (피드백 반영)
    for i, item in enumerate(items):
        if item in user_feedback:
            q_table[i, :] = user_feedback[item]  # 누적 선호도를 보상으로 반영

    # Q-러닝 학습
    for _ in range(episodes):
        state = random.randrange(n)
        done = False
        while not done:
            action = random.randrange(2) if random.random() < epsilon else int(np.argmax(q_table[state]))
            reward = q_table[state, action]
            next_state = random.randrange(n)
            old = q_table[state, action]
            q_table[state, action] = old + alpha * (reward + gamma * q_table[next_state].max() - old)
            state = next_state
            if random.random() < 0.1:
                done = True

    # 최종 추천 (가장 높은 Q값을 가진 아이템)
    best_idx = int(np.argmax(q_table.max(axis=1)))
    return df.loc[best_idx, '식단']


def generate_final_meal_plan(df: pd.DataFrame, user_feedback: dict, target_cal: int, margin: int) -> list:
    # 피드백이 있는 음식만 선택
    fav = df[df['식단'].isin(user_feedback.keys())].copy()
    if fav.empty:
        return []
    # 피드백 점수 매핑
    fav['score'] = fav['식단'].map(user_feedback)
    # 점수 내림차순, 칼로리 오름차순
    fav = fav.sort_values(['score','칼로리'], ascending=[False, True])
    result, total = [], 0
    for _, row in fav.iterrows():
        if total + row['칼로리'] <= target_cal + margin:
            result.append(row['식단'])
            total += row['칼로리']
    return result