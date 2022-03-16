from selenium import webdriver
from features.browser import Browser
from behave import *
from pages.csm_page import CSMPage
from pages.suspend_ban_page import SuspendForm
from pages.resume_suspend_page import ResumeSuspendForm
from pages.cancel_ctn_page import CancelCTNForm
from pages.resume_cancel_page import ResumeCancel
from pages.se_code_selection_page import SECodeForm
from pages.refresh_page import RefreshCTNForm
from pages.update_IMEI_page import UpdateIMEIForm
from pages.change_CC_page import changeCCForm
from pages.Customer_add_change_page import AddressChangeForm
from pages.Billing_add_change_page import billingForm
from pages.add_ATP_page import AddATPForm
from pages.Billed_unbilled_page import BilledUnbilledForm
from pages.Register_cards_page import RegistercardsForm
from pages.Billed_unbilled_page import BillingDateForm
from pages.Add_soc_features_page import AddSOCform
from pages.Bill_payment_page import Billpaymentform

def before_all(context):
    context.browser = Browser()
    context.csm_page = CSMPage()
    context.suspend_form = SuspendForm()
    context.resume_suspend_form = ResumeSuspendForm()
    context.cancel_ctn_form = CancelCTNForm()
    context.resume_cancel = ResumeCancel()
    context.se_code_form = SECodeForm()
    context.refresh_ctn_form = RefreshCTNForm()
    context.Update_IMEI_form = UpdateIMEIForm()
    context.change_CC_form = changeCCForm()
    context.change_custandbill_add_form = AddressChangeForm()
    context.change_only_bill_form = billingForm()
    context.add_atp = AddATPForm()
    context.Billed_Unbilled = BilledUnbilledForm() 
    context.REGISTER_CARD = RegistercardsForm() 
    context.Billing_Date = BillingDateForm()
    context.add_soc = AddSOCform()
    context.bill_payment = Billpaymentform()

def after_all(context):
    context.browser.closeBrowser()
    print('====== Closing Edge and Winium Driver ======')

# def before_scenario(context, scenario):
#     if 'TC_' in str(scenario):
#         print ('===Before Scenario===' + str(scenario))
#         context.browser = Browser()
#         context.login_page = LoginPage()

# def after_scenario(context, scenario):
#     if 'TC_' in str(scenario):
#         print ('===After Scenario===' + str(scenario))
#         context.browser.close()
