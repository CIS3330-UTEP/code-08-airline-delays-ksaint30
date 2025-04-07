import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as sm_api
import matplotlib.pyplot as plt
#If any of this libraries is missing from your computer. Please install them using pip.

filename = 'Flight_Delays_2018.csv'
df = pd.read_csv(filename)
query = "FL_Date == 'ARR_DELAY' or FL_Date == 'DEP_DELAY' or FL_Date == 'WEATHER_DELAY'"
df.query(query, inplace=True)

model = sm_api.ols('DISTANCE ~ C(ARR_DELAY)', data=df).fit()
anova_table = sm.stats.anova_lm(model,type=2)
print(anova_table)
#ARR_DELAY is the column name that should be used as dependent variable (Y).