from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment


class TestViews(TestCase):

    def test_get_index_page(self):
        """
        Test to ensure home page is displayed
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_post_detail_page(self):
        """
        Test to ensure post detail page is displayed
        """        
        post = Post.objects.create(title='Test Post Item', content='Hello', status=1, slug="test-post-slug")
        response = self.client.get(f'/{post.slug}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_get_profile_page(self):
        """
        Test to ensure user profile page is displayed
        """ 
        test_user = User.objects.create_user(
            username='testuser', password='password'
            )
        self.client.login(username='testuser', password='password')
        response = self.client.get('/user-profile')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_profile.html')

    def test_edit_post_page(self):
        """
        Test to ensure update post page can be displayed"
        """ 
        post = Post.objects.create(title='Test Post Item', content='Hello', status=1, slug="test-post-slug")
        response = self.client.get(f'/edit/{post.slug}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_post.html')

    def can_edit_post(self):
        """
        Test to ensure posts can be edited
        """
        response = self.client.post(f'/edit', {'title': 'Test Post Item 2'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '')

    def test_can_create_post(self):
        """
        Test to ensure posts can be created
        """ 
        post = Post.objects.create(title='Test Post Item', content='Hello', status=1)
        response = self.client.post('/create-post', {'title': 'Test Post Item', 'content': 'Hello', 'status': 1})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_post.html')

    def test_can_add_comment(self):
        """
        Test to ensure comments can be added
        """ 
        test_user = User.objects.create_user(
            username='testuser', password='password'
            )
        self.client.login(username='testuser', password='password')
        post = Post.objects.create(title='Test Post Item', content='Hello', status=1, slug="test-post-slug")
        comment = Comment.objects.create(body='Testing', post=post)
        response = self.client.post(f'/{post.slug}/', {'body': 'Testing'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_can_delete_post(self):
        """
        Test to ensure posts can be deleted
        """ 
        post = Post.objects.create(title='Test Post Item', content='Hello', status=1, slug="test-post-slug")
        response = self.client.post(f'/delete-post/{post.slug}')
        self.assertRedirects(response, '/')
        existing_posts = Post.objects.filter(slug=post.slug)
        self.assertEqual(len(existing_posts), 0)