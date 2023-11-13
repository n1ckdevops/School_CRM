from django.test import TestCase
from django.shortcuts import reverse

class LandingPageTest(TestCase):
    def test_status_code(self):
        response = self.client.get(reverse('landing-page'))
        self.assertEquals(response.status_code, 200)
    # def test_template_name(self):
    #     pass
