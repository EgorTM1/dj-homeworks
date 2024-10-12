from django.conf import settings

from django.shortcuts import render
import logging

from .models import Student, Teacher

logger = logging.getLogger(__name__)


def students_list(request):
    logger.info("Starting students_list request")

    template = "school/students_list.html"

    students = Student.objects.prefetch_related("teachers").all

    context = {
        "students": students,
        "debug": settings.DEBUG
    }

    return render(request, template, context)
