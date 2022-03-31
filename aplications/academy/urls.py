from django.urls import path
from aplications.academy.views import CourseListView, eliminarCurso, registrarCurso, editarCurso, editarunCurso

urlpatterns = [
    path('', CourseListView.as_view(), name='Gestion_cursos'),
    path('RegistrarCurso/', registrarCurso),
    path('EliminarCurso/<int:id>', eliminarCurso),
    path('EditarCurso/<int:id>', editarCurso),
    path('EditaunrCurso/', editarunCurso),
]
