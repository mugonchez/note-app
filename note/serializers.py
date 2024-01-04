from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()

    class Meta:
        model = Note
        fields = ('title', 'content', 'owner', 'created_at')
        extra_kwargs = {'created_at':{'read_only':True}, 'owner':{'read_only':True}}
    
    def get_owner(self, obj):
        return obj.owner.first_name if obj.owner else None

    def create(self, validated_data):
        # Retrieve the authenticated user from the request object
        user = self.context['request'].user

        # Add the user to the validated data before creating the note
        validated_data['owner'] = user

        return super().create(validated_data)

