# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path
data = pd.read_csv(path)
#Code starts here
data = data.rename(columns={'Total':'Total_Medals'})
data.head(10)


# --------------
#Code starts here


#better_event_dict = {'Season': {data['Total_Summer']:'Summer', data['Total_Winter']: 'Winter'}}
#better_event_df = pd.DataFrame(better_event_dict, columns = ['Season'])

data['Better_Event'] = np.where(data['Total_Summer']==data['Total_Winter'],'Both',np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter'))
#data['Better_Event'] = np.where(data['Total_Summer']<data['Total_Winter'],'Winter',np.nan)
#data['Better_Event'] = np.where(data['Total_Summer']==data['Total_Winter'],'Both',np.nan)
better_event = data['Better_Event'].value_counts().index[0]
print(better_event)
print(data['Better_Event'])


# --------------
#Code starts here




top_countries = data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]
top_countries.drop(top_countries.tail(1).index,inplace=True)
def top_ten(top_countries,col_name):
    country_list = []
    top = top_countries.nlargest(10,col_name)
    country_list = list(top['Country_Name'])
    return country_list
top_10_summer = list(top_ten(top_countries,'Total_Summer'))
top_10_winter = list(top_ten(top_countries,'Total_Winter'))
top_10 = list(top_ten(top_countries,'Total_Medals'))

common_array = np.intersect1d(top_10_summer, top_10_winter)
common = list(np.intersect1d(common_array, top_10))
print(common)
print(top_10_summer, top_10_winter, top_10)


# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]
summer_df.plot.bar(x='Country_Name',y='Total_Summer')
winter_df.plot.bar(x='Country_Name',y='Total_Winter')
top_df.plot.bar(x='Country_Name',y='Total_Medals')


# --------------
#Code starts here


summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = summer_df['Country_Name'][summer_df['Golden_Ratio']==summer_max_ratio].values

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = winter_df['Country_Name'][winter_df['Golden_Ratio']==winter_max_ratio].values

top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = top_df['Country_Name'][top_df['Golden_Ratio']== top_max_ratio].values

summer_country_gold = ''.join(map(str,summer_country_gold))
winter_country_gold = ''.join(map(str,winter_country_gold))
top_country_gold = ''.join(map(str,top_country_gold))

print(summer_country_gold, winter_country_gold,top_country_gold)


# --------------
#Code starts here
data.drop(data.tail(1).index,inplace=True)
data_1 = pd.DataFrame(data)

data_1['Total_Points'] = data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total']*1

most_points = data_1['Total_Points'].max()
best_country = data_1['Country_Name'][data_1['Total_Points']==data_1['Total_Points'].max()].values
best_country = ''.join(map(str,best_country))


# --------------
#Code starts here
best = pd.DataFrame(data[data['Country_Name']==best_country])
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation = 45)


