#Using SQL Lite to avoid RAM overlaoding with cache 
import sqlite3

import json
from datetime import datetime
import exploer_dataset

timeframe = '2015-05'
sql_transaction = []


# Getting connection for SQL - Lite 
# TODO: Update to MySQL 

connection = sqlite3.connect('{}.db'.format(timeframe))


#TODO: Change camle cases to under score naming
dbCoursor = connection.cursor()

def create_table():
    dbCoursor.execute("CREATE TABLE IF NOT EXISTS "+
    "parent_reply(parent_id TEXT PRIMARY KEY, comment_id TEXT UNIQUE, "+
    "parent TEXT, comment TEXT, subreddit TEXT, unix INT, score INT)")

if __name__ == '__main__':
    create_table()
    row_counter = 0
    paired_rows = 0

    with open('./chatdata/reddit_data/{}/RC_{}'.format(db_conection_manger.timeframe.split('-')[0],timeframe), buffering=1000) as f:
        for row in f:
            row_counter += 1
            row = json.loads(row)
            parent_id = row['parent_id']
            body = exploer_dataset.format_data(row['body'])
            created_utc = row['created_utc']
            score = row['score']
            comment_id = row['name']
            subreddit = row['subreddit']
