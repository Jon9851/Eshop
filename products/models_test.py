from django.test import TestCase
from .models import Category, Product

class TestModels(TestCase):

    def Test_done_defaults_to_false(self):
        item = Order.objects.create(Name=' Test Product')
        self.assertFalse(item.done)