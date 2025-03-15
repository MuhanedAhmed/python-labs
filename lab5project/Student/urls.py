from django.urls import path
from Student.views import get_all_students, get_single_student

urlpatterns = [
    path('', get_all_students),
    path('<int:id>',get_single_student)
]