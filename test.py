import unittest
import sqlite3
import warnings
import database
import pytest
import requests

warnings.simplefilter("ignore", ResourceWarning)


class TestProject(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        c = self.conn.cursor()

        cmd = database.CREATE_MOVIES_TABLE
        c.execute(cmd)

        cmd = database.CREATE_USERS_TABLE
        c.execute(cmd)

        cmd = database.CREATE_WATCHED_TABLE
        c.execute(cmd)

        self.conn.commit()

    def test_add_movies_to_db(self):
        title = 'test1'
        release_timestamp = '2022-10-12'
        cursor = self.conn.cursor()
        cursor.execute(database.INSERT_MOVIE, (title, release_timestamp))
        try:
            self.conn.commit()
        except Exception as ex:
            self.fail(f'Add DATA TO MOVIE TABLE FAILED. TEST FAILED exception is: {ex}')

    def test_add_watched_to_db(self):
        user_username = 'test1'
        movie_id = '1'
        cursor = self.conn.cursor()
        cursor.execute(database.INSERT_WATCHED_MOVIE, (user_username, movie_id))
        try:
            self.conn.commit()
        except Exception as ex:
            self.fail(f'Add DATA TO WATCHED TABLE FAILED. TEST FAILED exception is: {ex}')

    def test_add_users_to_db(self):
        username = 'test1'
        cursor = self.conn.cursor()
        cursor.execute(database.INSERT_USER, (username,))
        try:
            self.conn.commit()
        except Exception as ex:
            self.fail(f'Add DATA TO USERS TABLE FAILED. TEST FAILED exception is: {ex}')

    def test_delete_users_from_db(self):
        username = 'test1'
        cursor = self.conn.cursor()
        cursor.execute(database.DELETE_USER, (username,))
        try:
            self.conn.commit()
        except Exception as ex:
            self.fail(f'DELETE DATA FROM USERS TABLE FAILED. TEST FAILED exception is: {ex}')

    def test_get_all_movies(self):
        title = 'test1'
        release_timestamp = '2022-10-12'
        cursor = self.conn.cursor()
        cursor.execute(database.INSERT_MOVIE, (title, release_timestamp))
        cursor.execute(database.SELECT_ALL_MOVIES)
        result = cursor.fetchall()
        try:
            self.assertTrue(result)
        except Exception as ex:
            self.fail(f'GET DATA FROM MOVIE TABLE FAILED. TEST FAILED exception is: {ex}')

    def test_select_watched_movies(self):
        username = 'test1'
        cursor = self.conn.cursor()
        cursor.execute(database.SELECT_WATCHED_MOVIES, (username,))
        try:
            self.conn.commit()
        except Exception as ex:
            self.fail(f'GET DATA FROM WATCHED TABLE FAILED. TEST FAILED exception is: {ex}')

    def test_get_user_watched_movies(self):
        title = 'test1'
        cursor = self.conn.cursor()
        cursor.execute(database.SELECT_WATCHED_MOVIES, (title,))
        try:
            self.conn.commit()
        except Exception as ex:
            self.fail(f'GET DATA FROM WATCHED TABLE FAILED. TEST FAILED exception is: {ex}')

    def test_get_search_movies(self):
        title = 'test1'
        cursor = self.conn.cursor()
        cursor.execute(database.SEARCH_MOVIE, (title,))
        try:
            self.conn.commit()
        except Exception as ex:
            self.fail(f'GET DATA FROM MOVIE TABLE FAILED. TEST FAILED exception is: {ex}')

    def test_exit_movie_id(self):
        movie_id = 'movie_id'
        cursor = self.conn.cursor()
        cursor.execute(database.EXIST_MOVIE_ID, (movie_id,))
        try:
            self.conn.commit()
        except Exception as ex:
            self.fail(f'GET DATA FROM WATCHED TABLE FAILED. TEST FAILED exception is: {ex}')

    def tearDown(self):
        self.conn.close()


if __name__ == "__main__":
    unittest.main(warnings='ignore')


@pytest.fixture
def setup_database():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('''
	    CREATE TABLE stocks
        (date text, trans text, symbol text, qty real, price real)''')
    sample_data = [
        ('2020-01-01', 'BUY', 'IBM', 1000, 45.0),
        ('2020-01-01', 'SELL', 'GOOG', 40, 123.0),
    ]
    cursor.executemany('INSERT INTO stocks VALUES(?, ?, ?, ?, ?)', sample_data)
    yield conn


def test_connection(setup_database):

    cursor = setup_database
    assert len(list(cursor.execute('SELECT * FROM stocks'))) == 2

@pytest.fixture
def test_movies_table():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    release_timestamp REAL,
    status INTEGER default 1
);''')
    conn.commit()
    cursor.execute("SELECT * FROM movies;")
    data = cursor.fetchall()
    assert len(data) == 0
    conn.close()


def test_users_table():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT ,
    status INTEGER default 1
);''')
    conn.commit()
    cursor.execute("SELECT * FROM users;")
    data = cursor.fetchall()
    assert len(data) == 0
    conn.close()


