# Detailed description you can read in my blog: 
# https://psql.pro/data-parsing-with-python-scripts/

from pandas_datareader import data as pdr
import datetime as dt
import schedule


def time():
    end = dt.datetime.now()
    print('Time test', end)


def nyse():
    with open(r'C:\Pdata\NYSE\OUT\nyse_ticker.txt') as file:
        stocks = eval(file.read())
    directory = (r'C:\Pdata\NYSE\IN\\')
    file_name = 'nyse_data_new.csv'
    end = dt.datetime.now()
    start = dt.datetime(2023, 1, 20)
    for item in stocks:
        df = pdr.get_data_yahoo(symbols=stocks, start=start).stack("Symbols")
        df.to_csv(directory + file_name)
        print('NYSE DONE', end)

def nyse_error():
    with open(r'C:\Pdata\NYSE\OUT\error.csv') as file:
        stocks = eval(file.read())
    directory = (r'C:\Pdata\NYSE\IN\\')
    file_name = 'nyse_error.csv'
    end = dt.datetime.now()
    start = dt.datetime(2023, 1, 20)
    for item in stocks:
        df = pdr.get_data_yahoo(symbols=stocks, start=start).stack("Symbols")
        df.to_csv(directory + file_name)
        print('NYSE error DONE', end)


def main():
    schedule.every(1).hour.do(time)
    schedule.every().day.at('03:10').do(nyse)
    schedule.every().day.at('07:01').do(nyse_error)

    while True:
        schedule.run_pending()


if __name__ == '__main__':
    main()