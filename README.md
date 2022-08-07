# ibm-data-engineering
A collection of self-driven data engineering exercises, from IBM's Coursera course on data engineering with Python.

1. The first small exercise was to scrape a website for data related to banks and their respective market cap. The python script for
this exercise can be found in the web_scraper folder. The data was retrieved using the requests library, processed using BeautifulSoup, 
cleaned, presented in a pandas dataframe and finally exported as a csv file. The end product csv file can be found in the final_ETL folder (bank_market_cap.csv).

2. The second exercise was to grab data related to exchange rates from an API. The python script for this exercise can be found in the API_extract folder.
Once again, data was processed accordingly and exported as a csv file that can be found in the final_ETL folder (exchange_rates_1.csv)

3. The final exercise is a small ETL process. The python script for this exercise can be found in the final_ETL folder (ETL.py). Data is extracted from
the previously generated csv files, and transformations are done to beautify the data and also calculate the market cap in terms of British pounds instead of the
original USD, and finally the cleaned data is loaded into a csv (bank_market_cap_gbp.csv)
