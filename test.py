import unittest
import sqlite3
import warnings
import database
import pytest

warnings.simplefilter("ignore", ResourceWarning)


class TestProject(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect("data_u06_test.db")
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
        cursor = self.conn.cursor()
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

    def tearDown(self):
        self.conn.close()


if __name__ == "__main__":
    unittest.main(warnings='ignore')


@pytest.fixture
def setup_database():
    """ Fixture to set up the in-memory database with test data """
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
    # Test to make sure that there are 2 items in the database

    cursor = setup_database
    assert len(list(cursor.execute('SELECT * FROM stocks'))) == 2