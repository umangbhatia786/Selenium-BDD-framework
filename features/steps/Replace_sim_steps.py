from selenium.webdriver.common.by import By
from behave import *
from selenium import webdriver
import time
from nose.tools import assert_equal, assert_true
from pages.page_base import PageBase
from pages.test_base import TestBase

test_base = TestBase()

@then(u'We open Replace sim and enter IMEI number as {IMEI1}')
def step_impl(context, IMEI1):
    context.csm_page.open_replace_sim(IMEI1)
    time.sleep(5)
