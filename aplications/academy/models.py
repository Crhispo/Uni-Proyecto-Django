from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=30)
    credits = models.PositiveBigIntegerField()

    def __str__(self):
        text = "{0} - ({1})"
        return text.format(self.name,self.credits)