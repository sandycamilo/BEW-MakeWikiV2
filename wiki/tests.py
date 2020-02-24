from django.test import TestCase

class WikiTestCase(TestCase):
    def test_true_is_true(self):
        """ Tests is Trues is equal to True. Should always pass. """ 
        self.assertEqual(True, True)