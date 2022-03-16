from selenium.webdriver.common.by import By
from pages.page_base import PageBase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import os, re, os.path
from time import sleep
import pyautogui as pg
import keyboard 



class AddSOCLocator(object):
    Cust_services_FORM = (By.NAME, 'BT')
    BTN_Modify_services = (By.NAME, 'Modify Services')
    BTN_Maximum = (By.NAME, 'Maximum 30 characters allowed')
    BTN_ADD = (By.NAME, 'ADD')
    BTN_FEATURES = (By.NAME, 'FEATURES')

class AddSOCform(PageBase):

    def add_soc(self,SOC):
        self.click_element_advanced(AddSOCLocator.Cust_services_FORM, AddSOCLocator.BTN_Modify_services)
        sleep(10)
        pg.moveTo(1352,660)
        pg.click()
        pg.click()
        pg.click()
        pg.click()
        pg.click()
        pg.click()
        pg.click()
        sleep(5)
        self.click_element_advanced(AddSOCLocator.Cust_services_FORM, AddSOCLocator.BTN_Maximum)
        sleep(5)
        self.enter_text_advanced(SOC, AddSOCLocator.Cust_services_FORM, AddSOCLocator.BTN_Maximum)
        keyboard.press_and_release('enter')
        sleep(10)
        pg.click()
        self.click_element_advanced(AddSOCLocator.Cust_services_FORM, AddSOCLocator.BTN_ADD)
        sleep(5)

    def add_feature(self,Feature):
        self.click_element_advanced(AddSOCLocator.Cust_services_FORM, AddSOCLocator.BTN_Modify_services)
        sleep(10)
        pg.moveTo(1351,128)
        pg.click()
        pg.click()
        sleep(5)
        self.click_element_advanced(AddSOCLocator.Cust_services_FORM, AddSOCLocator.BTN_FEATURES)
        pg.moveTo(1352,660)
        pg.click()
        pg.click()
        pg.click()
        pg.click()
        pg.click()
        pg.click()
        pg.click()
        pg.click()
        pg.click()
        pg.click()
        pg.click()
        pg.click()
        sleep(8)
        self.click_element_advanced(AddSOCLocator.Cust_services_FORM, AddSOCLocator.BTN_Maximum)
        sleep(5)
        self.enter_text_advanced(Feature, AddSOCLocator.Cust_services_FORM, AddSOCLocator.BTN_Maximum)
        keyboard.press_and_release('enter')
        sleep(10)
        self.click_element_advanced(AddSOCLocator.Cust_services_FORM, AddSOCLocator.BTN_ADD)
        sleep(5)
