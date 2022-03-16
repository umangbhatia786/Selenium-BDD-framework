from selenium.webdriver.common.by import By
from behave import *
from selenium import webdriver
import time
from nose.tools import assert_equal, assert_true
from pages.page_base import PageBase
from pages.test_base import TestBase

test_base = TestBase()

@then(u'We open change CAB Window and enter new address {address}')
def step_impl(context, address):
    context.csm_page.open_view_profile_address_change()
    time.sleep(15)
    context.change_custandbill_add_form.change_custandbilling_address(address)
