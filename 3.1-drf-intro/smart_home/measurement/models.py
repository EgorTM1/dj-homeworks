from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=100, help_text="Название датчика")

    description = models.TextField(
        null=True, blank=True, help_text="Описание датчика"
    )

    def __str__(self):
        return f"{self.name}: {self.description or 'No description'}"


class Measurement(models.Model):
    sensor = models.ForeignKey(
        Sensor,
        related_name="measurements",
        on_delete=models.CASCADE,
        help_text="Связанный датчик",
    )

    temperature = models.FloatField(help_text="Измеренная температура")

    created_at = models.DateTimeField(
        auto_now_add=True, help_text="Дата и время измерения"
    )

    image = models.ImageField(
        upload_to="sensor_measurements/",
        null=True,
        blank=True,
        help_text="Изображение измерения",
    )

    def __str__(self):
        return f"Измерение датчика {self.sensor.name}: {self.created_at}"
