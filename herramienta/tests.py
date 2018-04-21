# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import models
import views
from django.urls import resolve, reverse
from django.http import HttpRequest
import os

from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common import alert


def getRealPath(rel_path):
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    abs_file_path = os.path.join(script_dir, rel_path)
    return os.path.realpath(abs_file_path)

class Test(TestCase):

#test para validar el funcionamiento del servicio para eliminar herramientas
    def test_HerramintaDelete(self):
        herramienta = models.Herramienta.objects.create(nombre='Herramienta test', descripcion='')
        if herramienta:
            url = reverse('herramienta-delete', args=[herramienta.id])
            response = self.client.delete(url)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response['content-type'], 'application/json')

#test para el metodo de filtrar herramientas por sistema opeativo en la home. PC19
    def test_filtrar_herramienta_metodo(self):
        lista_herramientas = models.Herramienta.objects.filter(sistema_operativo__icontains='windows')
        if lista_herramientas:
            url = reverse('home')
            response = self.client.delete(url)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response['content-type'], 'application/json')

usuario_prueba = "admin@uniandes.edu.co"
clave_prueba = "admin123456"
sistema_operativo_prueba="windows"# valor para prueba selenium PC19

class AtoTest(TestCase):
    # test automatico para validar el funcionamiento del servicio para eliminar herramientas
    def setUp(self):
        self.browser = webdriver.Chrome(getRealPath('../extra/chromedriver'))
        self.browser.set_window_size(1024, 786)
        self.browser.implicitly_wait(2)


    def tearDown(self):
        self.browser.quit()


    def test_EliminarHerramienta(self):
        #self.browser.get('http://localhost:8000/herramientas')
        self.browser.get('https://final-conectate-group4.herokuapp.com/herramientas')
        link = self.browser.find_element_by_id('login')
        link.click()
        self.browser.implicitly_wait(3)
        input_email = self.browser.find_element_by_id('email')
        input_email.send_keys(usuario_prueba)
        input_pass = self.browser.find_element_by_id('password')
        input_pass.send_keys(clave_prueba)
        btn_login = self.browser.find_element_by_id('btn_login')
        btn_login.click()
        self.browser.implicitly_wait(3)
        l2 = self.browser.find_element_by_id('menuHerramientas')
        l2.click()
        self.browser.implicitly_wait(3)
        l3 = self.browser.find_element_by_id('itemListaHerrramienta')
        l3.click()
        self.browser.implicitly_wait(3)
        l4 = self.browser.find_element_by_id('del_2')
        l4.click()
        self.browser.implicitly_wait(3)
        alert = self.driver.browser.switch_to_alert()
        alert.accept()
        self.browser.implicitly_wait(3)
        success = self.browser.find_element_by_id("id_success")
        self.assertIsNotNone(success)

    #Prueba unitaria automatica para PC19
    def test_filtrar_sistema_operativo(self):
        #self.browser.get('http://localhost:8000/herramientas')
        self.browser.get('https://final-conectate-group4.herokuapp.com/herramientas')
        input_sistema_operativo = self.browser.find_element_by_id('sistema_operativo')
        input_sistema_operativo.send_keys(sistema_operativo_prueba)
        btn_filtrar = self.browser.find_element_by_id("btnFiltrar")
        btn_filtrar.click()
        titulo= self.browser.find_element_by_css_selector('body > div:nth-child(9) > div.row > div:nth-child(1) > div > div.card-header.text-center > a')
        self.assertIn('TUTORIAL PYTHON',titulo.text)
        categoria = self.browser.find_element_by_css_selector('body > div:nth-child(9) > div.row > div:nth-child(1) > div > div.card-body > h6')
        self.assertIn("documento de word",categoria.text)
        descripcion=self.browser.find_element_by_css_selector('body > div:nth-child(9) > div.row > div:nth-child(1) > div > div.card-body > p')
        self.assertIn("lorem ipsum",descripcion.text)
        self.browser.implicitly_wait(60)
