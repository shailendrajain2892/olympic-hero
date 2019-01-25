# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data.rename(columns={'Total':"Total_Medals"}, inplace=True)
print(data.head(10))



# --------------
#Code starts here
data['Better_Event'] = np.where(data['Total_Summer']>=data['Total_Winter'],
                                (np.where(data['Total_Summer']==data['Total_Winter'], "Both", "Summer")), 'Winter')

better_event = data['Better_Event'].value_counts().index[0]


# --------------
#Code starts here
top_countries = data[
    ['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries.drop(top_countries.tail(1).index, inplace=True)

def top_ten(top_countries, column):
    top_10_data =  top_countries.nlargest(10, column)
    return top_10_data['Country_Name'].tolist()

top_10_summer = top_ten(top_countries, 'Total_Summer')
top_10_winter = top_ten(top_countries, 'Total_Winter')
top_10 = top_ten(top_countries, 'Total_Medals')
common = list(set(top_10_summer).intersection(set(top_10_winter), set(top_10)))
print(common)



# --------------
#Code starts here
df_countries_tuple = zip(['summer_df', 'windter_df', 'top_df'],
                    [top_10_summer, top_10_winter, top_10])
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

plt.bar(top_10_summer, summer_df['Total_Summer'])
plt.xticks(rotation=45)
plt.xlabel("top 10 Summer Country")
plt.show()

plt.bar(top_10_winter, winter_df['Total_Winter'])
plt.xticks(rotation=45)
plt.xlabel("top 10 Winter Country")
plt.show()

plt.bar(top_10, top_df['Total_Medals'])
plt.xticks(rotation=45)
plt.xlabel("top 10  Country")
plt.show()


# --------------
#Code starts here

summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'].idxmax(), 'Country_Name']
print(summer_max_ratio, summer_country_gold)

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/summer_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax(), 'Country_Name']
print(winter_max_ratio, winter_country_gold)

top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax(), 'Country_Name']
print(top_max_ratio, top_country_gold)


# --------------
#Code starts here
data_1 = data.drop(data.tail(1).index)
data_1['Total_Points'] = data_1['Gold_Total']*3+data_1['Silver_Total']*2+data_1['Bronze_Total']
#print(data_1.head())
best_country = data_1.loc[data_1['Total_Points'].idxmax(), 'Country_Name']
most_points = data_1['Total_Points'].max()
print(best_country)
print(most_points)


# --------------
#Code starts here
best = data[data['Country_Name']==best_country]
best = best[['Gold_Total', 'Silver_Total', 'Bronze_Total']]
best.plot.bar()
plt.xlabel("United States")
plt.ylabel("Medals Tally")
plt.xticks(rotation=45)
plt.show()


