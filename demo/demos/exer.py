import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as sm_api
import matplotlib.pyplot as plt
#  determine if there is sig difference 
file = './demos/graduates_clean.csv'
df = pd.read_csv(file)
query = "Education_Major == 'Mechanical_Engineering' or Education_Major == 'Electrical_Engineering' or Education_Major == 'Civil_Engineering'"
df = df.query(query)
