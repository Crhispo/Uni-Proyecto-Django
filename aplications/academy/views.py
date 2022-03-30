from django.views.generic import ListView
from pydoc import classname
from django.shortcuts import render
from .models import Course
# Create your views here.


def home(request):
    cursosListados = Course.objects.all().order_by("-name")
    return render(request, "gestionCursos.html", {"cursos": cursosListados})


class CourseListView(ListView):
    model = Course
    template_name = 'gestionCursos.html'

    def get_queryset(self):
        Course.objects.all()
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Gestion de cursos"
        return context
