import pandas as pd

#Extracting data from previous csv files we have generated
bank_market_cap_df = pd.read_csv('bank_market_cap.csv')
exchange_rates_df = pd.read_csv('exchange_rates_1.csv', index_col=0)
pound_exchange_rate = exchange_rates_df['rates']['GBP']

def transform(df, pound_exchange_rate):
    '''
    Converts market cap from USD to pounds, rounds values to 3 decimal places, and renames the column title
    '''
    df['Market Cap (US$ Billion)'] = df['Market Cap (US$ Billion)'] * pound_exchange_rate
    df['Market Cap (US$ Billion)'] = df['Market Cap (US$ Billion)'].round(3)
    df.rename(columns={'Market Cap (US$ Billion)': 'Market Cap (GBP$ Billion)'}, inplace=True)

#Transforms data to a cleaner format based on GBP instead of USD
transform(bank_market_cap_df, pound_exchange_rate)

#Loads the data to a csv file
bank_market_cap_df.to_csv('bank_market_cap_gbp.csv')



