import datetime
import sqlite3


CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    release_timestamp REAL
);"""

CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS users (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT 
);"""

CREATE_WATCHED_TABLE = """CREATE TABLE IF NOT EXISTS watched (
    user_username TEXT,
    movie_id INTEGER,
    FOREIGN KEY(user_username) REFERENCES users(username),
    FOREIGN KEY(movie_id) REFERENCES movies(id)
);"""

INSERT_MOVIE = "INSERT INTO movies (title, release_timestamp) VALUES (?, ?)"
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp >= ?;"
INSERT_USER = "INSERT INTO users (username) VALUES (?);"
INSERT_WATCHED_MOVIE = "INSERT INTO watched (user_username, movie_id) VALUES (?, ?);"
SELECT_WATCHED_MOVIES = """SELECT movies.*
FROM users
JOIN watched ON users.username = watched.user_username
JOIN movies ON watched.movie_id = movies.id
WHERE LOWER(users.username) = ?;"""
SEARCH_MOVIE = """SELECT * FROM movies WHERE LOWER(title) LIKE ?;"""
SELECT_USER_THAT_WATCHED_MOVIES = """
SELECT user_username
FROM watched 
JOIN movies ON watched.movie_id = movies.id
WHERE LOWER(movies.title) = ?;
"""
DELETE_MOVIE1 = """DELETE FROM movies WHERE LOWER(title) = ?;"""
DELETE_MOVIE2 = """DELETE FROM watched WHERE LOWER(movie_id) = ?;"""


def create_tables():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_USERS_TABLE)
        connection.execute(CREATE_WATCHED_TABLE)


def add_movie(title, release_timestamp):
    with connection:
        connection.execute(INSERT_MOVIE, (title, release_timestamp))


def delete_movie1(title):
    with connection:
        connection.execute(DELETE_MOVIE1, (title,))


def delete_movie2(movie_id):
    with connection:
        connection.execute(DELETE_MOVIE2, (movie_id,))


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


