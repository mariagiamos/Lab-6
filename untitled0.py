print("lab 6")

#1
#Are population size and healthcare resources balanced across the countries?
#is there a correlation between internet usage and male life expectancy?
#do females or males have a higher life expectancy in regions?

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
#this output of this function describes the statistics of the GNI and the high income economy.
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
#1
#plot for males
sns.relplot(data=wdi_wide, x="Life expectancy, male", y="GNI per capita", kind="scatter")

#plot for females
sns.relplot(data=wdi_wide, x="Life expectancy, female", y="GNI per capita", kind="scatter")

#2
#plot for males
sns.relplot(data=wdi_wide, x="Life expectancy, male", y="GNI per capita", kind="scatter", hue="Region")

#plot for females
sns.relplot(data=wdi_wide, x="Life expectancy, female", y="GNI per capita", kind="scatter", hue="Region")  

#3 (ask if its correct)
#plot for male with lines and standard deviation
sns.relplot(data=wdi_wide, x="Life expectancy, male", y="GNI per capita", kind="line", hue="Region", errorbar="sd")
#explain why it stays the same

#plot for female with lines and standard deviation
sns.relplot(data=wdi_wide, x="Life expectancy, female", y="GNI per capita", kind="line", hue="Region", errorbar="sd")

#4
#plot for males
sns.lmplot(data=wdi_wide, x="Life expectancy, male", y="GNI per capita", hue="Region")

#plot for females
sns.lmplot(data=wdi_wide, x="Life expectancy, female", y="GNI per capita", hue="Region")

#5
sns.relplot(data=wdi_wide, x="Life expectancy, female", y="Greenhouse gas emissions")
sns.relplot(data=wdi_wide, x="Life expectancy, male", y="Greenhouse gas emissions")
#There is no correlation between female or male life expectancy and greenhouse gas emissions.

sns.relplot(data=wdi_wide, x="Life expectancy, female", y="Internet use")
sns.relplot(data=wdi_wide, x="Life expectancy, male", y="Internet use")
#There is some correlation between female and male life expectancy with internet usage

#do greenhouse gases have an effect on female life expectancy
sns.relplot(data=wdi_wide, x="Life expectancy, female", y="Greenhouse gas emissions", col="Region", kind="scatter")
#Greenhouse gases do not have any correlation with female life expectancy

#does internet use have an effect on female life expectancy
sns.relplot(data=wdi_wide, x="Life expectancy, female", y="Internet use", col="Region", kind="scatter")
#Internet use has some correlation on female life expectancy. The internet is used throughout all kind of ages. 

#do physicians have an effect on female life expectancy
sns.relplot(data=wdi_wide, x="Life expectancy, female", y="Physicians", col="Region", kind="scatter")
#In asia, America, Oceania there is a slight correlation although in africa there is no correlation.

#does the Tertiary education for males have an effect on female life expectancy
sns.relplot(data=wdi_wide, x="Life expectancy, female", y="Tertiary education, male", col="Region", kind="scatter")
#There is a very weak correlation between tertiary education for males having an effect on female life expectancy in Asia, Oceania,Europe and america and close to no correlation in Africa.

#does high income economy have an effect on female life expectancy
sns.relplot(data=wdi_wide, x="Life expectancy, female", y="High Income Economy",col="Region", kind="scatter")
#In all regions,there is no effect and correlation between high income economy and female life expectancy.

#6
#a Is there any association between Internet use and emissions per capita?
#emission per capita = greenhouse gas emission/population
# Create a new column for emissions per capita
wdi_wide["emissions_per_capita"] = wdi_wide["Greenhouse gas emissions"] / wdi_wide["Population"]
# Then plot using the new column
sns.relplot(data=wdi_wide, x="Internet use", y="emissions_per_capita", hue="Region", kind="scatter")

#b Which are the countries with high emissions? (> 0.03)
# countries with high emissions
high_emissions = wdi_wide[wdi_wide["emissions_per_capita"] > 0.03]
print(high_emissions[["Country Name", "Region", "emissions_per_capita"]])

#c Is there much variation by region (with respect to high emissions vs Internet use)?
sns.relplot(data=high_emissions, x="Internet use", y="GNI per capita", kind="scatter", hue="Region")

#d Do all high income economies have high emissions?
sns.relplot(data=wdi_wide, x="High Income Economy", y="emissions_per_capita", hue="Region", kind="scatter")




      
      
      
      
                  
                  
      











