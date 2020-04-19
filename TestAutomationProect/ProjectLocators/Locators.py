'''
Created on 19 Apr 2020

@author: Y.Najah
'''
class Locators():
    # Login Page Objects
    username_textbox_id    =   'username'
    password_textbox_id    =   'password'
    login_button_id        =   'login_btn'
    # Home Page Objects
    not_now_button_id       =   '//button[text()="Not now"]'
    settings_tab_link_id    =   '//*[@id="tour-settings"]/span'
    firstmessage_mailbox_link_id    =   '//*[@id="conversation-list-columns"]/section/div[1]/div/div[1]/div/span[2]'
    firstfolder_mailbox_link_id     =   '//*[@id="sidebarLabels"]/div/ul/li[1]/a/span[1]'
    firstlabel_mailbox_link_id      =   '//*[@id="sidebarLabels"]/div/ul/li[2]/a/span[1]'

    
    # Settings Page Objects
    foldersandlabels_tab_link_id    =   '/html/body/div[1]/div[2]/div/div/div[2]/div/main/div[2]/div[11]/ul/li/a/span'
    # Folders and Labels Page Objects
    addfloder_button_link_id        =   '/html/body/div[1]/div[2]/div/div/div[2]/div/main/div/section/div[2]/button[1]'
    addLabel_button_link_id         =   '/html/body/div[1]/div[2]/div/div/div[2]/div/main/div/section/div[2]/button[2]'
    foldername_textbox_id           =   '//*[@id="accountName"]'
    labelname_textbox_id            =   '//*[@id="accountName"]'
    cancel_button_link_id           =   '//button[text()="Cancel"]'
    submit_button_link_id           =   '//button[text()="Submit"]'
