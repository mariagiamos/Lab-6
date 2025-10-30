print("lab 6")

#1
#Are population size and healthcare resources balanced across the contries?
#is there a correlation between internet usage and ,ale life expectancy?
#do females or males have a higher life expenctancy in regions?

#2
import pandas as pd
wdi_wide=pd.read_csv("wdi_wide.csv")
print(wdi_wide)

#3
#step 1, show data size and data types
wdi_wide.info()
#Empty Values=Total entries-Non null count
#Physicians= 217-207=10
#Population= 217-217=0

#4
print(wdi_wide.nunique())

