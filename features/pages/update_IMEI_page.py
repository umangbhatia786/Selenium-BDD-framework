from selenium.webdriver.common.by import By
from pages.page_base import PageBase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import os, re, os.path
from time import sleep
import pyautogui as pg

class UpdateIMEILocator(object):
    Update_IMEI_FORM = (By.CLASS_NAME, 'ATL:Eon00205')
    TXT_REASON = (By.ID, '1001')
    BTN_OK1 = (By.ID, '1006')
    Equipment_FORM = (By.CLASS_NAME, 'ATL:Eon00205')
    TXT_IMEI = (By.ID, '1009')
    BTN_OK = (By.ID, '1001')
    Confirm_IMEI_FORM = (By.CLASS_NAME, '#32770')
    BTN_OK2 = (By.ID, '1')
    MEMO_FORM = (By.CLASS_NAME, 'ATL:Eon00205')
    BTN_MEMO = (By.ID, '1004')
 
class UpdateIMEIForm(PageBase):

    def set_Update_IMEI(self, reason, IMEI):
        self.click_element_advanced(UpdateIMEILocator.Update_IMEI_FORM, UpdateIMEILocator.TXT_REASON)
        sleep(3)
        self.enter_text_advanced(reason, UpdateIMEILocator.Update_IMEI_FORM, UpdateIMEILocator.TXT_REASON)
        sleep(3)
        self.click_element_advanced(UpdateIMEILocator.Update_IMEI_FORM, UpdateIMEILocator.BTN_OK1)
        sleep(7)
        pg.write(IMEI)
        pg.write(IMEI)
        pg.write(IMEI)
        pg.write(IMEI)
        pg.write(IMEI)
        pg.write(IMEI)
        pg.write(IMEI)
        pg.write(IMEI)
        pg.write(IMEI)
        pg.write(IMEI)
        pg.write(IMEI)
        pg.write(IMEI)
        pg.write(IMEI)
        pg.write(IMEI)
        pg.write(IMEI)
        pg.write(IMEI)
        sleep(3)
        self.click_element_advanced(UpdateIMEILocator.Equipment_FORM, UpdateIMEILocator.BTN_OK)
        sleep(5)
        self.click_element_advanced(UpdateIMEILocator.Confirm_IMEI_FORM, UpdateIMEILocator.BTN_OK2)
        sleep(6)
        self.click_element_advanced(UpdateIMEILocator.MEMO_FORM, UpdateIMEILocator.BTN_MEMO)