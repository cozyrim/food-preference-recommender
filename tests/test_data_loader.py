import pytest
from data_loadter import load_data, filter_by_calories
import pandas as pd

def sample_df():
    return pd.DataFram({
        '식단': ['A', 'B', 'C'],
        '선호도': [1,2,3],
        '칼로리': [100, 200, 300]
    })

def test_load_data(tmp_path, monkeypatch):
    p = tmp_path / 'test.csv'
    sample_df().to_csv(p, index=False)
    df = load_data(str(p))
    assert list(df.columns) == ['식단', '선호도', '칼로리']
    assert len(df) == 3

def test_filter_by_calories():
    df = sample_df()
    filtered = filter_by_calories(df, 500, 100)
    assert all(filtered['칼로리'].between(400, 600))