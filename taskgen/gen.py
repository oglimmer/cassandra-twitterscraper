import os
import mysql.connector, time
from dotenv import load_dotenv
load_dotenv()

START_TIME_UNIX = 1609455600
END_TIME_UNIX = 1640991600
TIME_PER_TASK = 3600
COMPANY_INT = 1
SEARCH_TERMS = ["elon musk", "tesla"]

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
cnx = connectToDatabase()

for t in SEARCH_TERMS:
    query("INSERT INTO search_terms (company, term) VALUES (%s, %s)", [COMPANY_INT, t], cnx)

while START_TIME_UNIX < END_TIME_UNIX:
    end = START_TIME_UNIX + TIME_PER_TASK
    if end > END_TIME_UNIX: end = END_TIME_UNIX
    query("INSERT INTO tasks (company, unix_start, unix_end) VALUES (%s, %s, %s);",
        [COMPANY_INT, START_TIME_UNIX, end], cnx)
    START_TIME_UNIX += TIME_PER_TASK