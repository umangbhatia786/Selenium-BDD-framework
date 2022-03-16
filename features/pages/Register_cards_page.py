from selenium.webdriver.common.by import By
from pages.page_base import PageBase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import os, re, os.path
from time import sleep
import pyautogui as pg

class RegistercardsLocator(object):
    REGISTER_FORM = (By.CLASS_NAME, 'ATL:Eon00205')
    Use_different_card = (By.NAME, "Use different card")
    BTN_PROCEED = (By.NAME, "PROCEED")
    BTN_CANCEL = (By.NAME, "CANCEL")
    CLOSE_BAN = (By.ID, 'Item 10683')
    CLOSE_TOOLBAR = (By.CLASS_NAME, 'ReBarWindow32')

class RegistercardsForm(PageBase):

    def set_Register_cards(self):
        self.click_element_advanced(RegistercardsLocator.REGISTER_FORM, RegistercardsLocator.Use_different_card)
        pg.click()
        sleep(5)
        self.click_element_advanced(RegistercardsLocator.REGISTER_FORM, RegistercardsLocator.BTN_PROCEED)
        sleep(10)
        pg.moveTo(654,281)
        pg.click()
        pg.write('VVV')
        pg.press('enter')
        sleep(2)
        pg.moveTo(514,315)
        pg.click()
        pg.write('4929420077965432')
        sleep(3)
        pg.moveTo(514,412)
        pg.click()
        pg.write('01')
        sleep(2)
        pg.moveTo(595,412)
        pg.click()
        pg.write('2022')
        sleep(2)
        pg.moveTo(514,445)
        pg.click()
        pg.write('123')
        sleep(2)
        pg.moveTo(514,489)
        pg.click()
        pg.write('12345')
        sleep(2)
        pg.moveTo(514,568)
        pg.click()
        pg.write('XYZ')
        sleep(2)
        pg.moveTo(949,637)
        pg.click()
        sleep(7)
        pg.moveTo(1005,696)
        pg.click()
        sleep(2)
        self.click_element_advanced(RegistercardsLocator.REGISTER_FORM, RegistercardsLocator.BTN_CANCEL)
        sleep(5)
        self.click_element_advanced(RegistercardsLocator.CLOSE_TOOLBAR, RegistercardsLocator.CLOSE_BAN)
        sleep(8)
