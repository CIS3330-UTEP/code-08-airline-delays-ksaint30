import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as sm_api
import matplotlib.pyplot as plt
#If any of this libraries is missing from your computer. Please install them using pip.

# Descriptive find shapes, patterns, and trends in the data. 
filename = 'Flight_Delays_2018.csv'
df = pd.read_csv(filename)
smol_df = df[df['ARR_DELAY']<40]
print(smol_df)
df = df.query("DEP_DELAY > 0 or ARR_DELAY > 0")
# Used Excel function: Median for Arrival delay = 40 
df.boxplot(column="ARR_DELAY")
plt.show()
df.plot.scatter(x='DEP_DELAY', y='ARR_DELAY')
plt.show()

# # Predictive using statsmodels.api and ordinary least squares (OLS).
model = sm_api.ols('ARR_DELAY ~ C(OP_CARRIER_NAME)', data=df).fit()
anova_table = sm.stats.anova_lm(model,type=2)
print(anova_table)
# #ARR_DELAY is the column name that should be used as dependent variable (Y).