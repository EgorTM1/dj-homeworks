from django.urls import path

from school.views import students_list

urlpatterns = [
    path("students/", students_list, name="students"),
    path("test_students/", students_list, name="test_students"),
    path(
        "test_student_without_teacher/",
        lambda request: students_list(request),
        name="test_student_without_teacher",
    ),
    path(
        "test_empty_class/",
        lambda request: students_list(request),
        name="test_empty_class",
    ),
    path(
        "test_debug_mode/",
        lambda request: students_list(request),
        name="test_debug_mode",
    ),
]
