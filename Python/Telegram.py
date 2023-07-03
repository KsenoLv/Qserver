# This script allows you send any information from yours DB to telegram channel.

import psycopg2
import requests
from datetime import datetime

def send_to_telegram(message, text):
    # connect to Telegram
    apiToken = 'Yours API telegram token'
    chatID = '123456789'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': f"{text}\n{message}"})
        print(response.text)
    except Exception as e:
        print(e)

def execute_select_statement():
    try:
        # connect to PostgreSQL database
        conn = psycopg2.connect(
        host="111.111.111.11",
        database="Your_DB",
        user="user_name",
        password="password"
        )
        cursor = conn.cursor()

        # execute select statement
        cursor.execute(" QUERY INFORMATION TO BE SEND ")

        # fetch all rows
        rows = cursor.fetchall()

        # format rows as a string
        result = ""
        for row in rows:
            result += f"{datetime.strftime(row[0], '%Y-%m-%d')}: {row[1]}\n"

        # send result to Telegram
        send_to_telegram(result, "NAME OF MESSAGE:")

        # close cursor and connection
        cursor.close()
        conn.close()

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

if __name__ == '__main__':
    execute_select_statement()