'''
Created on 19 Apr 2020

@author: Y.Najah
'''
from selenium import webdriver
import time
import unittest
from LoginPage import LoginPage
from HomePage import HomePage
from selenium.webdriver.common.action_chains import ActionChains

class MessageToFolder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_move_message_to_folder(self):
        # Creating object for test
        driver          =   self.driver
        login           =   LoginPage(driver)
        home            =   HomePage(driver)
        actionchain     =   ActionChains(driver)

        # Open a Firefox window
        driver.get('https://beta.protonmail.com/')

        # Connect to ProtonMail
        login.enter_username('yaz123test@protonmail.com')
        login.enter_password('qwerty123')
        login.click_login()
        time.sleep(1)

        # Close PopUp Window
        home.click_not_now()
        time.sleep(1)

        # Move the first Message into the First Folder
        home.move_message_to_folder(actionchain)
        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
