import unittest
import hw13

class MyTestCase(unittest.TestCase):
    def test_find_err(self):
        self.assertEqual(hw13.find_err("syslog.txt","ERROR"), False)


if __name__ == '__main__':
    unittest.main()
