from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user(self):
        email = 'sangeethsubramoiam@gmail.com'
        password = 'sangeeth'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_super_user(self):
        user = get_user_model().objects.create_super_user(
            'sangeethsubramoniam@gmail.com',
            'sangeeth'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
