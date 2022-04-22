import pytest
import sqlite3
import unittest
from unittest import mock
import database
from unittest.mock import Mock, patch


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





class Test_insert_rows(unittest.TestCase):

    def fix_dbc(self):
        dbc = mock.MagicMock(spec=['cursor'])
        dbc.autocommit = True
        return dbc

    def fix_rows(self):
        rows = [{'title': 'Inception', 'release_timestamp': '2010-07-13'},
                {'title': 'chert', 'release_timestamp': '2010-07-13'}, ]
        return rows

    def fix_tuples(self):
        tuples = [('Inception', '2010-07-13'),
                  ('chert', '2010-13-07'), ]
        return tuples

    def test_insert_movies(self):
        dbc = self.fix_dbc()
        tuples = self.fix_tuples()
        expect_sql = 'INSERT INTO movies(title, release_timestamp) VALUES (?,?)'
        calls = [mock.call.executemany(expect_sql, tuples), mock.call.commit(), ]
        # cursor.assert_has_calls(calls)
        self.assertTrue(dbc.autocommit)

    def test_insert_rows_calls_cursor_method(self):
        dbc = self.fix_dbc()
        query = "SELECT * FROM movies WHERE release_timestamp >= ?;"
        calls = [mock.call.execute(query, '2010-07-13'), mock.call.commit(), ]
        self.assertEqual(dbc.cursor.called, False)

    def test_get_data(self):
        dbc = self.fix_dbc()
        query = "SELECT ID FROM movies WHERE title = 'Inception';"
        calls = mock.call.execute(query), mock.call.commit()
        self.assertEqual(dbc.cursor.called, False)


if __name__ == '__main__':
    unittest.main(argv=['', '-v'])


