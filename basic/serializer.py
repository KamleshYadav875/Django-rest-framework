from rest_framework import serializers
from .models import Pra

class PraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pra
        fields = '__all__'