# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from selenium import webdriver

usr_miembroGti = "miembro@uniandes.edu.co"
pwd_miembroGti = "miembro123456"

class Test(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.set_window_size(1024, 768)
        self.browser.implicitly_wait(5000)

    def tearDown(self):
        self.browser.quit()

    def test_MarcarListoRevision(self):
        self.browser.get('http://localhost:8080/herramientas')
        #self.browser.get('https://final-conectate-group4.herokuapp.com/herramientas')

        self.browser.implicitly_wait(10000)

        link = self.browser.find_element_by_id('login')
        link.click()
        self.browser.implicitly_wait(3000)
        input_email = self.browser.find_element_by_id('email')
        input_email.send_keys(usr_miembroGti)
        input_pass = self.browser.find_element_by_id('password')
        input_pass.send_keys(pwd_miembroGti)
        btn_login = self.browser.find_element_by_id('btn_login')
        btn_login.click()

        btn_login = self.browser.find_element_by_id('herramienta_4_nombre') #Herramienta en estado de revision
        btn_login.click()

        btn_postulacion = self.browser.find_element_by_id('postular_a_publicacion')
        btn_postulacion.click()

        self.browser.implicitly_wait(3000)

        self.browser.find_element_by_id("postulacion_enviada")

