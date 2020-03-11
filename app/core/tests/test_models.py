from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models

def sample_user(email='test3@gmail.com', password='test3test3'):
    return get_user_model().objects.create_user(email,password)


class ModelTests(TestCase):

    def test_create_user_create_with_email_successful(self):
        email = 'uhkhkh@gmail.com'
        password = 'nabechin'
        user = get_user_model().objects.create_user(
                email=email,
                password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        email = "aoie@GMAIL.COM"
        user = get_user_model().objects.create_user(
        email=email, password="iheri")
        self.assertEqual(user.email, email.lower())

    def test_new_user_email_value_check(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
            None, 'test@gmail.com'
            )

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
        email='ager@gmail.com', password="aseihfoa"
        )
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_tag_str(self):
        tag = models.Tag.objects.create(
            user = sample_user(),
            name = 'Vegan'
        )
        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Letas'
        )
        self.assertEqual(str(ingredient), ingredient.name)
