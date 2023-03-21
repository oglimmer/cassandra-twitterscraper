import os, sys
import mysql.connector, time
from dotenv import load_dotenv
load_dotenv()

START_TIME_UNIX = time.time()
END_TIME_UNIX = START_TIME_UNIX + 86400 # 1 day
TIME_PER_TASK = 3600 # 1 hour
COMPANY_INT = 1

def connectToDatabase():
    return mysql.connector.connect(
        user=os.getenv("DATABASEUSR"), 
        password=os.getenv("DATABASEPW"),
        host=os.getenv("DBHOST"),
        database=os.getenv("DBNAME")
    )
def query(q, p, cnx):
    cursor = cnx.cursor()
    cursor.execute(q, p)
    cursor.close()
    cnx.commit()

if __name__ == '__main__':

    if os.getenv("INIT") != "True":

        cnx = connectToDatabase()

        for t in os.getenv("SEARCH_TERMS").split(','):
            query("INSERT INTO search_terms (company, term) VALUES (%s, %s)", [COMPANY_INT, t], cnx)

        while START_TIME_UNIX < END_TIME_UNIX:
            end = START_TIME_UNIX + TIME_PER_TASK
            if end > END_TIME_UNIX: end = END_TIME_UNIX
            query("INSERT INTO tasks (company, unix_start, unix_end) VALUES (%s, %s, %s);",
                [COMPANY_INT, START_TIME_UNIX, end], cnx)
            START_TIME_UNIX += TIME_PER_TASK
