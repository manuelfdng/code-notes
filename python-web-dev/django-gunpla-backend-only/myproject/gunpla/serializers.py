# gunpla/serializers.py
from rest_framework import serializers
from .models import Gunpla

class GunplaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gunpla
        fields = ['id', 'name', 'series', 'grade', 'scale']

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name field is required.")
        return value

    def validate_series(self, value):
        if not value:
            raise serializers.ValidationError("Series field is required.")
        return value

    def validate_grade(self, value):
        if not value:
            raise serializers.ValidationError("Grade field is required.")
        return value