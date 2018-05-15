 # -*- coding: utf-8 -*-
from __future__ import unicode_literals
import models
import views
from django.urls import resolve, reverse
from django.http import HttpRequest
import os
import json

from django.test import TestCase
from selenium import webdriver

from selenium.webdriver.support.select import Select
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By


def getRealPath(rel_path):
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    abs_file_path = os.path.join(script_dir, rel_path)
    return os.path.realpath(abs_file_path)

# class Test(TestCase):

# # test para validar el funcionamiento del servicio para eliminar herramientas
#     def test_HerramintaDelete(self):
#         herramienta = models.Herramienta.objects.create(nombre='Herramienta test', descripcion='')
#         if herramienta:
#             url = reverse('herramienta-delete', args=[herramienta.id])
#             response = self.client.delete(url)
#             self.assertEqual(response.status_code, 200)
#             self.assertEqual(response['content-type'], 'application/json')
#
#
# #test para validar el funcionamiento del servicio que permite obtener todas las categorias
#     def test_getCategorias(self):
#         models.Categoria.objects.create(nombre='categoria test', descripcion='cat1')
#         models.Categoria.objects.create(nombre='categoria test1', descripcion='cat2')
#         url = reverse('categoria')
#         response = self.client.get(url)
#         arr = json.loads(response.content)
#         self.assertEqual(arr[0]['fields']['nombre'], 'categoria test')
#
# #test para el metodo de filtrar herramientas por sistema opeativo en la home. PC19
#     def test_filtrar_herramienta_metodo(self):
#         lista_herramientas = models.Herramienta.objects.filter(sistema_operativo__icontains='windows')
#         if lista_herramientas:
#             url = reverse('home')
#             response = self.client.delete(url)
#             self.assertEqual(response.status_code, 200)
#             self.assertEqual(response['content-type'], 'application/json')
#
# #test para el metodo de filtrar herramientas por tipo de licencia en la home. PC20
#     def test_filtrar_herramienta_metodo_licencia(self):
#         lista_herramientas = models.Herramienta.objects.filter(licencia__icontains='asd')
#         if lista_herramientas:
#             url = reverse('home')
#             response = self.client.delete(url)
#             self.assertEqual(response.status_code, 200)
#             self.assertEqual(response['content-type'], 'application/json')
#
# #test para el metodo de filtrar herramientas por tipo de licencia en la home. PC14
#     def test_filtrar_herramienta_metodo_uso(self):
#         lista_herramientas = models.Herramienta.objects.all()
#         print lista_herramientas
#         if lista_herramientas:
#             url = reverse('home')
#             response = self.client.delete(url)
#             self.assertEqual(response.status_code, 200)
#             self.assertEqual(response['content-type'], 'application/json')

usuario_prueba= "tj.marrugo10@uniandes.edu.co"
usuario_gti_prueba="pruebabuglogin@uniandes.edu.co"
usuario_prueba_local= "pruebabug5@uniandes.edu.co"
clave_prueba = "admin123456"
clave_prueba_local="administrador"
sistema_operativo_prueba="windows"# valor para prueba selenium PC19
usuario_pruebaAdmin = "usr.admin@uniandes.edu.co"
usuario_pruebaAdmin_clave = "admin123456"
usuario_pruebaGTI = "usr.gti@uniandes.edu.co"
usuario_pruebaGTI_clave = "admin123456"

