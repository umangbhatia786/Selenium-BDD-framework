from selenium.webdriver.common.by import By
from behave import *
from selenium import webdriver
import time
from nose.tools import assert_equal, assert_true
from pages.page_base import PageBase
from pages.test_base import TestBase

test_base = TestBase()

@given(u'I Navigate To BAN Window')
def step_impl(context):
    context.csm_page.method_ban_window()


@then(u'We enter the suspended CTN')
def step_impl(context):
    context.csm_page.set_ctn('07996705032')


@then(u'We Open Resume Suspend Window and Click Ok')
def step_impl(context):
    context.csm_page.open_suspend_ban_window()
    time.sleep(12)
    context.resume_suspend_form.resume_suspend_ctn()
    time.sleep(10)