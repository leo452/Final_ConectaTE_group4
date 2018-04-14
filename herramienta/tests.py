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
        herramientas = models.Herramienta.objects.all()
        if herramientas:
            response = self.client.delete(reverse('herramienta-delete', id=[herramientas[0].id]))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response['content-type'], 'application/json')


usuario_prueba = "tj.marrugo@uniandes.edu.co"
clave_prueba = "admin1234"


class AtoTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(getRealPath('../extra/chromedriver'))
        self.browser.set_window_size(1024, 786)
        self.browser.implicitly_wait(2)


    def tearDown(self):
        self.browser.quit()


    def test_EliminarHerramienta(self):
        herramientas = models.Herramienta.objects.all()
        self.browser.get(reverse('home'))
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
        l4 = self.browser.find_element_by_id('del_' + herramientas[0].id)
        l4.click()
        self.browser.implicitly_wait(3)
        alert = self.driver.browser.switch_to_alert()
        alert.accept()
        self.browser.implicitly_wait(3)
        success = self.browser.find_element_by_id("id_success")
        self.assertIsNotNone(success)
