import unittest
from app.models import Blog

class BlogModelTest(unittest.TestCase):
    def setUp(self):
        self.new_blog = Blog(blog = "Hello")

    def test_init(self):
        self.assertEqual(self.new_blog.blog,"Hello")