# streamlit 메인 애플리케이션
import streamlit as st
import logging
import yaml
from data_loader import load_data, filter_by_calories
from ui import show_table, get_user_feedback
from recommender import recommend_food_qlearning

# 로깅 설정
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s:%(message)s")

# 설정 읽기
def load_config(path="config.yaml"):
    with open(path, "r", encoding='utf-8') as f:
        return yaml.safe_load(f)
    
cfg = load_config()

def main():
    st.title("🍽️ 식단 추천 시스템")
    # 1) 데이터 로드
    df = load_data(cfg['data']['path'])

    # 2) 목표 칼로리 입력 & 필터링
    target_cal = st.slider("목표 칼로리", min_value=0, max_value=2000, value=cfg['ui']['default_calories'])
    filtered = filter_by_calories(df, target_cal, cfg['data']['margin'])
    show_table(filtered)

    # 3) 사용자 피드백
    feedback = get_user_feedback(filtered)
    st.write("사용자 피드백:", feedback)

    # 4) 추천
    if st.button("추천 생성하기"):
        recommendation = recommend_food_qlearning(filtered,
                                                  alpha=cfg['ql']['alpha'],
                                                  gamma=cfg['ql']['gamma'],
                                                  epsilon=cfg['ql']['epsilon'],
                                                  episodes=cfg['ql']['episodes'])
        st.success(f"추천된 식단: {recommendation}")
        logging.info(f"Recommended: {recommendation}")

if __name__ == '__main__':
        main()