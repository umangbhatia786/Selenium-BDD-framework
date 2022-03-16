from selenium.webdriver.common.by import By
from behave import *
from selenium import webdriver
import time
from nose.tools import assert_equal, assert_true
from pages.page_base import PageBase
from pages.test_base import TestBase

test_base = TestBase()

@then(u'We open ATP Window')
def step_impl(context):
    context.csm_page.open_add_atp_window()
    time.sleep(15)
    

@then(u'WE add a device')
def step_impl(context):
    context.add_atp.add_atp()
    time.sleep(10)







