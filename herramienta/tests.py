# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import models
import views
from django.urls import resolve, reverse
from django.http import HttpRequest
import os

from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common import alert


def getRealPath(rel_path):
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    abs_file_path = os.path.join(script_dir, rel_path)
    return os.path.realpath(abs_file_path)

class Test(TestCase):

    def test_HerramintaDelete(self):
        herramienta = models.Herramienta.objects.create(nombre='Herramienta test', descripcion='')
        if herramienta:
            url = reverse('herramienta-delete', args=[herramienta.id])
            response = self.client.delete(url)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response['content-type'], 'application/json')


usuario_prueba = "admin@uniandes.edu.co"
clave_prueba = "admin123456"


class AtoTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(getRealPath('../extra/chromedriver'))
        self.browser.set_window_size(1024, 786)
        self.browser.implicitly_wait(2)


    def tearDown(self):
        self.browser.quit()


    def test_EliminarHerramienta(self):
        self.browser.get('http://localhost:8000/herramientas')
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
