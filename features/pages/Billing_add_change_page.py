from selenium.webdriver.common.by import By
from pages.page_base import PageBase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import os, re, os.path
from time import sleep
import pyautogui as pg

class billingLocator(object):
    ADDRESS_FORM = (By.CLASS_NAME, 'Internet Explorer_Server')
    TXT_POSTAL_CODE = (By.NAME, 'Postal code')
    TXT_FIND_ADDRESS = (By.NAME, 'FIND ADDRESS')
   
    BTN_SUBMIT = (By.NAME, 'SUBMIT')
    BTN_CHANGE = (By.NAME, 'CONFIRM CHANGE')
    

class billingForm(PageBase):

    def change_billing_address(self,bill_address):

        pg.moveTo(1349,126)
        pg.click()
        pg.click()
        sleep(2)
        pg.moveTo(485,339)
        pg.click()
        sleep(2)
        pg.moveTo(1350,657)
        pg.click()
        pg.click()
        self.enter_text_advanced(bill_address, billingLocator.ADDRESS_FORM, billingLocator.TXT_POSTAL_CODE) 
        sleep(5)
        pg.press('down''down')
        sleep(5)
        self.click_element_advanced(billingLocator.ADDRESS_FORM, billingLocator.TXT_FIND_ADDRESS)
        sleep(5)
        pg.moveTo(1350,659)
        pg.click()
        pg.click()
        sleep(2)
        pg.moveTo(162,475)
        pg.click()
        sleep(2)
        pg.moveTo(238,596)
        pg.click()
        pg.press('down')
        sleep(2)
        self.click_element_advanced(billingLocator.ADDRESS_FORM, billingLocator.BTN_SUBMIT)
        sleep(4)
        pg.press('down')
        self.click_element_advanced(billingLocator.ADDRESS_FORM, billingLocator.BTN_CHANGE)
        sleep(4)
        
