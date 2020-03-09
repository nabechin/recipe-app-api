from django.test import TestCase
from django.urls import reverse
from core.models import Tag
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework import status
from recipe.serializers import TagSerializer

TAG_URL = reverse('recipe:tag-list')


class PublicTagAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        res = self.client.get(TAG_URL)
        self.assertEqual(res.status_code,status.HTTP_401_UNAUTHORIZED)


class PrivateTagAPITest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email = "test4@gmail.com",
            password = "test4test4"
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_tags(self):
        Tag.objects.create(user=self.user,name="Vegan")
        Tag.objects.create(user=self.user,name="Fluit")

        tags = Tag.objects.all().order_by('-name')

        res = self.client.get(TAG_URL)
        serializer = TagSerializer(tags, many=True)
        self.assertEqual(res.status_code,status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_tags_limited_user(self):
        self.user2 = get_user_model().objects.create_user(name="user2", email="test5@gmail.com", password="test5test5")
        tag = Tag.objects.create(user=self.user, name="Fluity")
        Tag.objects.create(user=self.user2, name="Flesh")
        res = self.client.get(TAG_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], tag.name)

    def test_tag_create_successful(self):
        payload = {'name': 'tagname'}
        self.client.post(TAG_URL, payload)
        exists = Tag.objects.filter(user=self.user, name=payload['name']).exists()
        self.assertTrue(exists)


    def test_create_tag_invalid(self):
        payload = {'name': ''}
        res = self.client.post(TAG_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        
