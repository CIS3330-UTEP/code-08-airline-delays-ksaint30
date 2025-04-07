import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as sm_api

file = './Flight_Delays_2018.csv'
df = pd.read_csv(file)

model = sm_api.ols('DISTANCE ~ C(OP_CARRIER_NAME)', data=df).fit()
anova_table = sm.stats.anova_lm(model,type=2)
print(anova_table)
# Higher F value means Lesser the vairance, If they were equalized, F value will be 1
# PR value would be Significant, Less then 0.5 means theres variance