# Streamlit UI 구성 모듈
import streamlit as st
import pandas as pd
import random

# 테이블 표시와 피드백 수집 함수
# sample_items: DataFrame ['식단','카테고리','선호도','칼로리']
def show_table(sample_items: pd.DataFrame) -> set:
    st.markdown("---")
    for _, row in sample_items.iterrows():
        cols = st.columns([6,1])
        # 왼쪽: 이름, 칼로리, 카테고리
        cols[0].write(f"{row['식단']} ({row['칼로리']} kcal) [{row['카테고리']}]" )
        # 토글 버튼
        is_sel = row['식단'] in st.session_state.selected_items
        label = "🥗" if is_sel else "⚪"
        if cols[1].button(label, key=f"btn_{row['식단']}"):
            new = set(st.session_state.selected_items)
            if is_sel:
                new.remove(row['식단'])
            else:
                if len(new) < 6:
                    new.add(row['식단'])
            st.session_state.selected_items = new
            st.rerun()
    return set(st.session_state.selected_items)

# 카테고리별 랜덤 샘플링
def get_random_feedback_items(df: pd.DataFrame, categories: list, sample_per_category: int) -> pd.DataFrame:
    frames = []
    for cat in categories:
        cat_df = df[df['카테고리'] == cat]
        if len(cat_df) >= sample_per_category:
            sampled = cat_df.sample(sample_per_category, random_state=42)
        else:
            sampled = cat_df
        frames.append(sampled)
    return pd.concat(frames).reset_index(drop=True)