from django.test import TestCase
from .models import neighbourhood,healthservices
from django.contrib.auth.models import User
import datetime as dt
# Create your tests here.
class neighbourhoodTestClass(TestCase):
    def setUp(self):
        self.Kasarani = neighbourhood(neighbourhood='Kasarani')

    def test_instance(self):
        self.assertTrue(isinstance(self.Kasarani,neighbourhood))

    def tearDown(self):
        neighbourhood.objects.all().delete()

    def test_save_method(self):
        self.Kasarani.save_neighbourhood()
        hood = neighbourhood.objects.all()
        self.assertTrue(len(hood)>0)

    def test_delete_method(self):
        self.Kasarani.delete_neighbourhood('Kasarani')
        hood = neighbourhood.objects.all()
		self.assertTrue(len(hood)==0)