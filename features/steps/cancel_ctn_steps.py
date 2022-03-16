from selenium.webdriver.common.by import By
from behave import *
from selenium import webdriver
import time
from nose.tools import assert_equal, assert_true
from pages.page_base import PageBase
from pages.test_base import TestBase

test_base = TestBase()

@then(u'We enter the CTN {CTN}')
def step_impl(context, CTN):
    context.csm_page.set_ctn(CTN)


@then(u'We open Cancel_CTN Window and Cancel with Reason as {reason} and DRM as {DRM}')
def step_impl(context, reason, DRM):
    context.csm_page.open_cancel_ctn_window()
    time.sleep(15)
    context.cancel_ctn_form.cancel_ctn(reason, DRM)
    time.sleep(10)