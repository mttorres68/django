from django.contrib import admin
from .models import Disciplina, Card

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
  list_display = ('name', 'name_assunto', 'description')

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
  list_display = ('id', 'question', 'response', 'disciplina')