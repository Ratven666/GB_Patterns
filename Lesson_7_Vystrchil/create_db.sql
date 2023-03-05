
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

DROP TABLE IF EXISTS students;
CREATE TABLE students (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
                      name VARCHAR (32));

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
