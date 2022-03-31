from unicodedata import name
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

def editarCurso(request,id):
    Course_ed = Course.objects.get(id=id)
    data = {
        'titulo': 'Edicion Curso',
        'curso': Course_ed,
    }
    return render(request, "edicionCurso.html", data)

def editarunCurso(request):
    id = request.POST['id']
    name = request.POST['txtNombre']
    credits = request.POST['numCredito']
    Course_ = Course.objects.get(id=id)
    Course_.name = name
    Course_.credits = credits
    Course_.save()
    return redirect('/')