class AtoTest(TestCase):
    # test automatico para validar el funcionamiento del servicio para eliminar herramientas
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.set_window_size(1024, 786)
        self.browser.implicitly_wait(2)


    def tearDown(self):
        self.browser.quit()


    # def test_EliminarHerramienta(self):
    #     self.browser.get('https://final-conectate-group4.herokuapp.com/herramientas')
    #     link = self.browser.find_element_by_id('login')
    #     link.click()
    #     self.browser.implicitly_wait(10)
    #     input_email = self.browser.find_element_by_id('email')
    #     input_email.send_keys(usuario_pruebaAdmin)
    #     input_pass = self.browser.find_element_by_id('password')
    #     input_pass.send_keys(usuario_pruebaAdmin_clave)
    #     btn_login = self.browser.find_element_by_id('btn_login')
    #     btn_login.click()
    #     self.browser.implicitly_wait(10)
    #     l2 = self.browser.find_element_by_id('menuHerramientas')
    #     l2.click()
    #     self.browser.implicitly_wait(10)
    #     l3 = self.browser.find_element_by_id('itemListaHerrramienta')
    #     l3.click()
    #     self.browser.implicitly_wait(10)
    #     l4 = self.browser.find_elements(By.XPATH, '//a[text()="Eliminar"]')
    #     #l4 = self.browser.find_element_by_id('del_2')
    #     l4[1].click()
    #     self.browser.implicitly_wait(10)
    #     alert = self.browser.switch_to_alert()
    #     alert.accept()
    #     self.browser.implicitly_wait(10)
    #     success = self.browser.find_element_by_id("id_success")
    #     self.assertIsNotNone(success)
    #
    #
    # # prueba unitaria  automatica para PC20
    # def test_FiltroTipolicencia(self):
    #     self.browser.get('https://final-conectate-group4.herokuapp.com/herramientas')
    #     input=self.browser.find_element_by_id('tipo_licencia')
    #     input.send_keys('GPL')
    #     submit=self.browser.find_element_by_id('btnFiltrar')
    #     submit.click()
    #     self.browser.implicitly_wait(2)
    #     herramientas = self.browser.find_element_by_id('herramientas').find_elements_by_xpath(".//*")
    #     self.assertNotEqual(len(herramientas),0,"no hay herramientas cuando deberian haber")
    #     h2 = self.browser.find_element(By.XPATH, '//a[text()=" TUTORIAL PYTHON"]')
    #     self.assertIsNotNone(h2,"no existe la herramienta que deberia estar")
    #     input = self.browser.find_element_by_id('tipo_licencia')
    #     input.clear()
    #     input.send_keys('pruebavacio')
    #     submit = self.browser.find_element_by_id('btnFiltrar')
    #     submit.click()
    #     self.browser.implicitly_wait(2)
    #     herramientas = self.browser.find_element_by_id('herramientas').find_elements_by_xpath(".//*")
    #     self.assertEqual(len(herramientas),0,"existen herramientas cuando no deberian haber")
    #
    # #prueba unitaria  automatica para PC14
    # def test_FitroPorUso(self):
    #     self.browser.get('https://final-conectate-group4.herokuapp.com/herramientas')
    #     link=self.browser.find_element_by_id('login')
    #     link.click()
    #     self.browser.implicitly_wait(10)
    #     input_email = self.browser.find_element_by_id('email')
    #     input_email.send_keys(usuario_gti_prueba)
    #     input_pass = self.browser.find_element_by_id('password')
    #     input_pass.send_keys(clave_prueba_local)
    #     btn_login = self.browser.find_element_by_id('btn_login')
    #     btn_login.click()
    #     self.browser.implicitly_wait(2)
    #     input = self.browser.find_element_by_id('uso')
    #     input.send_keys('Educación')
    #     submit = self.browser.find_element_by_id('btnFiltrar')
    #     submit.click()
    #     self.browser.implicitly_wait(2)
    #     herramientas = self.browser.find_element_by_id('herramientas').find_elements_by_xpath(".//*")
    #     self.assertNotEqual(len(herramientas),0,"no hay herramientas cuando deberian haber")
    #     h2 = self.browser.find_element(By.XPATH, '//a[text()=" Plataforma de Programacion"]')
    #     self.assertIsNotNone(h2, "no existe la herramienta que deberia estar")
    #
    #     input = self.browser.find_element_by_id('uso')
    #     input.clear()
    #     input.send_keys('pruebavacio')
    #     submit = self.browser.find_element_by_id('btnFiltrar')
    #     submit.click()
    #     self.browser.implicitly_wait(2)
    #     herramientas = self.browser.find_element_by_id('herramientas').find_elements_by_xpath(".//*")
    #     self.assertEqual(len(herramientas),0,"existen herramientas cuando no deberian haber")
    #
    #
    # def test_FiltroCategoria(self):
    #     self.browser.get('https://final-conectate-group4.herokuapp.com/herramientas/')
    #     link = self.browser.find_element_by_id('login')
    #     link.click()
    #     self.browser.implicitly_wait(10)
    #     input_email = self.browser.find_element_by_id('email')
    #     input_email.send_keys(usuario_pruebaGTI)
    #     input_pass = self.browser.find_element_by_id('password')
    #     input_pass.send_keys(usuario_pruebaGTI_clave)
    #     btn_login = self.browser.find_element_by_id('btn_login')
    #     btn_login.click()
    #     self.browser.implicitly_wait(10)
    #     select = Select(self.browser.find_element_by_id('categorias'))
    #     select.select_by_visible_text('documento de word')
    #     btn_Filtrar = self.browser.find_element_by_id('btnFiltrar')
    #     btn_Filtrar.click()
    #     self.browser.implicitly_wait(10)
    #     ele = self.browser.find_element(By.XPATH, '//a[text()=" Herramienta En Revision"]')
    #     self.assertEqual(ele.text,'Herramienta En Revision')
    #
    # #Prueba unitaria automatica para PC19
    # def test_filtrar_sistema_operativo(self):
    #     self.browser.get('https://final-conectate-group4.herokuapp.com/herramientas')
    #     input_sistema_operativo = self.browser.find_element_by_id('sistema_operativo')
    #     input_sistema_operativo.send_keys(sistema_operativo_prueba)
    #     btn_filtrar = self.browser.find_element_by_id("btnFiltrar")
    #     btn_filtrar.click()
    #     self.browser.get('https://final-conectate-group4.herokuapp.com/herramientas/?sistema_operativo=windows&tipo_licencia=')
    #     titulo= self.browser.find_element(By.XPATH,'//*[@id="herramienta_26_nombre"]/a')
    #     self.assertIn('TUTORIAL PYTHON',titulo.text)
    #     categoria = self.browser.find_element(By.XPATH,'//*[@id="herramientas"]/div/div/div[2]/h6')
    #     self.assertIn("documento de word",categoria.text)
    #     self.browser.implicitly_wait(60)
    #
    # #prueba unitaria automatica para PC15
    # def test_detalle_herramienta_publica(self):
    #     inicializacion(self)
    #     datos_parte1(self)
    #     datos_laterales(self)

    #prueba unitaria automatica para PC172
    def test_reporte_con_ejemplos_uso(self):
        self.browser.get('https://final-conectate-group4.herokuapp.com/herramientas')
        link = self.browser.find_element_by_id('login')
        link.click()
        self.browser.implicitly_wait(3)
        input_email = self.browser.find_element_by_id('email')
        input_email.send_keys(usuario_prueba)
        input_pass = self.browser.find_element_by_id('password')
        input_pass.send_keys(usuario_pruebaAdmin_clave)
        btn_login = self.browser.find_element_by_id('btn_login')
        btn_login.click()
        self.browser.implicitly_wait(3)
        l2 = self.browser.find_element_by_id('menuHerramientas')
        l2.click()
        self.browser.implicitly_wait(3)
        l3 = self.browser.find_element_by_id('reporteHerramientas')
        l3.click()
        self.browser.implicitly_wait(3)
        cantidadEjemplos = self.browser.find_element_by_id('herramientas').find_element(By.XPATH,'//tr/td[6]/a')
        cantidadEjemplos.click()
