import pandas as pd

schema = pd.read_csv('./survey-results-schema.csv')

cous_ed_vals = schema[schema['Column'] == 'CousinEducation'].value_counts()

print(cous_ed_vals)