from django.test import TestCase
from django.urls import reverse

from home.models import Disciplina

class DisciplinaListViewTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    # CREATE 15 DISCIPLINAS PARA PAGINAÇÃO TEST
    number_of_disciplina = 15

    for disciplina_id in range(number_of_disciplina):
      Disciplina.objects.create(
        name=f'Eng.Soft {disciplina_id}',
        name_assunto=f'sommerville {disciplina_id}',
        description=f'seila {disciplina_id}',
      )

  def test_view_url_exists(self):
    response = self.client.get('/disciplina/')
    self.assertEqual(response.status_code, 200)

  def test_view_url_accessible_by_name(self):
    response = self.client.get(reverse('disciplina-list'))
    self.assertEqual(response.status_code, 200)