from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Item

class ItemAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create an item for testing
        self.item = Item.objects.create(name='Football', description='A standard football', quantity=10)

    def test_create_item(self):
        item_data = {'name': 'Basketball', 'description': 'A standard basketball', 'quantity': 5}
        response = self.client.post('/api/inventory/v1/items/', item_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 2)  # 1 created in setUp + 1 new
        self.assertEqual(Item.objects.last().name, 'Basketball')

    def test_get_items(self):
        response = self.client.get('/api/inventory/v1/items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Should be 1 as setUp creates 1 item

    def test_update_item_quantity(self):
        response = self.client.patch(f'/api/inventory/v1/items/{self.item.id}/', {'quantity': 5}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.item.refresh_from_db()  # Refresh item from database
        self.assertEqual(self.item.quantity, 5)
