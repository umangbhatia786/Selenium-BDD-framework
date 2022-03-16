from selenium.webdriver.common.by import By
from pages.page_base import PageBase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import os, re, os.path
from time import sleep

class CancelCTNLocator(object):
    CANCEL_CTN_FORM = (By.CLASS_NAME, 'ATL:Eon00205')
    MEMO_TXT = (By.ID, '307161204')
    DEPOSIT_RETURN_METHOD_PARENT = (By.CLASS_NAME, 'ATL:Eon00007')
    DEPOSIT_RETURN_METHOD_CHILD = (By.ID, '1013')
    BTN_OK = (By.ID, '1006')
    DIALOG_CANCEL_CTN = (By.CLASS_NAME, '#32770')
    DIALOG_BTN_OK = (By.ID, '1')
    TXT_REASON = (By.ID, '1004')

class CancelCTNForm(PageBase):

    def cancel_ctn(self,cancel_reason, drm):
        self.enter_text_advanced(cancel_reason, CancelCTNLocator.CANCEL_CTN_FORM, CancelCTNLocator.TXT_REASON)
        sleep(2)
        self.enter_text_advanced(drm, CancelCTNLocator.DEPOSIT_RETURN_METHOD_PARENT, CancelCTNLocator.DEPOSIT_RETURN_METHOD_CHILD)
        sleep(2)
        self.click_element_advanced(CancelCTNLocator.CANCEL_CTN_FORM, CancelCTNLocator.BTN_OK)
        sleep(5)
        self.click_element_advanced(CancelCTNLocator.DIALOG_CANCEL_CTN, CancelCTNLocator.DIALOG_BTN_OK)