from django.test import TestCase
from restaurant.models import Menu

class MenuViewTestCase(TestCase):

    def setUp(self):
        Menu.objects.create(title="Pizza", price=10.99, inventory=5)
        Menu.objects.create(title="Pasta", price=8.99, inventory=10)

    def test_menu_view(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pizza")
        self.assertContains(response, "Pasta")