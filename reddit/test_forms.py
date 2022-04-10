from django.test import TestCase
from .forms import CommentForm, PostForm

class TestCommentForm(TestCase):
    '''
    Testing to Comment Form
    '''

    def comment_text_is_required(self):
        '''
        Test to ensure body is not empty
        '''
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        '''
        Test to ensure that the fields listed in the meta class are present
        '''
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('body',))

class TestPostForm(TestCase):

    def title_text_is_required(self):
        '''
        Test to ensure title is not empty
        '''
        form = PostForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def content_text_is_required(self):
        '''
        Test to ensure content is not empty
        '''
        form = PostForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        '''
        Test to ensure that the fields listed in the meta class are present
        '''
        form = PostForm()
        self.assertEqual(form.Meta.fields, ('title','content', 'status'))