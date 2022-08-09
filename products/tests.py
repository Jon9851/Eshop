from django.test import TestCase

# Create your tests here.


class TestViews(TestCase):

    """
    this test is to check that the view_bag view is rendering
    the correct template when used
    """

    def test_get_view_products(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
