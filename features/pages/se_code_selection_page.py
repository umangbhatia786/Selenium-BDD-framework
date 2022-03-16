from selenium.webdriver.common.by import By
from pages.page_base import PageBase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import os, re, os.path
from time import sleep

class SECodeLocator(object):
    SE_CODE_FORM = (By.CLASS_NAME, 'ATL:Eon00205')
    TXT_SALES_ENTITY = (By.ID, '1008')
    BTN_OK = (By.ID, '1014')


class SECodeForm(PageBase):

    def set_sales_entity(self, sales_entity):
        self.clear_text_advanced(sales_entity, SECodeLocator.SE_CODE_FORM, SECodeLocator.TXT_SALES_ENTITY)
        sleep(2)
        self.enter_text_advanced(sales_entity, SECodeLocator.SE_CODE_FORM, SECodeLocator.TXT_SALES_ENTITY)
        sleep(3)
        self.click_element_advanced(SECodeLocator.SE_CODE_FORM, SECodeLocator.BTN_OK)

