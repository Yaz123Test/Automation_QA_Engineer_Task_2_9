'''
Created on 19 Apr 2020

@author: Y.Najah
'''
from Locators import Locators
from selenium.webdriver.common import action_chains

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.not_now_button_id              =   Locators.not_now_button_id
        self.settings_tab_link_id           =   Locators.settings_tab_link_id
        self.firstmessage_mailbox_link_id   =   Locators.firstmessage_mailbox_link_id
        self.firstfolder_mailbox_link_id    =   Locators.firstfolder_mailbox_link_id
        self.firstlabel_mailbox_link_id     =   Locators.firstlabel_mailbox_link_id

    def click_not_now(self):
        self.driver.find_element_by_xpath(self.not_now_button_id).click()

    def click_settings_tab(self):
        self.driver.find_element_by_xpath(self.settings_tab_link_id).click()

    def move_message_to_folder(self, actionchain):
        source      =   self.driver.find_element_by_xpath(self.firstmessage_mailbox_link_id)
        destination =   self.driver.find_element_by_xpath(self.firstfolder_mailbox_link_id)
        actionchain.drag_and_drop(source, destination).perform()

    def add_label_to_message(self, actionchain):
        source      =   self.driver.find_element_by_xpath(self.firstmessage_mailbox_link_id)
        destination =   self.driver.find_element_by_xpath(self.firstlabel_mailbox_link_id)
        actionchain.drag_and_drop(source, destination).perform()