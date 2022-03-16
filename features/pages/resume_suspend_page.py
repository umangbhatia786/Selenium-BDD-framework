from selenium.webdriver.common.by import By
from pages.page_base import PageBase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from time import sleep

class ResumeSuspendFormLocator(object):
    RESTORE_SUSPEND_CTN_FORM = (By.CLASS_NAME, 'ATL:Eon00205')
    MEMO_TXT = (By.ID, '396739844')
    BTN_OK = (By.ID, '1006')
    TXT_REASON = (By.ID, '1004')
    DIALOG_RESTORE_SUSPEND_CTN = (By.NAME, 'Restore CTN   (#10020)')
    DIALG_BTN_OK = (By.ID, '1')

class ResumeSuspendForm:
    
    def resume_suspend_ctn(self):
        self.enter_text_advanced('AGMT', ResumeSuspendFormLocator.RESTORE_SUSPEND_CTN_FORM, ResumeSuspendFormLocator.TXT_REASON)
        sleep(2)
        self.click_element_advanced(ResumeSuspendFormLocator.RESTORE_SUSPEND_CTN_FORM, ResumeSuspendFormLocator.BTN_OK)
        sleep(5)
        self.click_element_advanced(ResumeSuspendFormLocator.DIALOG_RESTORE_SUSPEND_CTN, ResumeSuspendFormLocator.DIALG_BTN_OK)