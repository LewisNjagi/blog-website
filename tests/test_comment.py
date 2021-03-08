import unittest
from app.models import Comment

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.new_comment = Comment(comment = "Good Advice")

    def test_init(self):
        self.assertEqual(self.new_comment.comment,"Good Advice")