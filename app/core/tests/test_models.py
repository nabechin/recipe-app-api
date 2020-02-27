from django.test import TestCase
from django.contrib.auth import get_user_model


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
