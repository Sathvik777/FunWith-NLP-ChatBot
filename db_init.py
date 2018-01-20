#Using SQL Lite to avoid RAM overlaoding with cache 
import sqlite3

import json
from datetime import datetime

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

