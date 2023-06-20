from rest_framework.routers import SimpleRouter
from .views import (
  DisciplinaViewSet, CardViewSet
)

router = SimpleRouter()
router.register('disciplina', DisciplinaViewSet, basename='disciplina')
router.register('card', CardViewSet, basename='card')
