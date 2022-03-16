from selenium import webdriver
import time
from nose.tools import assert_equal, assert_true
from pages.page_base import PageBase
from pages.test_base import TestBase

test_base = TestBase()

@then(u'We give PAC as {PAC} and Ported CTN as {PCTN}')
def step_impl(context,PAC,PCTN):
    context.csm_page.open_port_in(PAC,PCTN)
    time.sleep(10)

