from selenium.webdriver.common.by import By
from pages.page_base import PageBase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from time import sleep

class SuspendFormLocator(object):
    SUSPEND_CTN_FORM = (By.CLASS_NAME, 'ATL:Eon00205')
    MEMO_TXT = (By.ID, '392663492')
    BTN_OK = (By.ID, '1011')
    TXT_REASON = (By.ID, '1004')
    DIALOG_SUSPEND_CTN = (By.CLASS_NAME, '#32770')
    DIALG_BTN_OK = (By.ID, '1')

class SuspendForm(PageBase):
    
    def suspend_ctn(self):
        self.enter_text_advanced('SDEP', SuspendFormLocator.SUSPEND_CTN_FORM, SuspendFormLocator.TXT_REASON)
        sleep(2)
        '''self.click_element_advanced(SuspendFormLocator.SUSPEND_CTN_FORM, SuspendFormLocator.MEMO_TXT)
        sleep(4)
        self.enter_text_advanced('SAMPLE REASON', SuspendFormLocator.SUSPEND_CTN_FORM, SuspendFormLocator.MEMO_TXT)
        sleep(1)'''
        self.click_element_advanced(SuspendFormLocator.SUSPEND_CTN_FORM, SuspendFormLocator.BTN_OK)
        sleep(5)
        self.click_element_advanced(SuspendFormLocator.DIALOG_SUSPEND_CTN, SuspendFormLocator.DIALG_BTN_OK)
        