from selenium.webdriver.common.by import By
from pages.page_base import PageBase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import os, re, os.path
from time import sleep
import pyautogui as pg
from datetime import datetime
dirpath = os.getcwd()

class CSMPageLocator(object):
    # CSM Page Locators
    CSM_APPLICATION = (By.CLASS_NAME, "ATL:Eon00202")
    BAN_BUTTON = (By.NAME, "BAN")
    DIALOG_WINDOW_1 = (By.NAME, 'SoftPhone Warning   (#7710183)')
    YES_BTN_1 = (By.ID, '6')
    #CTN_TXT_BOX_PARENT = (By.CLASS_NAME, 'ATL:Eon00205')
    CTN_TXT_BOX_CHILD = (By.ID, '1041')
    SELECT_BAN_WINDOW = (By.CLASS_NAME, 'ATL:Eon00205')
    GET_BTN = (By.ID, '1008')
    MENU_BAR = (By.ID, 'MenuBar')
    DRP_CTN_OPTIONS = (By.ID, 'Item 7')
    DRP_ACTIONS = (By.ID, 'Item 5')
    SUSPEND_CTN_PARENT = (By.CLASS_NAME, '#32768')
    SUSPEND_CTN_CHILD = (By.ID, 'Item 10991')
    RESUME_SUSPEND_PARENT = (By.CLASS_NAME, '#32768')
    RESUME_SUSPEND_CHILD = (By.ID, 'Item 10992')
    CANCEL_CTN_CHLD = (By.ID, 'Item 11675')
    RESUME_CANCEL_CTN = (By.ID, 'Item 12460')
    REFRESH_CTN = (By.ID, 'Item 12469')
    NETWORK_ACTIVITIES_PARENT = (By.CLASS_NAME, '#32768')
    NETWORK_ACTIVITIES_CHILD = (By.ID, 'Item 5')
    FULL_REFRESH_PARENT = (By.CLASS_NAME, '#32768')
    FULL_REFRESH_CHILD = (By.NAME, 'Full_refresh')
    Update_IMEI_PARENT = (By.CLASS_NAME, '#32768')
    Update_IMEI_CHILD = (By.NAME, 'Update IMEI')
    CREDIT_ACTIVITIES_PARENT = (By.CLASS_NAME, '#32768')
    CREDIT_ACTIVITIES_CHILD = (By.ID, 'Item 21')
    CHANGE_CC_PARENT = (By.CLASS_NAME, '#32768')
    CHANGE_CC_CHILD = (By.NAME, 'Change Credit')
    VIEW_PROFILE = (By.NAME, 'View Profile')
    CSM_WNDW = (By.CLASS_NAME, 'Internet Explorer_Server')
    CHANGE_ADD = (By.NAME, 'Change Address')
    REGISTER_CARD = (By.ID, 'Item 10891')
    ADD_ATP_PARENT = (By.CLASS_NAME, '#32768')
    ADD_ATP_CHILD = (By.ID, 'Item 11018')
    DRP_BILL_OPTIONS = (By.ID, 'Item 3')
    BILL_PARENT = (By.CLASS_NAME, '#32768')
    BILL_VALIDATION_CHILD = (By.ID, 'Item 10763')
    BILL_NEW_IE_WNDW =  (By.NAME, "I'm on a BT Webtop, sign me in automatically")
    IE_BROWSER = (By.CLASS_NAME, 'Internet Explorer_Server')
    BILLED_CALLS = (By.ID, 'Item 10770')
    REGISTER_CARD_PARENT = (By.CLASS_NAME, '#32768')
    REGISTER_CARDS = (By.ID, 'Item 10888')
    BILL_CYCLE = (By.ID, 'Item 10874')
    NEW_MNP_SERVICES = (By.ID, 'Item 30')
    PORT_IN_PARENT = (By.CLASS_NAME, '#32768')
    PORT_IN = (By.ID, 'Item 10904')
    Send_To_WEB = (By.NAME, "Send To WEB")
    WNDW_SAVE_SUCCEED = (By.CLASS_NAME, "#32770")
    WNDW_OK = (By.NAME, "OK")
    TAB_RAPLACE_SIM = (By.NAME, "Replace SIM")
    PARENT_REPLACE = (By.CLASS_NAME, '#32768')
    PARENT_ACTIVATE = (By.CLASS_NAME, '#32768')
    TAB_ACTIVATE = (By.NAME, "Activate SIM")
    ENTER_IMEI = (By.CLASS_NAME,  "Edit")
    PARENT_IMEI = (By.CLASS_NAME, 'ATL:Eon00205')
    BTN_OK = (By.NAME, "OK")
    WNDW_REPLACE = (By.CLASS_NAME, 'ATL:Eon00205')
    WNDW_SIM_REPLACED = (By.CLASS_NAME, "#32770")


