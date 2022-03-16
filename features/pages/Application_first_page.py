from selenium.webdriver.common.by import By
from pages.page_base import PageBase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import os, re, os.path
from time import sleep
import pyautogui as pg

class ApplicationInfoLocator(object):
    APPLICATION_FORM = (By.ID, '1006')
    DRP_APP_TYPE = (By.ID, '1018')
    DRP_CONTRACT_STATUS = (By.ID, '1017')
    DRP_CONDITIONS = (By.ID, '1016')
    DRP_ACCOUNT_TYPE = (By.ID, '1023')
    TXT_PURCHASE_ORDER = (By.ID, '1020')
    DRP_SALES_ENTITY_PARENT = (By.ID, '1000')
    DRP_SALES_ENTITY_CHILD = (By.ID, '1007')
    BTN_OPEN_WIZARD_PARENT = (By.CLASS_NAME, 'ToolbarWindow32')
    BTN_OPEN_WIZARD_CHILD = (By.NAME, 'open wizard')

class ApplicationInfoForm(PageBase):
    
    def fill_application_form_open_wizard(self, app_type, conditions_no, account_type, sales_entity, ctn='00'):
        pg.press(['tab', 'tab'])
        sleep(3)
        self.enter_text_advanced(app_type,ApplicationInfoLocator.APPLICATION_FORM, ApplicationInfoLocator.DRP_APP_TYPE)
        sleep(2)
        pg.press(['tab', 'tab','tab','tab'])
        sleep(3)
        self.enter_text_advanced(conditions_no,ApplicationInfoLocator.APPLICATION_FORM, ApplicationInfoLocator.DRP_CONDITIONS)
        sleep(2)
        pg.press(['tab', 'tab','tab'])
        sleep(3)
        self.enter_text_advanced(sales_entity,ApplicationInfoLocator.DRP_SALES_ENTITY_PARENT, ApplicationInfoLocator.DRP_SALES_ENTITY_CHILD)
        if app_type == 'PM':

            pg.press(['tab', 'tab','tab', 'tab'])
            sleep(3)
            self.enter_text_advanced(account_type,ApplicationInfoLocator.APPLICATION_FORM, ApplicationInfoLocator.DRP_ACCOUNT_TYPE)
            pg.press(['tab', 'tab'])
            sleep(3)
            pg.press('down')
            sleep(3)

        elif app_type == 'C':
            pg.moveTo(31,289)
            pg.click()
            sleep(5)
            pg.write(ctn)
            pg.press('enter')
            sleep(5)

        pg.moveTo(22,91)
        pg.click()
        sleep(5)
        pg.press(['tab', 'enter'])
        sleep(20)
