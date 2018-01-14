import unittest
from app import create_app

class BasicsTestCase(unittest.TestCase):
    def test(self):
        create_app()
        print('ok')

if __name__ == '__main__':
    unittest.main();
