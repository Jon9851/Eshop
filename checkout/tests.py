from django.test import TestCase

# Create your tests here.


class TestViews(TestCase):

    """
    this test is to check that the checkout view is using 
    the correct template when used
    """

    def test_get_view_checkout(self):
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')