from rest_framework import viewsets
from .serializers import DisciplinaSerializer, CardSerializer
from .models import Disciplina, Card
from rest_framework.response import Response
from .filters import CardFilter
from rest_framework.decorators import action
import json

class DisciplinaViewSet(viewsets.ModelViewSet):
  queryset = Disciplina.objects.all()
  serializer_class = DisciplinaSerializer

class CardViewSet(viewsets.ModelViewSet):
  queryset = Card.objects.all()
  serializer_class = CardSerializer
  filterset_class = CardFilter

  # def list(self, request, *args, **kwargs):
  #   id_disciplina = self.kwargs.get('pk')
  #   print(id_disciplina)
  #   queryset= Card.objects.filter(disciplina = id_disciplina)
  #   return Response(self.serializer_class(queryset, many=True).data, status=status.HTTP_200_OK) 

  def post(self, request, format=None):
    serializer = CardSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)