def test_watched_table():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('''
       CREATE TABLE IF NOT EXISTS watched (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    user_username TEXT,
    movie_id INTEGER,
    status INTEGER default 1,
    FOREIGN KEY(user_username) REFERENCES users(username),
    FOREIGN KEY(movie_id) REFERENCES movies(id)

);''')
    conn.commit()
    cursor.execute("SELECT * FROM watched;")
    data = cursor.fetchall()
    assert len(data) == 0
    conn.close()


def test_insert_data_movies():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS movies (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        release_timestamp REAL,
        status INTEGER default 1
    );''')

    sample_data = [
        ('5', 'Inception', '2010-07-13')
    ]
    cursor.executemany('INSERT INTO movies VALUES(NULL, ?, ?, ?)', sample_data)
    cursor.execute("SELECT * FROM movies;")
    data = cursor.fetchall()
    assert len(data) == 1


def test_insert_data_users():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT ,
        status INTEGER default 1
    );''')

    sample_data = [
        ('Arash', 5)
    ]
    cursor.executemany('INSERT INTO users VALUES(NULL, ?, ?)', sample_data)
    cursor.execute("SELECT * FROM users;")
    data = cursor.fetchall()
    assert len(data) == 1


def test_insert_data_watched():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('''
           CREATE TABLE IF NOT EXISTS watched (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        user_username TEXT,
        movie_id INTEGER,
        status INTEGER default 1,
        FOREIGN KEY(user_username) REFERENCES users(username),
        FOREIGN KEY(movie_id) REFERENCES movies(id)

    );''')

    sample_data = [
        ('1', 'Arash', '2')
    ]
    cursor.executemany('INSERT INTO watched VALUES(NULL, ?, ?, ?)', sample_data)
    cursor.execute("SELECT * FROM watched;")
    data = cursor.fetchall()
    assert len(data) == 1


def test_api_connection():
    url = "https://imdb-api.com/en/API/ComingSoon/k_i4k5g19z"
    api = requests.get(url)
    assert api.status_code == 200


def test_delete_movie_title():
    title = 'Inception'
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    sample_data = [
        ('Inception', '2010-07-13', 5)
    ]
    cursor.execute('''
              CREATE TABLE IF NOT EXISTS movies (
          ID INTEGER PRIMARY KEY AUTOINCREMENT,
          title TEXT,
          release_timestamp REAL,
          status INTEGER default 1
      );''')
    cursor.executemany('INSERT INTO movies VALUES(NULL, ?, ?, ?)', sample_data)
    cursor.execute(database.DELETE_MOVIE1, (title,))
    cursor.execute("SELECT * FROM movies where title = 'Inception' and status = 1;")
    data = cursor.fetchall()
    assert len(data) == 0


def test_add_movies():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    sample_data = [
        ('Inception', '2010-07-13', 1)
        ]
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    release_timestamp REAL,
    status INTEGER default 1
);''')

    cursor.executemany('INSERT INTO movies VALUES(NULL, ?, ?, ?)', sample_data)
    conn.commit()
    cursor.execute("SELECT * FROM movies;")
    data = cursor.fetchall()
    assert len(data) == 1
    conn.close()


def test_add_user():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    sample_data = [
        ('Arash', 1)
        ]
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT ,
        status INTEGER default 1
    );''')
    conn.commit()
    cursor.executemany('INSERT INTO users VALUES(NULL, ?, ?)', sample_data)
    cursor.execute("SELECT * FROM users;")
    data = cursor.fetchall()
    assert len(data) == 1
    conn.close()


def test_delete_user():
    username = 'arash'
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    sample_data = [
        ('Arash', 1)
        ]
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT ,
        status INTEGER default 1
    );''')

    cursor.executemany('INSERT INTO users VALUES(NULL, ?, ?)', sample_data)
    cursor.execute(database.DELETE_USER, (username,))
    conn.commit()
    cursor.execute("SELECT * FROM users where username = 'arash' and status = 1;")
    data = cursor.fetchall()
    assert len(data) == 0
    conn.close()


def test_watch_movie():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    sample_data = [
        ('Arash', '2', 1)
        ]
    cursor.execute('''
               CREATE TABLE IF NOT EXISTS watched (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            user_username TEXT,
            movie_id INTEGER,
            status INTEGER default 1,
            FOREIGN KEY(user_username) REFERENCES users(username),
            FOREIGN KEY(movie_id) REFERENCES movies(id)

        );''')
    conn.commit()
    cursor.executemany('INSERT INTO watched VALUES(NULL, ?, ?, ?)', sample_data)
#    cursor.execute("SELECT * FROM watched where user_username = 'Arash';")
    cursor.execute("SELECT * FROM watched where id = 1;")
    data = cursor.fetchall()
    assert len(data) == 1
    conn.close()


def test_search_movie():
    title = 'inception'
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    sample_data = [
        ('inception', '2010-07-13', 1)
        ]
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    release_timestamp REAL,
    status INTEGER default 1
);''')
    cursor.executemany('INSERT INTO movies VALUES(NULL, ?, ?, ?)', sample_data)
    conn.commit()
    cursor.execute("SELECT * FROM movies WHERE title = ?;", (title,))
    data = cursor.fetchall()
    assert len(data) > 0
    conn.close()
