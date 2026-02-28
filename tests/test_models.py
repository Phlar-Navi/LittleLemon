from django.test import TestCase
from restaurant.models import Menu

class MenuTestCase(TestCase):

    def test_menu_item_str(self):
        pizza = Menu.objects.create(title="Pizza", price=10.99, inventory=5)
        pasta = Menu.objects.create(title="Pasta", price=8.99, inventory=10)
        self.assertEqual(str(pizza), "Pizza : 10.99")
        self.assertEqual(str(pasta), "Pasta : 8.99")