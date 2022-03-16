from selenium.webdriver.common.by import By
from behave import *
from selenium import webdriver
import time
from nose.tools import assert_equal, assert_true
from pages.page_base import PageBase
from pages.test_base import TestBase

test_base = TestBase()

@then(u'We open Register cards Window and enter Card number')
def step_impl(context) :
    context.csm_page.open_register_cards()
    time.sleep(10)
    context.REGISTER_CARD.set_Register_cards()
