from rest_framework import viewsets
from .serializers import DisciplinaSerializer
from .models import Disciplina


class DisciplinaViewSet(viewsets.ModelViewSet):
  queryset = Disciplina.objects.all()
  serializer_class = DisciplinaSerializer