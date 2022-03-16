from selenium.webdriver.common.by import By
from behave import *
from selenium import webdriver
import time
from nose.tools import assert_equal, assert_true
from pages.page_base import PageBase
from pages.test_base import TestBase

test_base = TestBase()

@then(u'We open Billing date Window')
def step_impl(context):
  context.csm_page.open_billing_cycle()
  time.sleep(10)
  context.Billing_Date.set_Billing_date()
  time.sleep(10)


