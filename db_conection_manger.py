#Using SQL Lite to avoid RAM overlaoding with cache 
import sqlite3


# Getting connection for SQL - Lite 
# TODO: Update to MySQL 
timeframe = '2015-05'
connection = sqlite3.connect('{}.db'.format(timeframe))


#TODO: Change camle cases to under score naming
dbCoursor = connection.cursor()