
import unittest
from ..data_structures.stack import Stack


class TestStack(unittest.TestCase):

    def test_push(self):

        stack = Stack()

        stack.push(1)
        stack.push(2)

        self.assertEqual(stack.peek() == 2)


if __name__ == '__main__':

    unittest.main()
