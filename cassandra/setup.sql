CREATE  KEYSPACE IF NOT EXISTS scraper WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1} 

CREATE TABLE scraper.tweets (
    id bigint,
    company int,
    unix_day int,
    unix_time int,
    content text,
    likes int,
    replies int,
    retweets int,
    PRIMARY KEY ((unix_day, company), id)
) WITH compression = {'enabled': 'false'};