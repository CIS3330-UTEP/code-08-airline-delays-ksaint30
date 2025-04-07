import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as sm_api
import matplotlib.pyplot as plt
#  determine if there is sig difference 
file = './demos/cars.csv'
df = pd.read_csv(file)

query = "Identification_Make == 'Toyota' or Identification_Make == 'Mazda' or Identification_Make == 'Honda'"
df = df.query(query)

model = sm_api.ols('Dimensions_Length ~ C(Identification_Make)', data=df).fit()
anova_table = sm.stats.anova_lm(model,type=2)
print(anova_table)


df.boxplot(column="Dimensions_Length" , by='Identification_Make')
plt.xticks(rotation=90)#Rotates the x names 
plt.show()
# Low P value : no difference between values, No hypothesis
# Anova isn't showing who is the Problem child
# Tukey : Needs to run subsequent test to tell which is Different then the others
