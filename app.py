# streamlit 메인 애플리케이션
import streamlit as st
import logging
import yaml
from data_loader import load_data, filter_by_calories, get_categories
from ui import show_table, get_random_feedback_items
from recommender import generate_final_meal_plan

# 로깅 설정
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s:%(message)s")

def load_config(path="config.yaml"):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

cfg = load_config()

# 세션 초기화
if 'round' not in st.session_state:
    st.session_state.round = 1
if 'selected_items' not in st.session_state:
    st.session_state.selected_items = set()
if 'feedback' not in st.session_state:
    st.session_state.feedback = {}

st.title("🍽️ 식단 추천 시스템")

# 1) 데이터 로드
df = load_data(cfg['data']['path'])

# 2) 목표 칼로리
target_cal = st.slider("목표 칼로리", 0, 2000, cfg['ui']['default_calories'])
filtered = filter_by_calories(df, target_cal, cfg['data']['margin'])

# 3) 카테고리별 샘플링
categories = get_categories(filtered)
sample_items = get_random_feedback_items(filtered, categories, sample_per_category=3)

# 4) UI 표시 및 선택
selected = show_table(sample_items)

# 선택된 메뉴 띄우기
if selected:
    st.markdown(f"**선택된 메뉴:** {', '.join(selected)}")

# 5) 평가 라운드 처리
if st.session_state.round < cfg['ui']['max_rounds']:
    st.info(f"📝 {cfg['ui']['max_rounds'] - st.session_state.round + 1}회 평가 남음")
    if st.button("다음 평가"):
        # 피드백 누적
        for item in selected:
            st.session_state.feedback[item] = st.session_state.feedback.get(item, 0) + 1
        # 라운드 증가 및 선택 초기화
        st.session_state.round += 1
        st.session_state.selected_items.clear()
        st.rerun()
else:
    # 최종 추천
    if st.button("추천 생성하기"):
        rec = generate_final_meal_plan(filtered, st.session_state.feedback, target_cal, cfg['data']['margin'])
        if rec:
            st.success(f"💡 최종 추천 식단: {', '.join(rec)}")
        else:
            st.warning("⚠️ 선호한 음식이 없어 추천을 생성할 수 없습니다.")
        logging.info(f"Final Recommendation: {rec}")