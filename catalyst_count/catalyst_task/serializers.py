from rest_framework import serializers
from .models import myfile

class MyFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = myfile
        fields = '__all__'
