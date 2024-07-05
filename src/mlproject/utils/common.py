from dataclasses import dataclass
from pathlib import Path
from mlproject import logger
from dotenv import load_dotenv
import pandas as pd
import os
import pymysql


load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")

def read_sql_data():
    logger.info("Reading SQl database started")
    try:
        mydb=pymysql.connect(host=host, user=user, password=password, db=db)
        logger.info("Connection Established")
        df=pd.read_sql_query('Select * from student', con=mydb)
        print(df.head(2))
    except Exception as e:
        raise e
    return df
