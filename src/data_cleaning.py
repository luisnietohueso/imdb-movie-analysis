import pandas as pd

def clean_imdb_data(file_path):
    df = pd.read_csv(file_path)
    
    # Convert numeric columns
    df['Vote_Count'] = df['Vote_Count'].str.replace('K', '000').astype(int)
    df['Budget_USD'] = df['Budget_USD'].str.replace('[\$,M]', '', regex=True).astype(float) * 1e6
    df['Revenue_$'] = df['Revenue_$'].str.replace('[\$,M]', '', regex=True).astype(float) * 1e6
    df['Run_Time_Minutes'] = pd.to_numeric(df['Run_Time_Minutes'], errors='coerce')

    # Replace "Not_Found" with NaN
    df['Tagline'] = df['Tagline'].replace("Not_Found", None)

    # Save the cleaned data
    df.to_csv("data/cleaned_imdb.csv", index=False)
    return df

