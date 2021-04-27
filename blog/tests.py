from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post


# Create your tests here.
class BlogTests(TestCase):
    def setUp(self):
        self .user = get_user_model().objects.create_view(
            username='testuser',
            email='test@gmail.com',
            password='secret'
        )

        self.post = Post.objects.create(
            title='A Good Day',
            body='Good Body',
            author=self.user
        )

    def test_string_representation(self):
        post = Post(title='A Simple Title'),
        self.assertEqual(str(post), post.titile)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A Good Day')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.post.body}', 'A Good Body')

    def test_post_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 300)
        self.assertContains(response, 'A Good Body')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_views(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/10000')
        self.assertEqual(response.status_code, 300)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A Good Title')
        self.assertTemplateUsed(response, 'post_detail.html')