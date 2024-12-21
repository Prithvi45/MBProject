from rest_framework import serializers
from .models import DummyData


class DummyDataSerializer(serializers.Serializer):
    ten_min_std_deviation = serializers.CharField()
    time = serializers.CharField()
    datetime = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S")  # ISO format
    ten_min_sampled_avg = serializers.CharField()
