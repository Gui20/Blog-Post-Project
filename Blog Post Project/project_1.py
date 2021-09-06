from collections import defaultdict
import pandas as pd
import matplotlib.pyplot as plt

#FIRST TOPIC
df = pd.read_csv('survey_results_public.csv')

def total_count(df, col1, col2, look_for):
    new_df = defaultdict(int)
    #loop through list of ed types
    for val in look_for:
        #loop through rows
        for idx in range(df.shape[0]):
            #if the ed type is in the row add 1
            if val in df[col1][idx]:
                new_df[val] += int(df[col2][idx])
    new_df = pd.DataFrame(pd.Series(new_df)).reset_index()
    new_df.columns = [col1, col2]
    new_df.sort_values('count', ascending=False, inplace=True)
    return new_df

possible_vals = ["AWS", "Microsoft Azure", "Google Cloud Platform", "Heroku"]
plot = True
title = 'Most used Platforms for StakOverflow survey respondents'


print('Whats is the most used platforms in the Survey held in 2021?')
most_used_platform = df['PlatformHaveWorkedWith'].value_counts().reset_index()

print('Cloud Computing is getting stronger than ever')
most_used_platform.rename(columns={'index': 'method', 'PlatformHaveWorkedWith': 'count'}, inplace=True)
most_used_platform_df = total_count(most_used_platform, 'method', 'count', possible_vals)

most_used_platform_df.set_index('method', inplace=True)
if plot:
    (most_used_platform_df/most_used_platform_df.sum()).plot(kind='bar', legend=None);
    plt.title(title);
    plt.show()
props_study_df = most_used_platform_df/most_used_platform_df.sum()


