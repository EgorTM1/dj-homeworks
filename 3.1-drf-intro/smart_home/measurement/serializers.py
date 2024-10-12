from rest_framework import serializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Sensor, Measurement


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement

        fields = ["id", "sensor", "temperature", "created_at", "image"]


class SensorSerializer(serializers.ModelSerializer):
    measurements = serializers.SerializerMethodField()

    class Meta:
        model = Sensor

        fields = ["id", "name", "description", "measurements"]

    def get_measurements(self, obj):
        measurements = obj.measurements.all()
        serializer = MeasurementSerializer(measurements, many=True)
        return serializer.data


class SensorListCreateView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer