import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("canadian_immigration_data.csv")

years = list(map(str, range(1980, 2014)))

top_6_countries = data.nlargest(6, 'Total')[['Country'] + years]
top_6_countries.set_index('Country', inplace=True)
top_6_1990_2013 = top_6_countries.loc[:, '1990':'2013'].transpose()

top_6_1990_2013.plot(kind='area', stacked=True, alpha=0.7, figsize=(10, 6))
plt.title('Top 6 Immigrant Countries (1990-2013)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Immigrants', fontsize=12)
plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(alpha=0.5)
plt.tight_layout()
plt.show()

india_data = data.loc[data['Country'] == 'India', years].transpose()
india_data.columns = ['Immigrants']

india_data.plot(kind='bar', color='skyblue', figsize=(10, 6), legend=False)
plt.title('Immigration from India (1980-2013)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Immigrants', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

countries = ['India', 'Philippines', 'China']
selected_data = data[data['Country'].isin(countries)].set_index('Country')[years].transpose()

selected_data.plot(kind='box', vert=False, figsize=(10, 6), color=dict(boxes='blue', whiskers='black', medians='red', caps='green'))
plt.title('Immigration from India, Philippines, and China (1980-2013)', fontsize=14)
plt.xlabel('Immigrants', fontsize=12)
plt.tight_layout()
plt.show()

india_france_total = data[data['Country'].isin(['India', 'France'])][['Country', 'Total']].set_index('Country')
india_france_total.plot(kind='area', alpha=0.7, figsize=(8, 5), color=['skyblue', 'lightgreen'])
plt.title('Total Immigration from India and France', fontsize=14)
plt.ylabel('Total Immigrants', fontsize=12)
plt.tight_layout()
plt.show()

india_france_total['Total'].plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['skyblue', 'lightgreen'], figsize=(6, 6))
plt.title('Proportion of Immigration (India vs France)', fontsize=14)
plt.ylabel('')
plt.tight_layout()
plt.show()

fiji_singapore = data[data['Country'].isin(['Fiji', 'Singapore'])][['Country', '2013']].set_index('Country')

plt.scatter(fiji_singapore.index, fiji_singapore['2013'], color=['blue', 'orange'], s=100)
plt.title('Immigrants from Fiji and Singapore (2013)', fontsize=14)
plt.xlabel('Country', fontsize=12)
plt.ylabel('Immigrants', fontsize=12)
plt.grid(alpha=0.5)
plt.tight_layout()
plt.show()
