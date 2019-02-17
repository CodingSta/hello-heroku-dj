from django.shortcuts import resolve_url
from django.test import TestCase


class BlogTestCase(TestCase):
    def test_index(self):
        response = self.client.get(resolve_url('blog:index'))
        self.assertEqual(response.status_code, 200)


class CalculateTestCase(TestCase):
    def setUp(self):
        pass

    def test_1(self):
        self.assertEqual(1+1, 2)

