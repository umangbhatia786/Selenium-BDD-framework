from selenium.webdriver.common.by import By
from pages.page_base import PageBase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import os, re, os.path
from time import sleep
import pyautogui as pg

class AddATPLocator(object):
    COMPASS_FORM = (By.CLASS_NAME, '#32770')
    BTN_NO = (By.ID, '7')
    ADD_ATP_FORM = (By.CLASS_NAME, 'ATL:Eon00205')
    BTN_OK = (By.ID, '1004')
    SELECTED_ATP_FORM = (By.CLASS_NAME, 'ATL:Eon00205')
    BTN_CONFIRM = (By.ID, '1002')

class AddATPForm(PageBase):

    def add_atp(self):
        self.click_element_advanced(AddATPLocator.COMPASS_FORM, AddATPLocator.BTN_NO)
        sleep(4)
        pg.moveTo(96,134)
        pg.click()
        sleep(4)
        self.click_element_advanced(AddATPLocator.ADD_ATP_FORM, AddATPLocator.BTN_OK)
        sleep(5)
        self.click_element_advanced(AddATPLocator.SELECTED_ATP_FORM, AddATPLocator.BTN_CONFIRM)