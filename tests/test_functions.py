import pytest
import pandas as pd
from src.data_cleaning import clean_imdb_data

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        "Vote_Count": ["12K", "5K", "1.5K"],
        "Budget_USD": ["$50.0M", "$10.0M", "$7.5M"],
        "Revenue_$": ["$100.0M", "$40.0M", "$20.5M"]
    })

def test_clean_imdb_data(sample_data):
    cleaned_df = clean_imdb_data(sample_data)

    # Check conversion
    assert cleaned_df["Vote_Count"].dtype == int
    assert cleaned_df["Budget_USD"].dtype == float
    assert cleaned_df["Revenue_$"].dtype == float
