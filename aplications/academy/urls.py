from django.urls import path
from aplications.academy.views import CourseListView

urlpatterns = [
    path('', CourseListView.as_view(), name='Gestion_cursos')
]
