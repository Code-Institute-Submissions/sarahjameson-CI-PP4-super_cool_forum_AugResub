from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment


class TestModels(TestCase):

    def test_post_model_str(self):
        """
        Testing that calling the string method returns correct string
        """
        post = Post.objects.create(title='Test Post')
        self.assertEqual(str(post), 'Test Post')

    def test_comment_model_str(self):
        """
        Testing that calling the string method returns correct string
        """
        post = Post.objects.create(title='Test Post')
        comment = Comment.objects.create(
            body='Test',
            post=post,
            name='Test_user'
            )
        self.assertEqual(str(comment), 'Comment Test by Test_user')

    def test_post_slug(self):
        """
        Testing the slug of a created post
        """
        test_user = User.objects.create_user(
            username='testuser', password='password'
            )
        post = Post.objects.create(
            title='test post item',
            content='Hello',
            status=1,
            slug='test-post-item')
        self.assertEqual(
                post.slug, 'test-post-item'
                )
