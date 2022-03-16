from selenium.webdriver.common.by import By
from behave import *
from selenium import webdriver
import time
from nose.tools import assert_equal, assert_true
from pages.page_base import PageBase
from pages.test_base import TestBase

test_base = TestBase()

@then(u'We open change BAC Window and enter new address {bill_address}')
def step_impl(context,bill_address):
    context.csm_page.open_view_profile_address_change()
    time.sleep(10)
    context.change_only_bill_form.change_billing_address(bill_address)
