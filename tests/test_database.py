import os
import sys
import unittest
from unittest.mock import MagicMock, patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.models.database import Database

class TestDatabaseExecute(unittest.TestCase):
    def setUp(self):
        os.environ.setdefault('DB_HOST', 'localhost')
        os.environ.setdefault('DB_USER', 'user')
        os.environ.setdefault('DB_PASSWORD', 'password')
        os.environ.setdefault('DB_NAME', 'test_db')

    @patch('app.models.database.mysql.connector.connect')
    def test_execute_select(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [{'1': 1}]
        mock_conn.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_conn

        db = Database()
        result = db.execute('SELECT 1', fetch=True)

        self.assertEqual(result, [{'1': 1}])
        mock_cursor.execute.assert_called_with('SELECT 1', ())
        mock_conn.cursor.assert_called_with(dictionary=True)
        mock_cursor.close.assert_called_once()
        mock_conn.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()
