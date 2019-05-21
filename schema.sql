DROP TABLE IF EXISTS authors;
DROP TABLE IF EXISTS blogpost;
DROP TABLE IF EXISTS published;

CREATE TABLE authors(
                    user_id INTEGER PRIMARY KEY ASC,
                    first_name TEXT,
                    last_name TEXT,
                    username TEXT,
                    password TEXT
                    );

CREATE TABLE blogpost (
                       blog_id INTEGER PRIMARY KEY ASC,
                       title TEXT,
                       content INTEGER,
                       date TEXT,
                       category TEXT
                       );

CREATE TABLE published(
                       user_id INTEGER,
                       blog_id INTEGER,
                       published INTEGER
                       );

INSERT INTO authors (user_id, first_name, last_name, username, password) VALUES (01, "Dennis", "Awad", "Dawad", "sassmasterd");
INSERT INTO blogpost (blog_id, title, content, date, category) VALUES (01, "test blog", "This is to test posting the first blog in the data base", datetime.datetime.now(), "testing");
INSERT INTO published (user_id, blog_id, published) VALUES (01,01,01);
