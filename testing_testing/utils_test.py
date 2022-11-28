import unittest
import utils


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("I run only once")

    @classmethod
    def tearDownClass(cls) -> None:
        print("I run after all")

    def test_for_error(self):
        # with self.assertRaisesRegex(TypeError, "anything") as e:
        #     utils.add("4", 2)

        self.assertRaisesRegex(TypeError, "", utils.add, "4", 2)

    def setUp(self) -> None:
        print("I run  before every test case")

    def tearDown(self) -> None:
        print("I run  after every test case")

    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_add(self):
        self.assertEqual(5, utils.add(2, 3))

    def test_list(self):
        self.assertListEqual([1, 4, 9], utils.square_list([1, 2, 3]))


if __name__ == '__main__':
    unittest.main()
