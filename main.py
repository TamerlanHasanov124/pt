import unittest
def add(a, b):
    return a + b

def P(name):
    return name
class TestAddition(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(P("Tom"), "Tom")

unittest.main()