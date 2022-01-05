import unittest
import connecter


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_sql(self):
        data = connecter.execute("SELECT * FROM User")
        print(data)


if __name__ == '__main__':
    unittest.main()
