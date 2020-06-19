from django.shortcuts import render

from rest_framework import viewsets
from voting.serializers import VoteSerializer
from voting.models import vote_info
from rest_framework.response import Response
from rest_framework import status
from rest_framework.throttling import UserRateThrottle

from collections import Counter

# Create your views here.
class votingViewSet(viewsets.ViewSet):
    """ Voting Viewset """

    serializer_class = VoteSerializer
    throttle_classes = [UserRateThrottle]

    def list(self, request):
        """ list voted result """
        agree = vote_info.objects.raw("SELECT *, count(*) as count FROM VOTE WHERE agree = 1", [])
        disagree = vote_info.objects.raw("SELECT *, count(*) as count FROM VOTE WHERE agree = 0", [])

        counts = {
            'agree' : getattr(agree[0], 'count'),
            'disagree'    : getattr(disagree[0], 'count'),
        }

        return Response({'message': 'This is the counts of the poll!', 'poll': counts})

    def create(self, request):
        """ create a new vote  """

        serializer = VoteSerializer(data=request.data)
        message = {
            'status': 'OK',
            'agree': True,
            'email': '',
        }

        if serializer.is_valid():
            agree = serializer.data.get('agree')
            email = serializer.data.get('email')
            vote_info.objects.create(agree=agree, email=email)
            message['agree'] = agree
            message['email'] = email
            return Response({'response': message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
