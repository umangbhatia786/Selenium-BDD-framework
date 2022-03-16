from selenium.webdriver.common.by import By
from behave import *
from selenium import webdriver
import time
from nose.tools import assert_equal, assert_true
from pages.page_base import PageBase
from pages.test_base import TestBase

test_base = TestBase()

@then(u'We open Refresh_CTN Window and Refresh with Reason as {reason}')
def step_impl(context, reason):
    context.csm_page.open_refresh_ctn_window()
    time.sleep(8)
    context.refresh_ctn_form.set_refresh_ctn(reason)
    time.sleep(2)