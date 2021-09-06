import pandas as pd

df = pd.read_csv('./survey-results-public.csv')

most_missing_cols = set(df.columns[df.isnull().mean() > 0.75])

print(most_missing_cols)