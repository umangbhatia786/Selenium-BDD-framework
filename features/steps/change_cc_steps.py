from selenium.webdriver.common.by import By
from behave import *
from selenium import webdriver
import time
from nose.tools import assert_equal, assert_true
from pages.page_base import PageBase
from pages.test_base import TestBase

test_base = TestBase()

@then(u'We open change_CC Window')
def step_impl(context):
    context.csm_page.open_change_CC_window()
    time.sleep(15)
    context.change_CC_form.set_change_CC()
