from django.db import models

# Create your models here.

class Disciplina(models.Model):
  name = models.CharField(max_length=30)
  name_assunto = models.CharField(max_length=100)
  description = models.CharField(max_length=100)