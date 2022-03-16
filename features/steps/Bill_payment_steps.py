from selenium.webdriver.common.by import By
from behave import *
from selenium import webdriver
import time
from nose.tools import assert_equal, assert_true
from pages.page_base import PageBase
from pages.test_base import TestBase

test_base = TestBase()

@then(u'We open Bill Payment')
def step_impl(context):
    context.bill_payment.bill_payment()
    time.sleep(10)
  


