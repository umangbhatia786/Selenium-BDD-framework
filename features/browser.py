from selenium import webdriver
import os
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


dirpath = os.getcwd()

winium_driver_path_used = dirpath + r'/features/resources/drivers/Winium.Desktop.Driver.exe'
edge_driver_path_used = dirpath + r'/features/resources/drivers/msedgedriver.exe'
FirstPopupExePath = dirpath + r'/features/resources/AutoIT_Scripts/FirstPopUp.exe'
SecondPopupExePath = dirpath + r'/features/resources/AutoIT_Scripts/SecondPopUp.exe'
ie_exedriver_path = dirpath + r'/features/resources/drivers/IEDriverServer.exe'
WiniumDriverPopupExePath = dirpath + r'/features/resources/AutoIT_Scripts/minimize_win.exe'

class Browser(object):
    # def __init__(self):
    #     self.edge_driver = None
    #     self.driver = None

    # def login_web_application(self):
    '''Method To Setup Edge Browser and Login into CSM'''
    # cap = DesiredCapabilities.INTERNETEXPLORER.copy()
    # cap['INTRODUCE_FLAKINESS_BY_IGNORING_SECURITY_DOMAINS'] = True
    # cap['ignoreProtectedModeSettings'] = True
    #edge_driver = webdriver.Edge(executable_path=edge_driver_path_used)
    edge_driver = webdriver.Ie(executable_path=ie_exedriver_path)

    edge_driver.implicitly_wait(30)
    edge_driver.set_page_load_timeout(30)
    edge_driver.maximize_window()
    print('====== Opening Edge browser ======')
    edge_driver.get('https://exintweb1.eezone.bt.com/webint1/CSM2150_1?RELEASE=BF12150_1')
    sleep(10)
    '''edge_driver.find_element(By.ID, 'username').clear()
    sleep(1)
    edge_driver.find_element(By.ID, 'username').send_keys('612918953')
    edge_driver.find_element(By.ID, 'password').clear()
    sleep(1)
    edge_driver.find_element(By.ID, 'password').send_keys('Iforindia@123')'''
    edge_driver.find_element(By.XPATH, '//*[@id="login"]/button').click()
    sleep(30)
    os.startfile(FirstPopupExePath)
    sleep(5)
    os.startfile(SecondPopupExePath)
    sleep(10)
    # def setup_winium_driver(self):
    os.startfile(winium_driver_path_used)
    driver = webdriver.Remote(
    command_executor='http://localhost:9999',
    desired_capabilities={
            "debugConnectToRunningApp": 'false',
            "app": r"C:\Users\613144542\AppData\Local\Appeon Multi-browser Plug-in\AppeonMultiBrowserLauncher.exe"
        })
    sleep(6)
    os.startfile(WiniumDriverPopupExePath)  
    sleep(6)
    #driver.implicitly_wait(15) 
       
    def closeBrowser(context):
        context.edge_driver.close()
        context.edge_driver.quit() 
        os.system("TASKKILL /F /IM Winium.Desktop.Driver.exe")
