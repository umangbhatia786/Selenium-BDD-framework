from selenium.webdriver.common.by import By
from pages.page_base import PageBase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import os, re, os.path
from time import sleep
import pyautogui as pg
from datetime import datetime

class RefreshCTNLocator(object):
    REFRESH_CTN_FORM = (By.CLASS_NAME, 'ATL:Eon00205')
    BTN_OK = (By.ID, '1006')
    TXT_REASON = (By.ID, '1018')
    DIALOG_REFRESH_CTN = (By.CLASS_NAME, '#32770')
    DIALOG_BTN_OK = (By.ID, '2')
    CLOSE_BAN = (By.ID, 'Item 11172')
    CLOSE_TOOLBAR = (By.CLASS_NAME, 'ToolbarWindow32')

class RefreshCTNForm(PageBase):

    def set_refresh_ctn(self,reason):
        self.enter_text_advanced(reason, RefreshCTNLocator.REFRESH_CTN_FORM, RefreshCTNLocator.TXT_REASON)
        sleep(2)
        self.click_element_advanced(RefreshCTNLocator.REFRESH_CTN_FORM, RefreshCTNLocator.BTN_OK)
        sleep(2)
        pg.screenshot(r"C:\Users\613144542\Desktop\Refresh_CTN\Refreshed_CTN"+str(datetime.now().strftime('%Y-%m-%d-%H_%M_%S'))+".png")
        sleep(3)
        self.click_element_advanced(RefreshCTNLocator.DIALOG_REFRESH_CTN, RefreshCTNLocator.DIALOG_BTN_OK)
        sleep(7)
        self.click_element_advanced(RefreshCTNLocator.CLOSE_TOOLBAR, RefreshCTNLocator.CLOSE_BAN)
        sleep(8)