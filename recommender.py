# 추천 알고리즘 (Q-learning) 모듈
import numpy as np
import random

def recommend_food_qlearning(df, alpha=0.1, gamma=0.9, epsilon=0.2, episodes=1000):
    n = len(df)
    q_table = np.zeros((n, 2))
    for ep in range(episodes):
        state = random.randrange(n)
        done = False
        while not done:
            # epsilon-greedy 행동 선택
            if random.random() < epsilon:
                action = random.randrange(2)
            else:
                action = int(np.rgmax(q_table[state]))

            # 보상 : 좋아요=+1, 싫어요=-1
            reward = 1 if df.loc[state, '선호도'] >= 0 else -1
            next_state = random.randrange(n)

            # Q-업데이트
            old = q_table[state, action]
            q_table[state, action] = old + alpha * (reward + gamma * q_table[next_state].max() - old)
            state = next_state
            if random.random() < 0.1:
                done = True
    best_idx = int(np.argmax(q_table.max(axis=1)))
    return df.loc[best_idx, '식단']
