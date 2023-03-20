CREATE TABLE tasks(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    company INT NOT NULL,
    unix_start INT NOT NULL,
    unix_end INT NOT NULL,
    time_started INT NOT NULL DEFAULT 0,
    time_finished INT NOT NULL DEFAULT 0,
    tweets_scraped INT NOT NULL DEFAULT 0,
    done TINYINT(1) NOT NULL DEFAULT false
);
ALTER TABLE tasks ADD UNIQUE (company, unix_start, unix_end);
CREATE TABLE search_terms(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    company INT NOT NULL,
    term VARCHAR(100) NOT NULL
);
ALTER TABLE search_terms ADD UNIQUE (company, term);
CREATE TABLE log(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    instance VARCHAR(50) NOT NULL,
    msg VARCHAR(200) NOT NULL,
    time_logged INT NOT NULL DEFAULT UNIX_TIMESTAMP()
);
CREATE TABLE stats(
    stat_name VARCHAR(20) NOT NULL PRIMARY KEY,
    stat_value BIGINT NOT NULL
);
INSERT INTO stats (stat_name, stat_value) VALUES ('tweets_scraped', 0);