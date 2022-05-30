from django.test import TestCase
from .models import NetWorking, SocialNetworks
# Create your tests here.

class social_netwoking(TestCase):
    """ testing for models"""
    def setUp(self): # Construye el objeto a verificar
        self.net_working = NetWorking.objects.create()
        self.socials_networks = SocialNetworks.objects.create(user=self.net_working)

    def test_social_netwoking(self):
        self.assertTrue(isinstance(self.net_working, NetWorking))
        self.assertTrue(isinstance(self.socials_networks, SocialNetworks))