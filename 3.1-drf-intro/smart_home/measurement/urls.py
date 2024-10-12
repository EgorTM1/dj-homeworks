from django.urls import path
from .views import (
    api_root,
    SensorListCreateAPIView,
    SensorRetrieveUpdateAPIView,
    MeasurementListCreateAPIView,
    MeasurementRetrieveUpdateAPIView,
    MeasurementImageView,
)

urlpatterns = [
    path('', api_root, name='api_root'),
    path('sensors/', SensorListCreateAPIView.as_view(), name='sensor_list'),
    path('sensors/<int:pk>/', SensorRetrieveUpdateAPIView.as_view(), name='sensor_detail'),
    path('measurements/', MeasurementListCreateAPIView.as_view(), name='measurement_list'),
    path('measurements/<int:pk>/image/', MeasurementImageView.as_view(), name='view_measurement_image'),
]