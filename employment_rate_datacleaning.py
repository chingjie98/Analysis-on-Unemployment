#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 16:28:23 2021

@author: joanntan
"""

import pandas as pd
df = pd.read_csv("/Users/joanntan/Desktop/PYTHON PROJECT/PART 2/employment_rate_orginaldata.csv")
df.duplicated() 
df.to_csv("employmentrate_cleaned_data.csv", index = False)