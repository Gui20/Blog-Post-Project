import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./survey-results-public.csv')

status_vals = df.Professional.value_counts()

(status_vals/df.shape[0]).plot(kind="bar");
plt.title("What kind of developer are you?");
plt.show()

