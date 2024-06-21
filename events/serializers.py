from rest_framework import serializers
from .models import Event, Participant

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['id', 'name', 'email']

class EventSerializer(serializers.ModelSerializer):
    participants = ParticipantSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'name', 'location', 'date', 'description', 'participants']
    def get_participants_count(self, obj):
        return obj.participants.count()
