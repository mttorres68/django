from rest_framework import viewsets
from .serializers import DisciplinaSerializer, CardSerializer
from .models import Disciplina, Card
from rest_framework.response import Response


class DisciplinaViewSet(viewsets.ModelViewSet):
  queryset = Disciplina.objects.all()
  serializer_class = DisciplinaSerializer

class CardViewSet(viewsets.ModelViewSet):
  queryset= Card.objects.all()
  serializer_class = CardSerializer

  def post(self, request, format=None):
    serializer = CardSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)