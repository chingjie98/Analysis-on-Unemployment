
## A3 POSTER PAGE 1 (EMPLOYMENT TURNOVER RATE 2020)
# Note: If output prompts 'No such file in directory', kindly replace the file pathname in pd.read_csv.

import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt 
sb.set() #Set the default Seaborn style for graphics

df = pd.read_csv('/Users/joanntan/Desktop/PYTHON PROJECT/PART 2/employmentrate_cleaned_data.csv')
jan=df[df['month']==1]
feb=df[df['month']==2]
march=df[df['month']==3]
april=df[df['month']==4]
may=df[df['month']==5]
june=df[df['month']==6]
july=df[df['month']==7]
aug=df[df['month']==8]

month=df["month"].astype(str)
month=pd.DataFrame(month)
month=month.rename(columns={0: 'month'})


year_plot = pd.concat([month, df.drop(["year","month","day"],axis=1)], axis=1)

f, axes = plt.subplots(1, 1, figsize=(40, 20))

a=sb.lineplot(data=year_plot,x="month",y="emp_combined")
plt.setp(a.get_xticklabels())
plt.show()


