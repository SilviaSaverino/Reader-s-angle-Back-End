from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase

class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='testname', password='testpw')

    def test_can_list_posts(self):
        testname = User.objects.get(username='testname')
        Post.objects.create(owner=testname, title='test title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_a_post(self):
        self.client.login(username='testname', password='testpw')
        response = self.client.post('/posts/', {'title': 'test title'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_post(self):
        response = self.client.post('/posts/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class PostDetailViewTests(APITestCase):
    def setUp(self):
        testname1 = User.objects.create_user(username='testname1', password='pw1')
        testname2 = User.objects.create_user(username='testname2', password='pw2')
        Post.objects.create(
            owner=testname1, title='title1', content='content1'
        )
        Post.objects.create(
            owner=testname2, title='title2', content='content2'
        )

    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'title1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_not_retrieve_post_with_invalid_id(self):
        response = self.client.get('/posts/1989/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
  
    def test_user_can_update_own_post(self):
        self.client.login(username='testname1', password='pw1')
        response = self.client.put('/posts/1/', {'title': 'a new title1', 'content': 'content1'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'a new title1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)    

    def test_user_cant_update_another_users_post(self):
        self.client.login(username='testname1', password='pw1')
        response = self.client.put('/posts/2/', {'title': 'a new title', 'content': 'a new content'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)