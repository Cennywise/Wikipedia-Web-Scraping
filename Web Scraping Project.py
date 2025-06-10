from requests import get
from bs4 import BeautifulSoup
import pandas as pd

#Get site info
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = get(url)

#Get table data
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find('table') #This is actaully a list, so you could use find_all with an index to get a specific table from multiple.
world_titles = table.find_all('th')
world_table_titles = [title.text.strip() for title in world_titles] #.strip() gets rid of the newline characters

#Create data frame
df = pd.DataFrame(columns = world_table_titles)

#Add table data to data frame
column_data = table.find_all('tr')
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    length = len(df)
    df.loc[length] = individual_row_data

#Export data from as csv
df.to_csv(r'C:\Users\cenny\Documents\Data Analyist Bootcamp\Web Scraping\Companies.csv', index = False)
