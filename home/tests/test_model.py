from django.test import TestCase
from home.models import Disciplina

class DisciplinaTestCase(TestCase):
  @classmethod
  def setUpTestData(cls):
    Disciplina.objects.create(name = 'Quimica', name_assunto = 'Entalpia', description = '...')

  def test_name(self):
    disciplina = Disciplina.objects.get(id=1)
    name = disciplina._meta.get_field('name').verbose_name
    self.assertEquals(name, 'name')

  def test_name_max_length(self):
    disciplina = Disciplina.objects.get(id=1)
    max_length = disciplina._meta.get_field('name').max_length
    self.assertEquals(max_length, 30 )
