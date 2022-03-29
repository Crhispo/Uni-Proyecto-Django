from django.shortcuts import render
from .models import Course
# Create your views here.


def home(request):
    cursosListados = Course.objects.all().order_by("-name")
    return render(request, "gestionCursos.html", {"cursos": cursosListados})
