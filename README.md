# 🍽️ 식단 추천 시스템

**사용자 선호도 누적 Q-러닝 식단 추천**  
목표 칼로리를 설정하고, 카테고리별 음식에 대해 좋아요 버튼을 눌러 선호도를 학습한 뒤, 사용자의 선택을 반영해 최적의 식단 조합을 추천

## 🖼️ 데모

![식단 추천 UI 시연](./food-recommend_fast.gif)
---

## 🔍 주요 기능

* **목표 칼로리 필터링**: 슬라이더로 원하는 일일 칼로리 범위를 지정
* **카테고리별 샘플링**: 밥·국·반찬·디저트·음료·기타 카테고리에서 랜덤으로 음식 3가지씩 제시
* **다중 토글 선택**: 각 라운드마다 최대 6개까지 좋아요(🥗)/비선호(⚪) 토글 가능
* **라운드별 선호도 누적**: 총 3라운드 평가 후, 누적된 선호도를 반영해 추천
* **칼로리 최적화 추천**: 선호도가 높은 음식 우선, 목표 칼로리 ± 마진 내에서 식단 조합 생성

---

## 📁 프로젝트 구조

```
food-recommender/           # 프로젝트 루트
├── app.py                 # Streamlit 메인 애플리케이션
├── data_loader.py         # CSV 로드 및 전처리 모듈
├── ui.py                  # Streamlit UI 구성 모듈
├── recommender.py         # 추천 로직 모듈
├── config.yaml            # 사용자 설정 파일
├── requirements.txt       # 의존성 목록
├── tests/                 # 단위 테스트
│   ├── test_data_loader.py
│   └── test_recommender.py
└── README.md              # 프로젝트 설명서
```

---

## ⚙️ 설치 및 실행

1. 저장소 클론

   ```bash
   git clone https://github.com/yourname/food-recommender.git
   cd food-recommender
   ```
2. 의존성 설치

   ```bash
   pip install -r requirements.txt
   ```
3. Streamlit 실행

   ```bash
   streamlit run app.py
   ```
4. 웹 브라우저에서 표시된 URL(기본: [http://localhost:8501](http://localhost:8501)) 접속

---

## 🛠️ 설정 파일 (config.yaml)

```yaml
data:
  path: 'FoodDataFrame.csv'      # CSV 데이터 경로
  margin: 50                     # ±칼로리 마진
ql:
  alpha: 0.1                     # 학습률
  gamma: 0.9                     # 할인율
  epsilon: 0.2                   # 탐험(epsilon-greedy)
  episodes: 1000                # 에피소드 수
ui:
  default_calories: 500          # 슬라이더 초기 칼로리
  max_rounds: 3                  # 평가 라운드 수
```

---

## ✅ 사용법 요약

1. 슬라이더로 **목표 칼로리**를 설정
2. 제시된 음식 중 \*\*좋아요🔴/비선호⚪\*\*를 최대 6개까지 선택
3. **다음 평가** 버튼을 눌러 라운드 진행 (총 3회)
4. **추천 생성하기** 버튼으로 최종 식단 조합 확인

---


