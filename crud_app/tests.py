
from django.test import TestCase
#importadas
from django.test import SimpleTestCase # para el testo de paginas estaticas
from django.urls import reverse
from .models import Persona
# Create your tests here.


#Selenium libreria

class InicioTest(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/inicio_test')
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('inicio'))
        self.assertEqual(response.status_code, 200)
    
    def test_template_name_correct(self):
        response = self.client.get(reverse('inicio'))
        self.assertTemplateUsed(response, 'inicio_test.html')
    
    def test_template_content(self):
        response = self.client.get(reverse('inicio'))
        self.assertContains(response, '<h1>Página de inicio</h1>')
        self.assertNotContains(response, 'No es la pagina')


class PersonaTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.persona =  Persona.objects.create(nombre_completo = 'Christian Donoso',
                                              peso = '75000',
                                              talla='175')
    
    def test_model_content(self):
        self.assertEqual(self.persona.nombre_completo, 'Christian Donoso')
        self.assertEqual(self.persona.peso, '75000')
        self.assertEqual(self.persona.talla, '175')