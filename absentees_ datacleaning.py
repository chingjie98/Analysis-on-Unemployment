import pandas as pd
import numpy as np
df = pd.read_csv("absentees_originaldata.csv")
df = df.drop_duplicates() #remove 34 rows
df = df.dropna()  #did nothing
df["Day of the week"].replace([2,3,4,5,6],["Monday","Tuesday","Wednesday","Thursday","Friday"],inplace=True)
df["Reason for absence"].replace(0,np.NaN,inplace=True) #706 rows
df["Month of absence"].replace(0,np.NaN,inplace = True)
df["Disciplinary failure"].replace(1,"yes",inplace=True)
df["Disciplinary failure"].replace(0,"no",inplace=True)
df["Social drinker"].replace(1,"yes",inplace = True)
df["Social drinker"].replace(0,"no",inplace = True)
df["Social smoker"].replace(1,"yes",inplace = True)
df["Social smoker"].replace(0,"no",inplace = True)
df["Reason for absence"].replace([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22, 23, 24, 25, 26, 27, 28],["Certain infectious and parasitic diseases", "Neoplasms", "Diseases of the blood and blood-forming organs and certain disorders involving the immune mechanism", "Endocrine, nutritional and metabolic diseases", "Mental and behavioural disorders", "Diseases of the nervous system", "Diseases of the eye and adnexa", "Diseases of the ear and mastoid process", "Diseases of the circulatory system", "Diseases of the respiratory system", "Diseases of the digestive system", "Diseases of the skin and subcutaneous tissue", "Diseases of the musculoskeletal system and connective tissue", "Diseases of the genitourinary system", "Pregnancy, childbirth and the puerperium", "Certain conditions originating in the perinatal period", "Congenital malformations, deformations and chromosomal abnormalities", "Symptoms, signs and abnormal clinical and laboratory findings, not elsewhere classified", "Injury, poisoning and certain other consequences of external causes", "External causes of morbidity and mortality", "Factors influencing health status and contact with health services", "Patient follow-up", "Medical consultation", "Blood donation", "Laboratory examination", "Unjustified absence", "Physiotherapy", "Dental consultation"],inplace = True)
df.rename(columns = {'Body mass index': 'BMI',"Absenteeism time in hours":"Absenteeism"}, inplace = True)
df.rename(columns = {'Work load Average/day ':'Workload'}, inplace = True)
df.dropna(inplace=True) #663 rows
df.to_csv('absentees_cleaned_data.csv',index=False)
