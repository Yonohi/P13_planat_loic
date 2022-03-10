from django.test import TestCase
from django.urls import reverse
# A voir: https://docs.djangoproject.com/fr/4.0/topics/testing/tools/
# En particulier la partie 'test des réponses'
# Pytest peut apparemment sans problème passer des tests prévu pour unittest


def test_dummy():
    assert 1


class TestIndex(TestCase):
    def test_url(self):
        response = self.client.get(reverse('index'))
        assert response.status_code == 200
        assert b'Welcome to Holiday Homes' in response.content
