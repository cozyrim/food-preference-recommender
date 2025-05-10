# 데이터 로딩 및 전처리 모듈
import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path, encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv(path, encoding='cp949')

    df = df[['식단', '칼로리', '선호도','카테고리']].copy()
    return df

# 벡터화 칼로리 필터링
def filter_by_calories(df: pd.DataFrame, target: int, margin: int) -> pd.DataFrame:
    mask = df['칼로리'].between(target - margin, target + margin)
    return df.loc[mask].reset_index(drop=True)

# 고유 카테고리 리스트
def get_categories(df: pd.DataFrame) -> list:
    return df['카테고리'].unique().tolist()