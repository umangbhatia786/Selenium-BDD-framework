from selenium.webdriver.common.by import By
from behave import *
from selenium import webdriver
import time
from nose.tools import assert_equal, assert_true
from pages.page_base import PageBase
from pages.test_base import TestBase

test_base = TestBase()
@then(u'We open IMEI Update tab')
def step_impl(context):
  context.csm_page.open_Update_IMEI_window()

@then(u'We open Update_IMEI Window give reason as {reason} and Enter IMEI {IMEI}')
def step_impl(context, reason, IMEI):
    context.Update_IMEI_form.set_Update_IMEI(reason,IMEI)