class CSMPage(PageBase):

    # CSM Page Methods

    def open_replace_sim(self,IMEI1):
        sleep(10)
        self.click_element_advanced(CSMPageLocator.MENU_BAR, CSMPageLocator.DRP_CTN_OPTIONS)
        sleep(2)
        self.click_element_advanced(CSMPageLocator.PARENT_REPLACE, CSMPageLocator.TAB_RAPLACE_SIM)
        sleep(2)  
        self.click_element_advanced(CSMPageLocator.PARENT_ACTIVATE, CSMPageLocator.TAB_ACTIVATE)
        sleep(5)
        pg.moveTo(611,333)
        pg.click()
        pg.write("LOST")
        sleep(1)
        self.click_element_advanced(CSMPageLocator.WNDW_REPLACE, CSMPageLocator.BTN_OK)
        sleep(2)
        pg.moveTo(656,289)
        pg.click()
        pg.write(IMEI1)
        sleep(2)
        pg.moveTo(617,526)
        pg.click()
        sleep(2)
        self.click_element_advanced(CSMPageLocator.WNDW_SIM_REPLACED, CSMPageLocator.BTN_OK)
        sleep(3)
        self.click_element_advanced(CSMPageLocator.WNDW_SIM_REPLACED, CSMPageLocator.BTN_OK)
        sleep(2)
        pg.screenshot(r"C:\Users\613144542\Desktop\Replace_sim\replaced_ss"+str(datetime.now().strftime('%Y-%m-%d-%H_%M_%S'))+".png")
        sleep(3)
        self.click_element_advanced(CSMPageLocator.WNDW_SIM_REPLACED, CSMPageLocator.BTN_OK)
        sleep(3)


    def method_click_on_popup(self):
        self.click_element_advanced(CSMPageLocator.DIALOG_WINDOW_1, CSMPageLocator.YES_BTN_1).click()
        sleep(2)
        self.click_element_advanced(CSMPageLocator.DIALOG_WINDOW_1, CSMPageLocator.YES_BTN_1).click()
        sleep(15)

    def method_ban_window(self):
        self.click_element_advanced(CSMPageLocator.CSM_APPLICATION, CSMPageLocator.BAN_BUTTON)
        sleep(8)
    
    def set_ctn(self,my_ctn):
        self.enter_text_advanced(my_ctn,CSMPageLocator.SELECT_BAN_WINDOW, CSMPageLocator.CTN_TXT_BOX_CHILD)
        sleep(1)
        self.click_element_advanced(CSMPageLocator.SELECT_BAN_WINDOW, CSMPageLocator.GET_BTN)
        sleep(25)

    def open_suspend_ban_window(self):
        self.click_element_advanced(CSMPageLocator.MENU_BAR, CSMPageLocator.DRP_CTN_OPTIONS)
        sleep(4)
        self.click_element_advanced(CSMPageLocator.SUSPEND_CTN_PARENT, CSMPageLocator.SUSPEND_CTN_CHILD)

    def open_resume_suspend_ban_window(self):
        self.click_element_advanced(CSMPageLocator.MENU_BAR, CSMPageLocator.DRP_CTN_OPTIONS)
        sleep(4)
        self.click_element_advanced(CSMPageLocator.RESUME_SUSPEND_PARENT, CSMPageLocator.RESUME_SUSPEND_CHILD)

    def open_cancel_ctn_window(self):
        self.click_element_advanced(CSMPageLocator.MENU_BAR, CSMPageLocator.DRP_CTN_OPTIONS)
        sleep(4)
        #self.click_element_advanced(CSMPageLocator.SUSPEND_CTN_PARENT, CSMPageLocator.CANCEL_CTN_CHLD)
        self.enter_text_advanced(Keys.DOWN + Keys.DOWN + Keys.ENTER ,CSMPageLocator.MENU_BAR, CSMPageLocator.DRP_CTN_OPTIONS)

    def open_resume_cancel_window(self):
        self.click_element_advanced(CSMPageLocator.MENU_BAR, CSMPageLocator.DRP_CTN_OPTIONS)
        sleep(4)
        self.enter_text_advanced(Keys.DOWN + Keys.ENTER ,CSMPageLocator.MENU_BAR, CSMPageLocator.DRP_CTN_OPTIONS)

    def open_refresh_ctn_window(self):
        self.click_element_advanced(CSMPageLocator.MENU_BAR, CSMPageLocator.DRP_CTN_OPTIONS)
        sleep(4)
        self.click_element_advanced(CSMPageLocator.NETWORK_ACTIVITIES_PARENT, CSMPageLocator.NETWORK_ACTIVITIES_CHILD)
        sleep(3)
        self.click_element_advanced(CSMPageLocator.FULL_REFRESH_PARENT, CSMPageLocator.FULL_REFRESH_CHILD)
     
    def open_Update_IMEI_window(self):
        self.click_element_advanced(CSMPageLocator.MENU_BAR, CSMPageLocator.DRP_CTN_OPTIONS)
        sleep(4)
        self.click_element_advanced(CSMPageLocator.Update_IMEI_PARENT, CSMPageLocator.Update_IMEI_CHILD)
       
    def open_change_CC_window(self):
        self.click_element_advanced(CSMPageLocator.MENU_BAR, CSMPageLocator.DRP_ACTIONS)
        sleep(4)
        self.click_element_advanced(CSMPageLocator.CREDIT_ACTIVITIES_PARENT, CSMPageLocator.CREDIT_ACTIVITIES_CHILD)
        sleep(3)
        self.click_element_advanced(CSMPageLocator.CHANGE_CC_PARENT, CSMPageLocator.CHANGE_CC_CHILD)
        sleep(3)

    def open_view_profile_address_change(self):
        sleep(5)
        self.click_element_advanced(CSMPageLocator.CSM_WNDW, CSMPageLocator.VIEW_PROFILE)
        sleep(5)
        pg.press('down')
        sleep(5)
        self.click_element_advanced(CSMPageLocator.CSM_WNDW, CSMPageLocator.CHANGE_ADD)
        sleep(5)
        

    def open_add_atp_window(self):
        self.click_element_advanced(CSMPageLocator.MENU_BAR, CSMPageLocator.DRP_CTN_OPTIONS)
        sleep(4)
        self.click_element_advanced(CSMPageLocator.ADD_ATP_PARENT, CSMPageLocator.ADD_ATP_CHILD)
        sleep(5)
    
    def open_billing_validation(self):
        self.click_element_advanced(CSMPageLocator.MENU_BAR, CSMPageLocator.DRP_BILL_OPTIONS)
        sleep(3)
        self.click_element_advanced(CSMPageLocator.BILL_PARENT, CSMPageLocator.BILL_VALIDATION_CHILD)
        sleep(10)
        self.click_element_advanced(CSMPageLocator.IE_BROWSER, CSMPageLocator.BILL_NEW_IE_WNDW)
        sleep(3)
        pg.screenshot(r"C:\Users\613144542\Desktop\Bill_SS\Bill"+str(datetime.now().strftime('%Y-%m-%d-%H_%M_%S'))+".png")
        sleep(8)
    
    
    def open_billed_unbilled_val(self):
        self.click_element_advanced(CSMPageLocator.MENU_BAR, CSMPageLocator.DRP_BILL_OPTIONS)
        sleep(3)
        self.click_element_advanced(CSMPageLocator.BILL_PARENT, CSMPageLocator.BILLED_CALLS)
        sleep(5)

    def open_register_cards(self):
        self.click_element_advanced(CSMPageLocator.MENU_BAR, CSMPageLocator.DRP_ACTIONS)
        sleep(3)
        self.click_element_advanced(CSMPageLocator.REGISTER_CARD_PARENT, CSMPageLocator.REGISTER_CARDS)
        sleep(5)

      
    def open_billing_cycle(self):
        self.click_element_advanced(CSMPageLocator.MENU_BAR, CSMPageLocator.DRP_ACTIONS)
        sleep(2)
        self.click_element_advanced(CSMPageLocator.REGISTER_CARD_PARENT, CSMPageLocator.BILL_CYCLE)
        sleep(2)  

    def open_port_in(self,PAC,PCTN):
        self.click_element_advanced(CSMPageLocator.MENU_BAR, CSMPageLocator.DRP_ACTIONS)
        sleep(3)
        self.click_element_advanced(CSMPageLocator.REGISTER_CARD_PARENT, CSMPageLocator.NEW_MNP_SERVICES)
        sleep(5)  
        self.click_element_advanced(CSMPageLocator.PORT_IN_PARENT, CSMPageLocator.PORT_IN)
        sleep(7)
        pg.moveTo(326,241)
        pg.click()
        sleep(2)
        pg.write(PAC)
        sleep(2)
        pg.write(PCTN)
        sleep(5)
        self.click_element_advanced(CSMPageLocator.SELECT_BAN_WINDOW, CSMPageLocator.Send_To_WEB)
        sleep(8)
        self.click_element_advanced(CSMPageLocator.WNDW_SAVE_SUCCEED, CSMPageLocator.WNDW_OK)
        sleep(5)
    
  