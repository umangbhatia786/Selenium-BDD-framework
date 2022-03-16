from selenium.webdriver.common.by import By
from behave import *
from selenium import webdriver
import time
from nose.tools import assert_equal, assert_true
from pages.page_base import PageBase
from pages.test_base import TestBase

test_base = TestBase()

@then(u'We open Billed calls')
def step_impl(context):
  context.csm_page.open_billed_unbilled_val()
  time.sleep(10)
  context.Billed_Unbilled.set_Billed_Unbilled()
  time.sleep(10)


