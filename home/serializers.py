from rest_framework import serializers
from .models import Disciplina, Card

class DisciplinaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Disciplina
    fields = '__all__'
class CardSerializer(serializers.ModelSerializer):
  disciplina = serializers.PrimaryKeyRelatedField(queryset=Disciplina.objects.all())
  class Meta:
    model = Card
    fields = ('question', 'response', 'disciplina')