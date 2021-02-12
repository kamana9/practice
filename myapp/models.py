from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=40)
    age=models.IntegerField()
    status=models.TextField()
    image=models.ImageField(upload_to="media")
    def __str__(self):
        return self.name
  
    class Meta:
        verbose_name="Person"
        verbose_name_plural="People"    