from selenium.webdriver.common.by import By
from pages.page_base import PageBase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import os, re, os.path
from time import sleep
import pyautogui as pg

class BilledUnbilledLocator(object):
    Billed_FORM = (By.CLASS_NAME, 'ATL:Eon00205')
    BTN_OK = (By.ID, '1001')
    BTN_OK_date = (By.ID, '1002')
    BTN_OK1_date = (By.ID, '1004')

    
class BilledUnbilledForm(PageBase):

    def set_Billed_Unbilled(self):
        self.click_element_advanced(BilledUnbilledLocator.Billed_FORM, BilledUnbilledLocator.BTN_OK)
        sleep(5)
      
class BillingDateForm(PageBase):

    def set_Billing_date(self):
        pg.moveTo(634,429)
        pg.click()
        sleep(2)
        self.click_element_advanced(BilledUnbilledLocator.Billed_FORM, BilledUnbilledLocator.BTN_OK_date)
        sleep(3)   
        self.click_element_advanced(BilledUnbilledLocator.Billed_FORM, BilledUnbilledLocator.BTN_OK1_date)   
        sleep(5)