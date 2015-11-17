import unittest


__all__ = ['TestBaseClass']


class TestBaseClass(unittest.TestCase):
    def test_name(self):
        self.assertEqual(4, 2 + 2)
