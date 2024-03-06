from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()

    class Meta:
        model = Note
        fields = ('id', 'title', 'content', 'owner', 'created_at')
        extra_kwargs = {'created_at':{'read_only':True}, 'owner':{'read_only':True}, 'id': {'read_only': True}}
    
    def get_owner(self, obj):
        return obj.owner.first_name if obj.owner else None


