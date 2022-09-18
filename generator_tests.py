import unittest
import interface


class MyTestCase(unittest.TestCase):
    """
    Tests under construction.
    """
    def test_basic_case(self):
        # show = interface.start_user_interface()

        self.assertNotEqual(False, True)


if __name__ == '__main__':
    unittest.main()
