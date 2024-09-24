from django.test import SimpleTestCase

# Create your tests here.

class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_loc(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)

class AboutPageTests(SimpleTestCase):
    def test_url_exists_at_correct_loc(self):
        res = self.client.get("/about/")
        self.assertEqual(res.status_code, 200)
