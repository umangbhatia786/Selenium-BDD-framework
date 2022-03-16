from selenium.webdriver.common.by import By
from pages.page_base import PageBase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import os, re, os.path
from time import sleep
import pyautogui as pg

class changeCCLocator(object):
    change_CC_FORM = (By.CLASS_NAME, 'ATL:Eon00205')
    TXT_Class = (By.ID, '1031')
    BTN_OK = (By.ID, '1028')
    
class changeCCForm(PageBase):

    def set_change_CC(self):
        pg.moveTo(559,432)
        pg.click()
        pg.press('up')
        sleep(3)
        pg.moveTo(699,454)
        pg.click()
        sleep(3) 
        pg.moveTo(729,454)
        pg.click()      
        sleep(3) 
        pg.moveTo(729,454)
        pg.click()  
        sleep(3) 
        self.click_element_advanced(changeCCLocator.change_CC_FORM, changeCCLocator.BTN_OK)
        sleep(4)