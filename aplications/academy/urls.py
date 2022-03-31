from django.urls import path
from aplications.academy.views import CourseListView, eliminarCurso, registrarCurso

urlpatterns = [
    path('', CourseListView.as_view(), name='Gestion_cursos'),
    path('RegistrarCurso/', registrarCurso),
    path('EliminarCurso/<int:id>', eliminarCurso),
]
