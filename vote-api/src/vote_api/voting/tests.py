import json
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from voting.models import vote_info
from voting import serializer

'''
class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {
            'agree': True,
            'email': 'test@localhost.app',
        }
        response = self.client.post("api/rest-auth/registration/", data)
        self.asserEqual(response.status_code, status.HTTP_201_CREATED)
'''
