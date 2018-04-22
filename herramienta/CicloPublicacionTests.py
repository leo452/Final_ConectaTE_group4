# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from selenium import webdriver

usr_miembroGti = "miembro@uniandes.edu.co"
pwd_miembroGti = "miembro123456"

usr_miembroGti2 = "miembro2@uniandes.edu.co"
pwd_miembroGti2 = "miembro123456"

usr_admin = "admin@uniandes.edu.co"
pwd_admin = "admin123456"

class Test(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome("C:\\Users\\Cristian\\Documents\\Python Projects\\chromedriver.exe")
        self.browser.set_window_size(1024, 768)
        self.browser.implicitly_wait(5000)

    def tearDown(self):
        self.browser.quit()

    def test_comenzarEdicion(self):
        self.browser.get('http://localhost:8080/herramientas')
        #self.browser.get('https://final-conectate-group4.herokuapp.com/herramientas')

        self.browser.implicitly_wait(10000)

        link = self.browser.find_element_by_id('login')
        link.click()
        self.browser.implicitly_wait(3000)
        input_email = self.browser.find_element_by_id('email')
        input_email.send_keys(usr_miembroGti2)
        input_pass = self.browser.find_element_by_id('password')
        input_pass.send_keys(pwd_miembroGti2)
        btn_login = self.browser.find_element_by_id('btn_login')
        btn_login.click()

        btn_tool = self.browser.find_element_by_id('herramienta_4_nombre') #Herramienta en estado de revision propia
        btn_tool.click()

        btn_edicion = self.browser.find_element_by_id('comenzar_edicion')
        btn_edicion.click()

    def test_solicitarRevision(self):
        self.browser.get('http://localhost:8080/herramientas')
        #self.browser.get('https://final-conectate-group4.herokuapp.com/herramientas')

        self.browser.get('http://localhost:8080/herramientas')
        #self.browser.get('https://final-conectate-group4.herokuapp.com/herramientas')

        self.browser.implicitly_wait(10000)

        link = self.browser.find_element_by_id('login')
        link.click()
        self.browser.implicitly_wait(3000)
        input_email = self.browser.find_element_by_id('email')
        input_email.send_keys(usr_miembroGti2)
        input_pass = self.browser.find_element_by_id('password')
        input_pass.send_keys(pwd_miembroGti2)
        btn_login = self.browser.find_element_by_id('btn_login')
        btn_login.click()

        btn_tool = self.browser.find_element_by_id('herramienta_10_nombre') #Herramienta en estado de revision propia
        btn_tool.click()

        btn_revision = self.browser.find_element_by_id('solicitar_revision_pares')
        btn_revision.click()

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

        btn_tool = self.browser.find_element_by_id('herramienta_4_nombre') #Herramienta en estado de revision
        btn_tool.click()

        btn_postulacion = self.browser.find_element_by_id('postular_a_publicacion')
        btn_postulacion.click()

        self.browser.implicitly_wait(3000)

        self.browser.find_element_by_id("postulacion_enviada")

    def test_adminAccessBorrador(self):
        self.browser.get('http://localhost:8080/herramientas')
        # self.browser.get('https://final-conectate-group4.herokuapp.com/herramientas')

        self.browser.implicitly_wait(10000)

        link = self.browser.find_element_by_id('login')
        link.click()
        self.browser.implicitly_wait(3000)
        input_email = self.browser.find_element_by_id('email')
        input_email.send_keys(usr_admin)
        input_pass = self.browser.find_element_by_id('password')
        input_pass.send_keys(pwd_admin)
        btn_login = self.browser.find_element_by_id('btn_login')
        btn_login.click()

        btn_tool = self.browser.find_element_by_id('herramienta_7_nombre')  # Herramienta en estado de revision
        btn_tool.click()

    def test_publicar_herramienta (self):
        self.browser.get('http://localhost:8080/herramientas')
        # self.browser.get('https://final-conectate-group4.herokuapp.com/herramientas')

        self.browser.implicitly_wait(10000)

        link = self.browser.find_element_by_id('login')
        link.click()
        self.browser.implicitly_wait(3000)
        input_email = self.browser.find_element_by_id('email')
        input_email.send_keys(usr_admin)
        input_pass = self.browser.find_element_by_id('password')
        input_pass.send_keys(pwd_admin)
        btn_login = self.browser.find_element_by_id('btn_login')
        btn_login.click()

        btn_desplegable = self.browser.find_element_by_id('menuHerramientas')
        btn_desplegable.click()

        btn_lista_por_publicacion = self.browser.find_element_by_id('listaPorPublicacion')
        btn_lista_por_publicacion.click()

        btn_aceptar = self.browser.find_element_by_id('aceptarHerramienta-1')
        btn_aceptar.click()

        btn_rechazar = self.browser.find_element_by_id('rechazarHerramienta-1')
        btn_rechazar.click()
