from bs4 import BeautifulSoup
import requests
import pandas as pd

#Website containing list of banks around the world and their respective market caps that we are going to scrape
html_data = requests.get('https://en.wikipedia.org/wiki/List_of_largest_banks').text
soup = BeautifulSoup(html_data, 'html.parser')
raw_data = []

#Store beautified row data in raw_data list
for row in soup.find_all('tbody')[3].find_all('tr'):
    col = row.find_all('td')
    raw_data.append(col)

master_list = []

#Iterate over raw data, process, and extract information on bank name and market cap
for i in raw_data[1:]:
    bank_name_dirty = str(i[1]).split('>')[-3]
    bank_name = bank_name_dirty[:len(bank_name_dirty)-3]
    amount_dirty = str(i[2]).split('<')[1]
    amount = amount_dirty[3:len(amount_dirty)].strip()
    master_list.append([bank_name, amount])

#Transfer data to dataframe, and then to csv
data = pd.DataFrame(master_list, columns=["Name", "Market Cap (US$ Billion)"])
data.to_csv('bank_market_cap.csv', index=False)