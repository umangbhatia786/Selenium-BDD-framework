from selenium import webdriver
import time
from nose.tools import assert_equal, assert_true
from pages.page_base import PageBase
from pages.test_base import TestBase

test_base = TestBase()

@then(u'We open add soc and enter Feature name {Feature}')
def step_impl(context,Feature):
    context.add_soc.add_feature(Feature)
    time.sleep(10)

