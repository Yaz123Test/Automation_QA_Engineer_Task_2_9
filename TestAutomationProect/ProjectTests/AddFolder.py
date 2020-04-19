'''
Created on 19 Apr 2020

@author: Y.Najah
'''
from selenium import webdriver
import time
import unittest
import HtmlTestRunner
from LoginPage import LoginPage
from HomePage import HomePage
from SettingsPage import SettingsPage
from FoldersAndLabelsPage import FoldersAndLabelsPage

class AddFolder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_add_folder(self):
        # Creating object for test
        driver          =   self.driver
        login           =   LoginPage(driver)
        home            =   HomePage(driver)
        settings        =   SettingsPage(driver)
        foldersandabels =   FoldersAndLabelsPage(driver)

        # Open a Firefox window
        driver.get('https://beta.protonmail.com/')

        # Connect to ProtonMail
        login.enter_username('yaz123test@protonmail.com')
        login.enter_password('qwerty123')
        login.click_login()
        time.sleep(1)

        # Close PopUp Window and Click on Settings Tab
        home.click_not_now()
        home.click_settings_tab()
        time.sleep(1)

        # Click on the Folders and Labels link
        settings.click_foldersandlabels()
        time.sleep(1)

        # Add a Folder and Submit
        foldersandabels.create_folder('MyFolderSubmit1')
        foldersandabels.click_submit()
        time.sleep(1)

        # Add a Folder and Cancel
        foldersandabels.create_folder('MyFolderCancel')
        foldersandabels.click_cancel()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output = "/TestAutomationProject/ProjectTestsReports"))