x


#refactor PC194
# def inicializacion(self):
#     self.browser.get('https://final-conectate-group4.herokuapp.com/herramientas/')
#     span = self.browser.find_element(By.XPATH, '//*[@id="herramienta_26_nombre"]/a')
#     span.click()
#
# def datos_parte1(self):
#     h2 = self.browser.find_element(By.XPATH, '/html/body/div/div/div[1]/h1')
#     self.assertIn('TUTORIAL PYTHON', h2.text)
#     h3 = self.browser.find_element(By.XPATH, '/html/body/div/div/div[1]/p[1]')
#     self.assertIn('Estado: Público', h3.text)
#     h4 = self.browser.find_element(By.XPATH, '/html/body/div/div/div[1]/p[2]')
#     self.assertIn('Versión: 1', h4.text)
#     h5 = self.browser.find_element(By.XPATH, '/html/body/div/div/div[1]/p[3]')
#     self.assertIn(
#         'Mediante el presente tutorial se presente hacer una aplicación básica en donde se creara la estructura de una galería de imágenes, se usará Python+Django como plataforma de desarrollo debido a que incluyen funcionalidades muy beneficiosas para hacer desarrollo en menos tiempo',
#         h5.text)
#     h6 = self.browser.find_element(By.XPATH, '/html/body/div/div/div[1]/p[4]')
#     self.assertIn('GPL', h6.text)
#
# def datos_laterales(self):
#     h7 = self.browser.find_element(By.XPATH, '/html/body/div/div/div[1]/p[5]')
#     self.assertIn('Curso en Moodle', h7.text)
#     h8 = self.browser.find_element(By.XPATH, '/html/body/div/div/div[1]/p[6]')
#     self.assertIn(
#         'http://moodleinstitucional.uniandes.edu.co/pluginfile.php/157272/mod_label/intro/TutorialDjangoGuia1.pdf',
#         h8.text)
#     h9 = self.browser.find_element(By.XPATH, '/html/body/div/div/div[1]/p[7]')
#     self.assertIn(
#         'http://moodleinstitucional.uniandes.edu.co/pluginfile.php/157272/mod_label/intro/TutorialDjangoGuia1.pdf',
#         h9.text)
#     h10 = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/div')
#
#     self.assertIn('Academico', h10.text)
#     h11 = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div[3]/div')
#     self.assertIn('windows', h11.text)
#     h12 = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div[4]/div')
#     self.assertIn('pertenece al curso MISO 4101', h12.text)
#     h13 = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div[5]/div')
#     self.assertIn('http://moodleinstitucional.uniandes.edu.co/course/view.php?id=1242&section=24', h13.text)
#     self.browser.implicitly_wait(10)

