CREATE DATABASE IF NOT EXISTS nest_database;
USE nest_database;
CREATE TABLE IF NOT EXISTS credentials (
    id int NOT NULL AUTO_INCREMENT,
    token varchar(10),
    data varchar(255),
    PRIMARY KEY (id)
);
truncate table credentials;
