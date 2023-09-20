import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


def connectToSql():
    mydb = mysql.connector.connect(
        host="localhost",
        port=3406,
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
    )
    return mydb
