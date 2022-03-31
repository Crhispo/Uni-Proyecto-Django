from django.contrib import admin
from .models import Course, Teacher

# Register your models here.

# admin.site.register(Course)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('id','name','credits')
    list_editable = ('name','credits')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('id','apellido_paterno','apellido_materno')