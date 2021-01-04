#import pandas
import pandas as pd
import matplotlib.pyplot as plt
#read the csv that's online
covid_csv = pd.read_csv("https://covid.ourworldindata.org/data/owid-covid-data.csv")
#cut down on the needless columns
new_covid_csv = covid_csv[['location', 'date', 'new_cases', 'new_deaths']]

#Choose a country
print ('Choose a country')
variable = input()

#cut out the needless rows
covid_uk = new_covid_csv[(new_covid_csv.location == variable)]

#plot!
covid_uk.plot(x = 'date', y = 'new_cases', kind = 'line')
covid_uk.plot(x = 'date', y = 'new_deaths', kind = 'line')
plt.show()