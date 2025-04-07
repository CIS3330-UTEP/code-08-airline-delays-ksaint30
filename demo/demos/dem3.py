import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as sm_api
import matplotlib.pyplot as plt
file = './Flight_Delays_2018.csv'
df = pd.read_csv(file)

query = "OP_CARRIER == 'AA' or OP_CARRIER == 'DL' or OP_CARRIER == 'UA'"
# inplace instead of df= will change df within this file, so does not need to store it in df variable
df.query(query, inplace=True)

model = sm_api.ols('DISTANCE ~ C(OP_CARRIER_NAME)', data=df).fit()
anova_table = sm.stats.anova_lm(model,type=2)
print(anova_table)
# Higher F value means Lesser the vairance, If they were equalized, F value will be 1
# PR value would be Significant, Less then 0.5 means theres variance

df.boxplot(column="DISTANCE" , by='OP_CARRIER_NAME')
plt.xticks(rotation=90)
plt.show()