'''
Created on 19 Apr 2020

@author: Y.Najah
'''
from Locators import Locators

class FoldersAndLabelsPage():

    def __init__(self, driver):
        self.driver = driver

        self.addfloder_button_link_id   =   Locators.addfloder_button_link_id
        self.addLabel_button_link_id    =   Locators.addLabel_button_link_id
        self.foldername_textbox_id      =   Locators.foldername_textbox_id
        self.labelname_textbox_id       =   Locators.labelname_textbox_id
        self.cancel_button_link_id      =   Locators.cancel_button_link_id
        self.submit_button_link_id      =   Locators.submit_button_link_id

    def create_folder(self, foldername):
        self.driver.find_element_by_xpath(self.addfloder_button_link_id).click()
        self.driver.find_element_by_xpath(self.foldername_textbox_id).clear()
        self.driver.find_element_by_xpath(self.foldername_textbox_id).send_keys(foldername)

    def create_label(self, labelname):
        self.driver.find_element_by_xpath(self.addLabel_button_link_id).click()
        self.driver.find_element_by_xpath(self.labelname_textbox_id).clear()
        self.driver.find_element_by_xpath(self.labelname_textbox_id).send_keys(labelname)

    def click_cancel(self):
        self.driver.find_element_by_xpath(self.cancel_button_link_id).click()

    def click_submit(self):
        self.driver.find_element_by_xpath(self.submit_button_link_id).click()
