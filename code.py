# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data = pd.read_csv(path)

#Code starts here
data.rename(columns = {"Total":"Total_Medals"}, inplace =True)
data.head(10)



# --------------
#Code starts here

data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'], 'Summer', 'Winter')
data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'], 'Both', data['Better_Event'])
better_event = data['Better_Event'].value_counts().index.values[0]

print('Better Event is: ', better_event)


# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]

top_countries = top_countries.drop(top_countries[top_countries.Country_Name == 'Totals'].index)

def top_ten(df, column_name):
    country_list = []
    top_10 = df.nlargest(10,column_name)
    country_list = list(top_10['Country_Name'])
    return country_list

top_10_summer = top_ten(top_countries,'Total_Summer')
top_10_winter = top_ten(top_countries,'Total_Winter')
top_10 = top_ten(top_countries,'Total_Medals')

common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))


# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

plt.figure(figsize=(20, 6))
plt.bar(summer_df['Country_Name'], summer_df['Total_Summer'])
plt.xlabel('Country Name') 
plt.ylabel('Total Medals in Summer') 
plt.title('Country vs Total Medals in Summer')
plt.show()

plt.figure(figsize=(20, 6))
plt.bar(winter_df['Country_Name'], winter_df['Total_Winter'])
plt.xlabel('Country Name') 
plt.ylabel('Total Medals in Winter') 
plt.title('Country vs Total Medals in Winter')
plt.show()

plt.figure(figsize=(20, 6))
plt.bar(top_df['Country_Name'], top_df['Total_Medals'])
plt.xlabel('Country Name') 
plt.ylabel('Total Medals') 
plt.title('Country vs Total Medals')
plt.show()


# --------------
#Code starts here

summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']

summer_max_ratio = summer_df['Golden_Ratio'].max()
print(summer_max_ratio)
summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'].idxmax, 'Country_Name']
print(summer_country_gold)

winter_max_ratio = winter_df['Golden_Ratio'].max()
print(winter_max_ratio)
winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax, 'Country_Name']
print(winter_country_gold)

top_max_ratio = top_df['Golden_Ratio'].max()
print(top_max_ratio)
top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax, 'Country_Name']
print(top_country_gold)



# --------------
#Code starts here

data_1 = data[:-1]
data_1['Total_Points'] = data_1['Gold_Total'] *3 + data_1['Silver_Total'] *2 + data_1['Bronze_Total'] *1

most_points = data_1['Total_Points'].max()
print(most_points)

best_country = data_1.loc[data_1['Total_Points'].idxmax, 'Country_Name']
print(best_country)



# --------------
#Code starts here

best = data_1[data_1['Country_Name'] == best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]

best.plot.bar(stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)
l=plt.legend()

l.get_texts()[0].set_text('Gold_Total :' + str(best['Gold_Total'].values))
l.get_texts()[1].set_text('Silver_Total :' + str(best['Silver_Total'].values))
l.get_texts()[2].set_text('Bronze_Total :' + str(best['Bronze_Total'].values))

plt.show()


