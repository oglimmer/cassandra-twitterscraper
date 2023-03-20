from flask import Flask, request
import mysql.connector.pooling, json, time, math, logging, os
from dotenv import load_dotenv
load_dotenv() 
log = logging.getLogger('werkzeug')
log.setLevel(logging.FATAL)

#AUTH HEADER
SECRET = os.getenv("SECRET")

#DATABASE STUFF
def connectToDatabase():
    dbconfig = {
        "user": os.getenv("DATABASEUSR"), 
        "password": os.getenv("DATABASEPW"),
        "host": os.getenv("DBHOST"),
        "database": os.getenv("DBNAME")
    }
    return mysql.connector.pooling.MySQLConnectionPool(
        pool_name="pool", pool_size=10, pool_reset_session=True, **dbconfig
    )
def query(q, p, cnxpool):
    cnx = cnxpool.get_connection()
    cursor = cnx.cursor()
    cursor.execute(q, p)
    toReturn = cursor.fetchall()
    cursor.close()
    cnx.commit()
    cnx.close()
    return toReturn
def queryS(q, p, cnxpool):
    cnx = cnxpool.get_connection()
    cursor = cnx.cursor()
    cursor.execute(q, p)
    cursor.close()
    cnx.commit()
    cnx.close()

cnx = connectToDatabase()

app = Flask("scraper-tasksapi")

@app.before_request
def before_request():
    try:
        if request.headers['AUTH'] != SECRET: return "", 403
    except: return "", 403

@app.route("/api/gettask", methods=["GET"])
def gettask():
    tasks =  query("SELECT id, unix_start, unix_end, company FROM tasks WHERE done = false AND time_started < %s LIMIT 1", 
    [math.floor(time.time())-10000], cnx)
    if len(tasks) != 1: return "", 404
    task = tasks[0]
    terms = query("SELECT term FROM search_terms WHERE company = %s", 
    [task[3]], cnx)
    returnobj = {
        "id": task[0],
        "unix_start": task[1],
        "unix_end": task[2],
        "company": task[3],
        "search_terms": [item for sublist in terms for item in sublist]
    }
    queryS("UPDATE tasks SET time_started = %s WHERE id = %s",[math.floor(time.time()), task[0]], cnx)
    return json.dumps(returnobj), 200

@app.route("/api/submit", methods=["POST"])
def submit():
    r = request.json
    queryS("UPDATE tasks SET time_finished = %s, tweets_scraped = %s, done=%s WHERE id = %s",
    [math.floor(time.time()), r["tweets_scraped"], True, r["id"]], cnx)
    queryS("UPDATE stats SET stat_value = stat_value + %s WHERE stat_name = 'tweets_scraped'",
    [r["tweets_scraped"]], cnx)
    return "", 200

@app.route("/api/log", methods=["POST"])
def log():
    r = request.json
    queryS("INSERT INTO log (instance, msg) VALUES (%s, %s)",
    [r["instance"], r["msg"]], cnx)
    return "", 200

app.run(host=os.getenv("APIHOST"), port=os.getenv("APIPORT"))