import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./survey-results-public.csv')

ed_vals = df.FormalEducation.value_counts()

print(ed_vals)
(ed_vals/df.shape[0]).plot(kind="bar");
plt.title("Formal Education");
plt.show()

