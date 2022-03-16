from selenium.webdriver.common.by import By
from pages.page_base import PageBase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import os, re, os.path
from time import sleep

class ResumeCancelLocator(object):
    RESUME_CANCEL_CTN_FORM = (By.CLASS_NAME, 'ATL:Eon00205')
    TXT_REASON = (By.ID, '1001')
    BTN_OK = (By.ID, '1006')


class ResumeCancel(PageBase):

    def set_cancellation_reason(self, reason):
        self.enter_text_advanced(reason, ResumeCancelLocator.RESUME_CANCEL_CTN_FORM, ResumeCancelLocator.TXT_REASON)
        sleep(3)
        self.click_element_advanced(ResumeCancelLocator.RESUME_CANCEL_CTN_FORM, ResumeCancelLocator.BTN_OK)
        sleep(7)
