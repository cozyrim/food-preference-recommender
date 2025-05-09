# Streamlit UI 구성 모듈
import streamlit as st
import pandas as pd

# 테이블 표시
def show_table(df: pd.DataFrame):
    feedback = {}
    for i, row in df.iterrows():
        col1, col2 = st.columns([3,1])
        with col1:
            st.write(f"{i}. {row['식단']} ({row['칼로리']} kcal)")
            with col2:
                if st.button(f"👍 {i}", key=f"like_{i}"):
                    feedback[row['식단']] = 'like'
                if st.button("👎 {i}", key=f"dislike_{i}"):
                    feedback[row['식단']] = 'dislike'
    return feedback