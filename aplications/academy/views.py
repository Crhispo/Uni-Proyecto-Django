from django.views.generic import ListView
from django.shortcuts import redirect, render
from .models import Course
# Create your views here.


# def home(request):
    # cursosListados = Course.objects.all().order_by("-name")
    # return render(request, "gestionCursos.html", {"cursos": cursosListados})


class CourseListView(ListView):
    model = Course
    template_name = 'gestionCursos.html'

    def get_queryset(self):
        getCourse = Course.objects.all().order_by('id')
        return getCourse

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Gestion de cursos"
        return context

def registrarCurso(request):
    Course_Re = request.POST
    Course.objects.create(name=Course_Re['txtNombre'],credits= Course_Re['numCredito'])
    return redirect('/')

def eliminarCurso(request,id):
    Course_el = Course.objects.get(id=id)
    Course_el.delete()
    return redirect('/')
