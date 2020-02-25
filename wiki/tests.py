from django.test import TestCase
from django.contrib.auth.models import User
from wiki.models import Page

class WikiTestCase(TestCase): #class name - inherits from test case
    def test_true_is_true(self): #unit test to true is true
        """ Tests is Trues is equal to True. Should always pass. """ 
        self.assertEqual(True, True) 

    def test_page_slugify_on_save(self):
        """ Tests the slug generated when saving a Page. """
        user = User()
        user.save()

        page = Page(title="My Test Page", content="test", author=user)
        page.save()

        self.assertEqual(page.slug, "my-test-page")

class PageListViewTests(TestCase):
    def tesy_multiple_pages(self):
        user = User.objects.create()

        Page.objects.create(title="My Test Page", content="test", author=user)
        Page.objects.create(title="Other", content="test", author=user)

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        responses = response.context['pages']
        self.assertEqual(len(responses), 2)

        self.assertQueryEqual(
            responses, 
            ['<Page: My Test Page', '<Page:Other'],
            ordered=False
        )