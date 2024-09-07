######################################################################################################
#
# This script contains various functions that can be used for financial analysis of the stock market.
#
# Other use cases pending...
#
######################################################################################################
import yfinance as yf
import pandas as pd
import os



""" 
This function uses yfinance to retrieve the stock data (price at open/close, volumne, high, low)

Outputs a csv of the data in the scripts root folder

"""
def get_stock_data(tickers, start_date, end_date):
    df_list = []
    for ticker in tickers:
        # Using yfinance to fetch the data
        df = yf.download(ticker, start=start_date, end=end_date)
        df['Ticker'] = ticker
        df_list.append(df)

    # Combine the dataframes
    dfs = pd.concat(df_list)

    # Create a CSV and write the data to it
    counter = 1
    base_csv_name = 'Stock Data'
    while os.path.isfile(f'{base_csv_name} {counter}.csv'):
        counter += 1
    output_filename = f'{base_csv_name} {counter}.csv'
    dfs.to_csv(output_filename)   

    return dfs, df_list


def main():

    while True:
        function_input = input('Which function would you like to use?\n'\
                            'Q - Quit\n'\
                            '1 - Get stock data\n'\
                            'Function: ')
        
        if function_input.lower().strip() == 'q':
            print('Ending program')
            break

        # Function 1: Retrieve stock data
        if function_input.strip() == '1':
            ticker_input = input('Enter ticker(s) separated by commas: ')
            ticker_lst = ticker_input.upper().split(',')
            ticker_lst = [tic.strip() for tic in ticker_lst if tic != '']
            start_input = input('Enter start date (e.g. 2020-01-31): ')
            end_input = input('Enter start date (e.g. 2020-12-31): ')
            print('Fetching stock data...')
            get_stock_data(ticker_lst, start_input, end_input)
            
             

if __name__ == "__main__":
    main()


