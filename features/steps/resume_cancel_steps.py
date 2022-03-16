from selenium.webdriver.common.by import By
from behave import *
from selenium import webdriver
import time
from nose.tools import assert_equal, assert_true
from pages.page_base import PageBase
from pages.test_base import TestBase

test_base = TestBase()

@then(u'We open Resume_Cancel_CTN Window and Resume_Cancel with Reason as {reason}')
def step_impl(context, reason):
    context.csm_page.open_resume_cancel_window()
    time.sleep(15)
    context.resume_cancel.set_cancellation_reason(reason)

@then(u'We give Sales Entity as {SE}')
def step_impl(context, SE):
    context.se_code_form.set_sales_entity(SE)

