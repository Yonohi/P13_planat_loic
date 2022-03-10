from django.test import TestCase
from django.urls import reverse
from .models import Letting, Address


class TestLettings(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.address = Address.objects.create(number=1,
                                             street='street',
                                             city='City',
                                             state='State',
                                             zip_code=00000,
                                             country_iso_code=000
                                             )
        cls.letting = Letting.objects.create(title='Test', address=cls.address)

    def test_lettings_index(self):
        response = self.client.get(reverse('lettings_index'))
        assert response.status_code == 200
        assert b'<title>Lettings</title>' in response.content

    def test_lettings_detail(self):
        response = self.client.get(reverse('letting', kwargs={'letting_id': 1}))
        assert response.status_code == 200
        assert b'<title>Test</title>' in response.content
        assert b'street' in response.content
        assert b'City' in response.content
        assert b'State' in response.content
