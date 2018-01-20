import json
from datetime import datetime
import db_conection_manger

def format_data(data):
    data = data.replace('\n',' newlinechar ').replace('\r',' newlinechar ').replace('"',"'")
    return data

parent_data = find_parent_data('')


def find_parent_data(parent_id):
    try:
        sql = "SELECT comment FROM parent_reply WHERE comment_id = '{}' LIMIT 1".format(pid)
        db_conection_manger.dbCoursor.execute(sql)
        result = db_conection_manger.dbCoursor.fetchone()
        if result != None:
            return result[0]
        else: return False
    except Exception as e:
        #print(str(e))
        return False
