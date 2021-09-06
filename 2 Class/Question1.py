import pandas as pd

schema = pd.read_csv('./survey-results-schema.csv')

def get_description(columns_name, schema = schema):

    desc = list(schema[schema['Column'] == columns_name]['Question'])[0]
    return desc

print(get_description('CousinEducation'))
