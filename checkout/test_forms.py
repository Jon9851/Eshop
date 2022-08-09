from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):
    form = OrderForm({'full_name': ''})
    self.assertFalse(form.is_valid())
    self.assertIn('full_name', form.errors.keys())
    self.assertEqual(form.errors['name'][0], 'This field is required')
    
