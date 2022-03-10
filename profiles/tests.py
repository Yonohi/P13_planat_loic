from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile


class TestProfiles(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user('Username', 'a@email.com', 'Mypassword')
        cls.profile = Profile.objects.create(user=cls.user,
                                             favorite_city='City'
                                             )

    def test_profiles_index(self):
        response = self.client.get(reverse('profiles_index'))
        assert response.status_code == 200
        assert b'<title>Profiles</title>' in response.content

    def test_profiles_detail(self):
        response = self.client.get(reverse('profile', kwargs={'username': 'Username'}))
        assert response.status_code == 200
        assert b'<title>Username</title>' in response.content
        assert b'<h1>Username</h1>' in response.content
        assert b'a@email.com' in response.content
        assert b'City' in response.content
