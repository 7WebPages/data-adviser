from django.test import TestCase


__all__ = ['SampleTestCase']


class SampleTestCase(TestCase):
    def test_sample(self):
        self.assertEqual(4, 2 + 2)
