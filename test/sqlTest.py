import unittest
import connection.mysqlConnector


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_sql(self):
        data = connection.mysqlConnector.execute("SELECT * FROM User")
        print(data)


if __name__ == '__main__':
    unittest.main()
