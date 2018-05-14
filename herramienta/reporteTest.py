from __future__ import unicode_literals
import models
from django.urls import resolve, reverse
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

from django.test import TestCase
from selenium import webdriver


usuario_pruebaAdmin = "usr.admin@uniandes.edu.co"
usuario_pruebaAdmin_clave = "admin123456"
usuario_pruebaGTI = "usr.gti@uniandes.edu.co"
usuario_pruebaGTI_clave = "admin123456"

class ReporteTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.set_window_size(1024, 786)
        self.browser.implicitly_wait(2)


    def tearDown(self):
        self.browser.quit()

    def test_MenuReporte(self):
        #self.browser.get('https://final-conectate-group4.herokuapp.com/herramientas')
        self.browser.get('http://localhost:8000/herramientas')
        link = self.browser.find_element_by_id('login')
        link.click()
        self.browser.implicitly_wait(10)
        input_email = self.browser.find_element_by_id('email')
        input_email.send_keys(usuario_pruebaAdmin)
        input_pass = self.browser.find_element_by_id('password')
        input_pass.send_keys(usuario_pruebaAdmin_clave)
        btn_login = self.browser.find_element_by_id('btn_login')
        btn_login.click()
        self.browser.implicitly_wait(10)
        l2 = self.browser.find_element_by_id('menuHerramientas')
        l2.click()
        self.browser.implicitly_wait(10)
        success = self.browser.find_element_by_id("reporteHerramientas")
        self.assertIsNotNone(success)

    def test_PaginaReporte(self):
        #self.browser.get('https://final-conectate-group4.herokuapp.com/herramientas')
        self.browser.get('http://localhost:8000/herramientas')
        link = self.browser.find_element_by_id('login')
        link.click()
        self.browser.implicitly_wait(10)
        input_email = self.browser.find_element_by_id('email')
        input_email.send_keys(usuario_pruebaAdmin)
        input_pass = self.browser.find_element_by_id('password')
        input_pass.send_keys(usuario_pruebaAdmin_clave)
        btn_login = self.browser.find_element_by_id('btn_login')
        btn_login.click()
        self.browser.implicitly_wait(10)
        l2 = self.browser.find_element_by_id('menuHerramientas')
        l2.click()
        self.browser.implicitly_wait(10)
        l3 = self.browser.find_element_by_id("reporteHerramientas")
        l3.click()
        self.browser.implicitly_wait(10)
        l4 = self.browser.find_elements(By.XPATH, '//h1[text()="Reporte de Herramientas"]')
        self.assertEqual(l4.text, 'Reporte de Herramientas')

    def test_PaginaReporteTabla(self):
        # self.browser.get('https://final-conectate-group4.herokuapp.com/herramientas')
        self.browser.get('http://localhost:8000/herramientas')
        link = self.browser.find_element_by_id('login')
        link.click()
        self.browser.implicitly_wait(10)
        input_email = self.browser.find_element_by_id('email')
        input_email.send_keys(usuario_pruebaAdmin)
        input_pass = self.browser.find_element_by_id('password')
        input_pass.send_keys(usuario_pruebaAdmin_clave)
        btn_login = self.browser.find_element_by_id('btn_login')
        btn_login.click()
        self.browser.implicitly_wait(10)
        l2 = self.browser.find_element_by_id('menuHerramientas')
        l2.click()
        self.browser.implicitly_wait(10)
        l3 = self.browser.find_element_by_id("reporteHerramientas")
        l3.click()
        self.browser.implicitly_wait(10)
        l4 = self.browser.find_element_by_id('reporteHerramienta')
        self.assertIsNotNone(l4)
