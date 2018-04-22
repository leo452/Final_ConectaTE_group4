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

class Test(TestCase):

# test para validar el funcionamiento del servicio para eliminar herramientas
    def test_HerramintaDelete(self):
        herramienta = models.Herramienta.objects.create(nombre='Herramienta test', descripcion='')
        if herramienta:
            url = reverse('herramienta-delete', args=[herramienta.id])
            response = self.client.delete(url)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response['content-type'], 'application/json')


#test para validar el funcionamiento del servicio que permite obtener todas las categorias
    def test_getCategorias(self):
        models.Categoria.objects.create(nombre='categoria test', descripcion='cat1')
        models.Categoria.objects.create(nombre='categoria test1', descripcion='cat2')
        url = reverse('categoria')
        response = self.client.get('/herramientas/')
        arr = json.loads(response.content)
        self.assertEqual(arr[0]['fields']['nombre'], 'categoria test')

#test para el metodo de filtrar herramientas por sistema opeativo en la home. PC19
    def test_filtrar_herramienta_metodo(self):
        lista_herramientas = models.Herramienta.objects.filter(sistema_operativo__icontains='windows')
        if lista_herramientas:
            url = reverse('home')
            response = self.client.delete(url)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response['content-type'], 'application/json')

#test para el metodo de filtrar herramientas por tipo de licencia en la home. PC20
    def test_filtrar_herramienta_metodo_licencia(self):
        lista_herramientas = models.Herramienta.objects.filter(licencia__icontains='asd')
        if lista_herramientas:
            url = reverse('home')
            response = self.client.delete(url)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response['content-type'], 'application/json')

#test para el metodo de filtrar herramientas por tipo de licencia en la home. PC14
    def test_filtrar_herramienta_metodo_uso(self):
        lista_herramientas = models.Herramienta.objects.all()
        print lista_herramientas
        if lista_herramientas:
            url = reverse('home')
            response = self.client.delete(url)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response['content-type'], 'application/json')

usuario_prueba = "tj.marrugo10@uniandes.edu.co"
usuario_prueba_local= "pruebabug5@uniandes.edu.co"
clave_prueba = "admin123456"
clave_prueba_local="administrador"
sistema_operativo_prueba="windows"# valor para prueba selenium PC19

