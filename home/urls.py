from rest_framework.routers import SimpleRouter
from .views import (
  DisciplinaViewSet
)

router = SimpleRouter()
router.register('disciplina', DisciplinaViewSet)
