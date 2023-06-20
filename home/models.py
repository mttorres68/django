from django.db import models

# Create your models here.

class Disciplina(models.Model):
  name = models.CharField(max_length=30)
  name_assunto = models.CharField(max_length=100)
  description = models.CharField(max_length=100)

class Card(models.Model):
  question = models.CharField(max_length=80)
  response = models.CharField(max_length=100)
  disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, null=True)

  def __str__(self):
    return self.question