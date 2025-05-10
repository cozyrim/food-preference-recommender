import pytest
from data_loader import load_data, filter_by_calories, get_categories
import pandas as pd

def sample_df():
    return pd.DataFrame({
        '식단':['A','B'], '카테고리':['국','밥'],
        '칼로리':[100,200]
    })

def test_load_data(tmp_path):
    p = tmp_path / 'test.csv'
    pd.DataFrame({'식품명':['A'], '에너지':[100], '카테고리':['국']}).to_csv(p, index=False)
    df = load_data(str(p))
    assert list(df.columns)==['식단','카테고리','선호도','칼로리']


def test_filter_and_categories():
    df = sample_df()
    filtered = filter_by_calories(df,150,60)
    assert 'A' in filtered['식단'].values
    cats = get_categories(df)
    assert set(cats)=={'국','밥'}