# class AtoTest(TestCase):
#     # test automatico para validar el funcionamiento del servicio para eliminar herramientas
#     def setUp(self):
#         #Windows
#         #self.browser = webdriver.Chrome(executable_path=r"extra/chromedriver.exe")
#         #ubuntu
#         self.browser= webdriver.Chrome()
#         self.browser.set_window_size(1024, 786)
#         self.browser.implicitly_wait(2)
#
#
#     def tearDown(self):
#         self.browser.quit()
#
#
#     def test_EliminarHerramienta(self):
#         self.browser.get('http://localhost:8000/herramientas')
#         #self.browser.get('https://final-conectate-group4.herokuapp.com/herramientas')
#         link = self.browser.find_element_by_id('login')
#         link.click()
#         self.browser.implicitly_wait(10)
#         input_email = self.browser.find_element_by_id('email')
#         input_email.send_keys(usuario_prueba)
#         input_pass = self.browser.find_element_by_id('password')
#         input_pass.send_keys(clave_prueba)
#         btn_login = self.browser.find_element_by_id('btn_login')
#         btn_login.click()
#         self.browser.implicitly_wait(10)
#         l2 = self.browser.find_element_by_id('menuHerramientas')
#         l2.click()
#         self.browser.implicitly_wait(10)
#         l3 = self.browser.find_element_by_id('itemListaHerrramienta')
#         l3.click()
#         self.browser.implicitly_wait(10)
#         l4 = self.browser.find_element_by_id('del_2')
#         l4.click()
#         self.browser.implicitly_wait(10)
#         alert = self.driver.browser.switch_to_alert()
#         alert.accept()
#         self.browser.implicitly_wait(10)
#         success = self.browser.find_element_by_id("id_success")
#         self.assertIsNotNone(success)
#
#     # prueba unitaria  automatica para PC20
#     def test_FiltroTipolicencia(self):
#         self.browser.get('http://localhost:8000/herramientas')
#         input=self.browser.find_element_by_id('tipo_licencia')
#         input.send_keys('asd')
#         submit=self.browser.find_element_by_id('btnFiltrar')
#         submit.click()
#         self.browser.implicitly_wait(2)
#         herramientas = self.browser.find_element_by_id('herramientas').find_elements_by_xpath(".//*")
#         self.assertNotEqual(len(herramientas),0,"no hay herramientas cuando deberian haber")
#         h2 = self.browser.find_element(By.XPATH, '//a[text()=" Herramienta Publica"]')
#         self.assertIsNotNone(h2,"no existe la herramienta que deberia estar")
#
#         input = self.browser.find_element_by_id('tipo_licencia')
#         input.clear()
#         input.send_keys('pruebaerror')
#         submit = self.browser.find_element_by_id('btnFiltrar')
#         submit.click()
#         self.browser.implicitly_wait(2)
#         herramientas = self.browser.find_element_by_id('herramientas').find_elements_by_xpath(".//*")
#         self.assertEqual(len(herramientas),0,"existen herramientas cuando no deberian haber")
#
#
#
#     def test_FiltroCategoria(self):
#         #self.browser.get('http://localhost:8000/herramientas')
#         self.browser.get('https://final-conectate-group4.herokuapp.com/herramientas')
#         link = self.browser.find_element_by_id('login')
#         link.click()
#         self.browser.implicitly_wait(10)
#         input_email = self.browser.find_element_by_id('email')
#         input_email.send_keys(usuario_prueba)
#         input_pass = self.browser.find_element_by_id('password')
#         input_pass.send_keys(clave_prueba)
#         btn_login = self.browser.find_element_by_id('btn_login')
#         btn_login.click()
#         self.browser.implicitly_wait(10)
#         select = Select(self.browser.find_element_by_id('categorias'))
#         #self.browser.implicitly_wait(5)
#         select.select_by_index(1)
#         btn_Filtrar = self.browser.find_element_by_id('btnFiltrar')
#         btn_Filtrar.click()
#         self.browser.implicitly_wait(10)
#         ele = self.browser.find_elements_by_xpath("//div[@class='card-header text-center']")
#         self.assertEqual(ele[1].text,'Herramienta En Revision')
#
#     #prueba unitaria  automatica para PC14
#     def test_FitroPorUso(self):
#         self.browser.get('http://localhost:8000/herramientas')
#         link=self.browser.find_element_by_id('login')
#         link.click()
#         self.browser.implicitly_wait(10)
#         input_email = self.browser.find_element_by_id('email')
#         input_email.send_keys(usuario_prueba_local)
#         input_pass = self.browser.find_element_by_id('password')
#         input_pass.send_keys(clave_prueba_local)
#         btn_login = self.browser.find_element_by_id('btn_login')
#         btn_login.click()
#         self.browser.implicitly_wait(2)
#         input = self.browser.find_element_by_id('uso')
#         input.send_keys('Educativo')
#         submit = self.browser.find_element_by_id('btnFiltrar')
#         submit.click()
#         self.browser.implicitly_wait(2)
#         herramientas = self.browser.find_element_by_id('herramientas').find_elements_by_xpath(".//*")
#         self.assertNotEqual(len(herramientas),0,"no hay herramientas cuando deberian haber")
#         h2 = self.browser.find_element(By.XPATH, '//a[text()=" Herramienta En Revision"]')
#         self.assertIsNotNone(h2, "no existe la herramienta que deberia estar")
#
#         input = self.browser.find_element_by_id('uso')
#         input.clear()
#         input.send_keys('pruebaerror')
#         submit = self.browser.find_element_by_id('btnFiltrar')
#         submit.click()
#         self.browser.implicitly_wait(2)
#         herramientas = self.browser.find_element_by_id('herramientas').find_elements_by_xpath(".//*")
#         self.assertEqual(len(herramientas),0,"existen herramientas cuando no deberian haber")
#
#     #Prueba unitaria automatica para PC19
#     def test_filtrar_sistema_operativo(self):
#         #self.browser.get('http://localhost:8000/herramientas')
#         self.browser.get('https://final-conectate-group4.herokuapp.com/herramientas')
#         input_sistema_operativo = self.browser.find_element_by_id('sistema_operativo')
#         input_sistema_operativo.send_keys(sistema_operativo_prueba)
#         btn_filtrar = self.browser.find_element_by_id("btnFiltrar")
#         btn_filtrar.click()
#         titulo= self.browser.find_element_by_css_selector('body > div:nth-child(9) > div.row > div:nth-child(1) > div > div.card-header.text-center > a')
#         self.assertIn('TUTORIAL PYTHON',titulo.text)
#         categoria = self.browser.find_element_by_css_selector('body > div:nth-child(9) > div.row > div:nth-child(1) > div > div.card-body > h6')
#         self.assertIn("documento de word",categoria.text)
#         descripcion=self.browser.find_element_by_css_selector('body > div:nth-child(9) > div.row > div:nth-child(1) > div > div.card-body > p')
#         self.assertIn("lorem ipsum",descripcion.text)
#         self.browser.implicitly_wait(60)
#
#     #prueba unitaria automatica para PC15
#     def test_detalle_herramienta_publica(self):
#         self.browser.get('https://final-conectate-group4.herokuapp.com/herramientas/')
#         span = self.browser.find_element(By.XPATH, '//*[@id="herramienta_26_nombre"]/a')
#         span.click()
#         self.browser.get('https://final-conectate-group4.herokuapp.com/herramientas/detail/26/')
#         h2 = self.browser.find_element(By.XPATH, '/html/body/div/div/div[1]/h1')
#
#         self.assertIn('TUTORIAL PYTHON', h2.text)
#
#         self.browser.implicitly_wait(3)
