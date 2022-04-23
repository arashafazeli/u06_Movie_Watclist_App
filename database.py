import datetime
import sqlite3

# Query for make tables in database  (if not exists already)
CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    release_timestamp REAL,
    status INTEGER default 1
);"""

CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS users (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT ,
    status INTEGER default 1
);"""

CREATE_WATCHED_TABLE = """CREATE TABLE IF NOT EXISTS watched (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    user_username TEXT,
    movie_id INTEGER,
    status INTEGER default 1,
    FOREIGN KEY(user_username) REFERENCES users(username),
    FOREIGN KEY(movie_id) REFERENCES movies(id)

);"""

# MAKE ALL THE QUERY THAT USED IN THE FUNCTIONS
INSERT_MOVIE = "INSERT INTO movies (title, release_timestamp) VALUES (?, ?)"

SELECT_ALL_MOVIES = "SELECT * FROM movies where status = 1;"

SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp >= ? and status = 1;"

INSERT_USER = "INSERT INTO users (username) VALUES (?);"

INSERT_WATCHED_MOVIE = "INSERT INTO watched (user_username, movie_id) VALUES (?, ?);"

SELECT_WATCHED_MOVIES = """SELECT m.*
FROM users
JOIN watched w ON users.username = w.user_username 
JOIN movies m ON w.movie_id = m.id
WHERE LOWER(users.username) = ? and  w.status = 1 and m.status = 1"""

SEARCH_MOVIE = """SELECT * FROM movies WHERE LOWER(title) LIKE ? and status = 1;"""

SELECT_USER_THAT_WATCHED_MOVIES = """
SELECT user_username
FROM watched 
JOIN movies ON watched.movie_id = movies.id
WHERE LOWER(movies.title) = ? and movies.status = 1;"""

DELETE_MOVIE1 = """UPDATE movies set status = 0 WHERE LOWER(title) = ?;"""

EXIST_MOVIE_ID = "SELECT * FROM movies where ID = ?;"

DELETE_USER = """UPDATE users set status = 0 WHERE LOWER(username) = ?;"""


# ==========================================Define Function==================================================
# Define creat_tables() function to make the tables.


def create_tables():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_USERS_TABLE)
        connection.execute(CREATE_WATCHED_TABLE)
# Define add_movie() function to use this in the tab1.(insert the movie in the database)


def add_movie(title, release_timestamp):
    with connection:
        connection.execute(INSERT_MOVIE, (title, release_timestamp))
# Define delete_movie_title() funktion to use this in the tab1.(Delete movie from database)


def delete_movie_title(title):
    with connection:
        connection.execute(DELETE_MOVIE1, (title,))


def get_movies(upcoming=False):
    with connection:
        cursor = connection.cursor()
        if upcoming:
            today_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp,))
        else:
            cursor.execute(SELECT_ALL_MOVIES)
        return cursor.fetchall()


def add_user(username):
    with connection:
        connection.execute(INSERT_USER, (username,))


def delete_username(username):
    with connection:
        connection.execute(DELETE_USER, (username,))


def watch_movie(username, movie_id):
    with connection:
        connection.execute(INSERT_WATCHED_MOVIE, (username, movie_id))


def get_watched_movies(username):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_WATCHED_MOVIES, (username,))
        return cursor.fetchall()


def search_movies(search_term):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SEARCH_MOVIE, (f"%{search_term}%",))
        return cursor.fetchall()


def get_user_watched_movies(movie_name):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_USER_THAT_WATCHED_MOVIES, (movie_name,))
        return cursor.fetchall()


def exist_movie_id(movie_id):
    with connection:
        cursor = connection.cursor()
        cursor.execute(EXIST_MOVIE_ID, (movie_id,))
        result = cursor.fetchall()
        if result:
            return True
        else:
            return False

# make database and tables


connection = sqlite3.connect("data_u06.db")
create_tables()
# insert data to database
# create a cursor object from the cursor class
cur = connection.cursor()
# creating a list of items
sql_file1 = open("u06_seed_movies.sql")
sql_as_string1 = sql_file1.read()
cur.executescript(sql_as_string1)
sql_file2 = open("u06_seed_users.sql")
sql_as_string2 = sql_file2.read()
cur.executescript(sql_as_string2)
sql_file3 = open("u06_seed_watched.sql")
sql_as_string3 = sql_file3.read()
cur.executescript(sql_as_string3)


