import mysql.connector
#from db import con

class Model():
    table_name = None
    def __init__(self):
        table_name = type(self).__name__

    def save(self):
        #con = con()
        properties = vars(self)
        propNum = len(properties)
        sqlQuery = "INSERT INTO %s (" + "%s,"*(propNum-1) + "%s) VALUES (" + "%s,"*(propNum-1) + "%s)"
