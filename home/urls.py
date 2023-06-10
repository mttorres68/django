from rest_framework.routers import SimpleRouter
from .views import (
  DisciplinaViewSet, CardViewSet
)

router = SimpleRouter()
router.register('disciplina', DisciplinaViewSet)
router.register('card', CardViewSet)
