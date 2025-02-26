# gunpla/tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Gunpla

class GunplaAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.test_gunpla = Gunpla.objects.create(
            name="RX-78-2 Gundam",
            series="Mobile Suit Gundam",
            grade="Master Grade",
            scale="1/100"
        )
        self.base_url = "/gunplas"

    def test_get_gunplas_empty(self):
        """Test getting gunplas when database is empty."""
        # First, clear the DB
        Gunpla.objects.all().delete()

        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), [])

    def test_get_gunplas(self):
        """Test getting list of gunplas."""
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)
        gunpla_data = response.json()[0]
        self.assertEqual(gunpla_data['name'], "RX-78-2 Gundam")
        self.assertEqual(gunpla_data['series'], "Mobile Suit Gundam")
        self.assertEqual(gunpla_data['grade'], "Master Grade")
        self.assertEqual(gunpla_data['scale'], "1/100")

    def test_create_gunpla(self):
        """Test creating a new gunpla."""
        data = {
            'name': 'Wing Gundam Zero',
            'series': 'Gundam Wing',
            'grade': 'Perfect Grade',
            'scale': '1/60'
        }
        response = self.client.post(self.base_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['name'], data['name'])
        self.assertEqual(response.json()['series'], data['series'])
        self.assertEqual(response.json()['grade'], data['grade'])
        self.assertEqual(response.json()['scale'], data['scale'])

    def test_create_gunpla_missing_required_fields(self):
        """Test creating a gunpla with missing required fields."""
        data = {
            'name': 'Wing Gundam Zero',
            # Missing series and grade
            'scale': '1/60'
        }
        response = self.client.post(self.base_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('message', response.json())
        self.assertIn('Series field is required', str(response.json()['message']))
        self.assertIn('Grade field is required', str(response.json()['message']))

    def test_get_gunpla(self):
        """Test getting a specific gunpla."""
        response = self.client.get(f'{self.base_url}/{self.test_gunpla.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        gunpla_data = response.json()
        self.assertEqual(gunpla_data['name'], self.test_gunpla.name)
        self.assertEqual(gunpla_data['series'], self.test_gunpla.series)
        self.assertEqual(gunpla_data['grade'], self.test_gunpla.grade)
        self.assertEqual(gunpla_data['scale'], self.test_gunpla.scale)

    def test_get_nonexistent_gunpla(self):
        """Test getting a gunpla that doesn't exist."""
        response = self.client.get(f'{self.base_url}/999')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.json()['detail'], 'Not found.')

    def test_update_gunpla(self):
        """Test updating a gunpla."""
        data = {
            'name': 'Updated Gundam',
            'series': 'Updated Series',
            'grade': 'Updated Grade',
            'scale': '1/144'
        }
        response = self.client.put(f'{self.base_url}/{self.test_gunpla.id}', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        gunpla_data = response.json()
        self.assertEqual(gunpla_data['name'], data['name'])
        self.assertEqual(gunpla_data['series'], data['series'])
        self.assertEqual(gunpla_data['grade'], data['grade'])
        self.assertEqual(gunpla_data['scale'], data['scale'])

    def test_update_nonexistent_gunpla(self):
        """Test updating a gunpla that doesn't exist."""
        data = {
            'name': 'Updated Gundam',
            'series': 'Updated Series',
            'grade': 'Updated Grade',
            'scale': '1/144'
        }
        response = self.client.put(f'{self.base_url}/999', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.json()['detail'], 'Not found.')

    def test_delete_gunpla(self):
        """Test deleting a gunpla."""
        response = self.client.delete(f'{self.base_url}/{self.test_gunpla.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['message'], 'Gunpla model deleted successfully')

        # Verify gunpla was deleted
        response = self.client.get(f'{self.base_url}/{self.test_gunpla.id}')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_nonexistent_gunpla(self):
        """Test deleting a gunpla that doesn't exist."""
        response = self.client.delete(f'{self.base_url}/999')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.json()['detail'], 'Not found.')
