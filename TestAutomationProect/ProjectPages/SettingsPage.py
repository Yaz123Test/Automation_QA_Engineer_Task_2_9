'''
Created on 19 Apr 2020

@author: Y.Najah
'''
from Locators import Locators

class SettingsPage():

    def __init__(self, driver):
        self.driver = driver

        self.foldersandlabels_tab_link_id   =   Locators.foldersandlabels_tab_link_id

    def click_foldersandlabels(self):
        self.driver.find_element_by_xpath(self.foldersandlabels_tab_link_id).click()