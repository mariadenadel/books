from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView

class HomepageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.responce = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.responce.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.responce, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.responce, 'Homepage')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.responce, 'Hi! I should not be here!')

    def test_homepage_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )

class AboutPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('about')
        self.responce = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.responce.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.responce, 'about.html')

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.responce, 'About Page')

    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.responce, 'Hi! I should not be here!')

    def test_aboutpage_resolves_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )