-- Detailed description you can read in my blog: 
-- https://psql.pro/server-set-up-sql-part/

-- Adding new date to table nyse.nyse_data_new
select * from nyse.load_csv_files();

-- This script copy all new data from from nyse.nyse_data_new to nyse.nyse_data
-- In the same time its rounded quotes to 4 dec.
WITH rounded_values AS (SELECT ticker, date, ROUND(open, 4) AS rounded_close, ROUND(High, 4) AS rounded_high, ROUND(Low, 4) AS rounded_low, ROUND(Close, 4) AS rounded_open FROM nyse.nyse_data_new WHERE date BETWEEN CURRENT_DATE-2 AND CURRENT_DATE) INSERT INTO nyse.nyse_data (date, symbols, Open, High, Low, Close) SELECT rv.date, rv.ticker, rv.rounded_close, rv.rounded_high, rv.rounded_low, rv.rounded_open FROM rounded_values rv WHERE NOT EXISTS (SELECT 1 FROM nyse.nyse_data nd WHERE nd.date = rv.date AND nd.symbols = rv.ticker);

-- This script compare all data and search for missing tickets.
-- If they exist, create file nyse_error_tickers_sql.csv for future checking.
COPY(select ticker FROM nyse.nyse_ticker_list WHERE ticker NOT IN (select symbols from nyse.nyse_data WHERE date=CURRENT_DATE-1 GROUP BY symbols)) TO '/var/lib/postgresql/nyse_error_tickers_sql.csv'

-- Telegram, if needet. That query returns and send via telegram how many tickers was scraped for two previous days.
SELECT date, count(*) FROM nyse.nyse_data group by date order by date desc limit 2