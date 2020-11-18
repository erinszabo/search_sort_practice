import unittest
import binary as b


class MyTestCase(unittest.TestCase):

    def test_binary_search(self):
        testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
        self.assertEqual(b.binary_search(testlist, 3), False)
        self.assertEqual(b.binary_search(testlist, 13), True)
        # self.assertEqual(b.binary_search(testlist, 13), False)




if __name__ == '__main__':
    unittest.main()
