from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        """test set up of the admin page"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='sangeethsubramoniam@gmail.com',
            password='sangeeth'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='sangeethsubramoniamtest@gmail.com',
            password='sangeeth'
        )

    def test_user_listed(self):
        """test if the users are listed in the modified admin page"""
        # reverse to the listing page ... the name is appname and the url \
        #           name is provided by documentation
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        # assert contains checks for the response contains the mentioned \
        #           items and also if the response was 200 OK
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        "test that the create user works "
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
