print("lab 6")

#1
#Are population size and healthcare resources balanced across the contries?
#is there a correlation between internet usage and ,ale life expectancy?
#do females or males have a higher life expenctancy in regions?

#2
import pandas as pd
wdi_wide=pd.read_csv("wdi_wide.csv")
print(wdi_wide)
import seaborn as sns

#3
#step 1, show data size and data types
print(wdi_wide.info())
#Empty Values=Total entries-Non null count
#Physicians= 217-207=10
#Population= 217-217=0

#4
print(wdi_wide.nunique())

#5
print(wdi_wide.describe())
#this output of this fuction describes the statistics of the GNI and the high income economy.
#it shows the count (number of non empty values), mean (average GNI and income), the standard deviation, the minimum value, 25% percentile , 50% (median), 75% percentile and the maximum value. 

#6
#creating a new column GNI per capita
wdi_wide["GNI per capita"]=wdi_wide["GNI"]/wdi_wide["Population"]

#rounding to the nearest cent
print(wdi_wide["GNI per capita"].round())

#7
#a. how many contries are in each region?
print(wdi_wide["Region"].value_counts())


#b . how many high incomes are there?
print(wdi_wide["High Income Economy"].value_counts())
#150 where high income= 0, 67 where high income=1
#africa=54,asia=50, europe=47, americas=46, oceania=19

#8 where are the high income economies (per region)
print(pd.crosstab(wdi_wide["High Income Economy"], wdi_wide["Region"]))

#9
# we can filter only the countries where women live more than 80 years.
# This is done without a loop — pandas does it for us super fast.
filtered = wdi_wide[wdi_wide["Life expectancy, female"] > 80]

# Print how many countries fit the condition
# The len() function counts how many countries meet that condition.
print("Number of countries where women live more than 80 years:", len(filtered))

# And now we need to print out the actual country names along with the female life expectancy.
# This helps us double-check which ones they are and what their values look like.
print(filtered[["Country Name", "Life expectancy, female"]])

#Part 4




      
      
      
      
                  
                  
      











