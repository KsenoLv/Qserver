# Project Overview

This project is a 24/7 fully automated quotes server for any financial instrument on any market. It allows you to download quotes information from Yahoo Finance.

## Installation Instructions

To set up the project, you will need a VPS (Virtual Private Server) running Ubuntu and the latest version of Python and PostgreSQL installed on it.

Clone the repository to your VPS server or copy the files from your local machine. Make sure to update the folder paths and file names in the script as needed.

```git clone https://github.com/KsenoLv/Qserver```

## Configuration

### Python folder

- **BeautifulSoup.py:** This script uses the BeautifulSoup library for web scraping and is fully functional. It extracts quotes from Yahoo Finance. 
- **Pandas.py:** This script uses the Pandas library. However, since December 2022, it has encountered various errors when trying to parse data from Yahoo Finance. Therefore, it might have some bugs.

- **Main_template.py:** Template to execute queries via Python.

- **Telegram.py:** Server monitoring via Telegram.

### SQL folderr

- **Tables.sql:** Scripts for database tables.

- **Requests.sql:** Python scripts for the database.

- **Data.sql:** Scripts to manipulate data in the database.

- **Audit.sql:** For checking and correcting missing data.

## Data Scraping

- **BeautifulSoup.py:** This script utilizes the BeautifulSoup library to extract quotes from Yahoo Finance. It is fully functional and can be used for web scraping. <br> For a detailed description, visit [here](https://psql.pro/market-data-with-python-and-beautifulsoup/).

- **Pandas.py:** This script utilizes the Pandas library. However, since December 2022, it has encountered various errors when trying to parse data from Yahoo Finance. As a result, it may contain some bugs. <br> For a detailed description, visit [here](https://psql.pro/data-parsing-with-python-scripts/).

Please note that web scraping should be used responsibly and within legal and ethical boundaries. Always ensure that you have proper authorization to access and extract data from websites before initiating any scraping activities.

## Step-by-Step Guide

For a detailed guide on setting up your personal server with quotes, visit:

1 - [Server set up – roadmap.](https://psql.pro/server-set-up-roadmap/)<br>
2 - [Server set up – python on Ubuntu with cron.](https://psql.pro/<br>python-on-ubuntu-with-cron/)<br>
3 - [Server set up – SQL DB part.](https://psql.pro/server-set-up-sql-part/)<br>
4 - [Server set up – SQL requests.](https://psql.pro/server-set-up-sql-requests/)<br>
5 - [Market Data with Python and Beautiful Soup.](https://psql.pro/market-data-with-python-and-beautifulsoup/)<br>
6 - [DATA scraping with Python scripts (Pandas).](https://psql.pro/data-parsing-with-python-scripts/)

If you prefer assistance in setting up the server, feel free to contact me, and I can help you for a small reward. Contact information is provided at the bottom of this document or in my web page: www.psql.pro

## Download

If you need all the data in the database, you can download it from Google Drive using the following link: [Gdrive](https://drive.google.com/drive/u/1/folders/1-PMDXtoVcRWZcoqAoYP5Zzs2fI1SlkHo). This file contains NYSE quotes on daily charts since May 9, 1983. It is updated monthly.

## Usage

Once PostgreSQL, Python, and the dependencies are set up, the server will run fully automated, requiring no daily manual monitoring. Integration with Telegram allows for monitoring the server and receiving daily messages with all the quotes fully automated.

## Dependencies

Make sure to install the following dependencies:

```
pip install requests
pip install beautifulsoup4
pip install pandas-datareader
pip install psycopg2
pip install telegram
pip install tqdm
```

## Contact Information

I am in Latvia, Riga.
Phone: +371 29720407
Email: ksenofontov.mihail@gmail.com
Telegram: https://t.me/psqlpro
WhatsApp: https://wa.me/+37129720407