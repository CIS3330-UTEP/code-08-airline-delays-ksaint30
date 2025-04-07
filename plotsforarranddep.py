import pandas as pd
import matplotlib.pyplot as plt
filename = 'Flight_Delays_2018.csv'
df = pd.read_csv(filename)
df = df.query("DEP_DELAY > 0 or ARR_DELAY > 0")
df.boxplot(column="ARR_DELAY")
plt.show()
df.plot.scatter(x='DEP_DELAY', y='ARR_DELAY')
plt.show()