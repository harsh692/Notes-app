from rest_framework.serializers import ModelSerializer
from .models import Notes 

class NoteSerialiser(ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__' ## serialise all fields
