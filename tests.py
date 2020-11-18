import unittest
import binary as b
import sorts as s


class MyTestCase(unittest.TestCase):

    def test_binary_search(self):
        testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
        self.assertEqual(b.binary_search(testlist, 3), False)
        self.assertEqual(b.binary_search(testlist, 13), True)
        # self.assertEqual(b.binary_search(testlist, 13), False)

    def test_bubble_sort(self):
        a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        self.assertEqual(s.bubble_sort(a), [17, 20, 26, 31, 44, 54, 55, 77, 93])


if __name__ == '__main__':
    unittest.main()
