import pandas as pd
import numpy as np
df = pd.read_csv(r"C:\Users\ngchi\Desktop\Default_data\employee.csv")
pd.set_option('display.max_rows', df.shape[0]+1)

df = df.drop_duplicates()
df = df.dropna()

df.to_csv('employee_cleaned_data.csv',index=False)
