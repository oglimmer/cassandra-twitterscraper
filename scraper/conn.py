from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import json

with open("conf.json") as c: conf = json.load(c)
def getSession():
    auth = PlainTextAuthProvider(username=conf.get("user"), password=conf.get("password"))
    servers = conf.get('servers')
    cluster = Cluster(contact_points=servers, auth_provider=auth)
    session = cluster.connect(conf.get('keyspace'))
    return session

def getPreparedStatement(session):
    return session.prepare(f'''
    INSERT INTO {conf.get("table")}
    (id , company, unix_day, unix_time, content, likes, replies, retweets)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''')