from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer
from django.http import HttpResponse

@api_view(["GET"])
def api_root(request):
    return Response(
        {
            "message": "Welcome to Smart Home API!",
            "endpoints": {
                "sensors": {
                    "list": "/api/sensors/",
                    "detail": "/api/sensors/<int:pk>/",
                    "create": "/api/sensors/",
                    "update": "/api/sensors/<int:pk>/",
                    "delete": "/api/sensors/<int:pk>/",
                },
                "measurements": {
                    "list": "/api/measurements/",
                    "create": "/api/measurements/",
                    "view-image": "/api/measurements/<int:pk>/image/",
                },
            },
        }
    )

class SensorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class MeasurementListCreateAPIView(generics.ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

class MeasurementRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

class MeasurementImageView(generics.RetrieveAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def get(self, request, pk):
        measurement = Measurement.objects.get(pk=pk)

        if measurement.image:
            response = HttpResponse(content_type="image/jpeg")
            response["Content-Disposition"] = (
                f'inline; filename="measurement_{pk}.jpg"'
            )
            response.write(measurement.image.open().read())
            return response

        else:
            return Response(
                {"message": "Изображение отсутствует"}, status=status.HTTP_200_OK
            )
        