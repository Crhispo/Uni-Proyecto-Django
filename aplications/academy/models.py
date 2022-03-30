from django.db import models
from .choises import sexo

# Create your models here.


class Teacher(models.Model):
    """Model definition for Teacher."""

    # TODO: Define fields here

    apellido_paterno = models.CharField(
        max_length=20, verbose_name='Apellido paterno')
    apellido_materno = models.CharField(
        max_length=20, verbose_name='Apellido materno')
    nombres = models.CharField(max_length=20, verbose_name='Nombres')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    sexo = models.CharField(max_length=1, choices=sexo, default='F')

    def nombre_completo(self):
        return "{} {}, {}".format(self.apellido_paterno, self.apellido_materno, self.nombres)

    class Meta:
        """Meta definition for Teacher."""

        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
        db_table = 'Tbl_Teacher'
        ordering = ['apellido_paterno', '-apellido_materno']

    def __str__(self):
        """Unicode representation of Teacher."""
        return self.nombre_completo()


class Course(models.Model):
    name = models.CharField(max_length=30)
    credits = models.PositiveBigIntegerField()
    teacherFK = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)

    def __str__(self):
        text = "{0} - ({1})"
        return text.format(self.name, self.credits)
