from rest_framework import serializers
from voting.models import vote_info

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = vote_info
        fields = ['agree', 'email']
