
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\ngchi\Desktop\File for Part 2\employee_cleaned_data.csv")
df_without_termination = df[df["Attrition"] != "Termination"]
df_only_resignation = df[df["Attrition"] == "Voluntary Resignation"]
df_resigned = df[df["Attrition"] == "Voluntary Resignation"]
df_employed = df[df["Attrition"] == "Current employee"]


# Average Environment Satisfaction Graph


bar_EnvironmentSatisfaction = df.groupby("Attrition").EnvironmentSatisfaction.mean().sort_values(ascending = True).plot(kind = "bar",figsize = (7,6),color = ["yellowgreen","Steelblue","Skyblue"],width = 0.8)
bar_EnvironmentSatisfaction.set_ylabel("Environment Satisfaction", fontsize = 18)
bar_EnvironmentSatisfaction.set_xlabel("")
bar_EnvironmentSatisfaction.set_title("Average Environment Satisfaction",fontsize = 22)
bar_EnvironmentSatisfaction.set_ylim(0,4)
bar_EnvironmentSatisfaction.set_xticklabels(["Terminated","Resigned","Current Employees"],size=14,rotation = 0)
bar_EnvironmentSatisfaction.set_yticklabels([0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0],size=15)


# % Of Experience with OverTime Graph


bar_OverTime = df.groupby("Attrition").OverTime.mean().sort_values(ascending = False).plot(kind = "bar",figsize = (7,6),color = ["Skyblue","Steelblue","yellowgreen"],width = 0.8)
bar_OverTime.set_ylabel("OverTime", fontsize = 18)
bar_OverTime.set_title("% of Experience with OverTime",fontsize = 22)
bar_OverTime.set_xlabel("")
bar_OverTime.set_ylim(0,1)
bar_OverTime.set_xticklabels(["Terminated","Resigned","Current Employees"],size=14,rotation = 0)
bar_OverTime.set_yticklabels(["0%","20%","40%","60%","80%","100%"],size=15)


# Average Relationship Satisfaction Graph


bar_RelationshipSatisfaction = df.groupby("Attrition").RelationshipSatisfaction.mean().sort_values(ascending = True).plot(kind = "bar",figsize = (7,6),color = ["Skyblue","Steelblue","yellowgreen"],width = 0.8)
bar_RelationshipSatisfaction.set_ylabel("Relationship Satisfaction", fontsize = 18)
bar_RelationshipSatisfaction.set_title("Average Relationship Satisfaction",fontsize = 22)
bar_RelationshipSatisfaction.set_xlabel("")
bar_RelationshipSatisfaction.set_ylim(0,4)
bar_RelationshipSatisfaction.set_xticklabels(["Terminated","Current Employees","Resigned"],size=14,rotation = 0)
bar_RelationshipSatisfaction.set_yticklabels([0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0],size=15)


# Average Work Life Balance Graph


bar_WorkLifeBalance = df.groupby("Attrition").WorkLifeBalance.mean().sort_values(ascending = True).plot(kind = "bar",figsize = (7,6),color = ["Skyblue","Steelblue","yellowgreen"],width = 0.8)
bar_WorkLifeBalance.set_ylabel("Work Life Balance", fontsize = 18)
bar_WorkLifeBalance.set_title("Average Work Life Balance",fontsize = 22)
bar_WorkLifeBalance.set_ylim(0,4)
bar_WorkLifeBalance.set_xlabel("")
bar_WorkLifeBalance.set_xticklabels(["Resigned","Terminated","Current Employees"],size=14,rotation=0)
bar_WorkLifeBalance.set_yticklabels([0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0],size=15)


# Average Job Involvement Graph


bar_JobInvolvement = df.groupby("Attrition").JobInvolvement.mean().sort_values(ascending = True).plot(kind = "bar",figsize = (7,6),color=["yellowgreen","Steelblue","Skyblue"],width = 0.8)
bar_JobInvolvement.set_ylabel("Job Involvement", fontsize = 18)
bar_JobInvolvement.set_title("Average Job Involvement",fontsize = 22)
bar_JobInvolvement.set_ylim(0,4)
bar_JobInvolvement.set_xlabel("")
bar_JobInvolvement.set_xticklabels(["Terminated","Resigned","Current Employees"],size=14,rotation = 0)
bar_JobInvolvement.set_yticklabels([0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0],size=15)



# Average Monthly Income Graph


bar_MonthlyIncome = df.groupby("Attrition").MonthlyIncome.mean().sort_values(ascending = True).plot(kind = "bar",figsize = (7,6),color=["yellowgreen","Steelblue","Skyblue"],width = 0.8)
bar_MonthlyIncome.set_ylabel("Monthly Income", fontsize = 18)
bar_MonthlyIncome.set_title("Average Monthly Income",fontsize = 22)
bar_MonthlyIncome.set_xlabel("")
bar_MonthlyIncome.set_xticklabels(["Terminated","Resigned","Current Employees"],size=14,rotation=0)
bar_MonthlyIncome.set_yticklabels([0,1000,2000,3000,4000,5000,6000,7000],size=15)

