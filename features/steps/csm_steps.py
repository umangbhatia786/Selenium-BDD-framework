from selenium.webdriver.common.by import By
from behave import *
from selenium import webdriver
import time
from nose.tools import assert_equal, assert_true
from pages.page_base import PageBase
from pages.test_base import TestBase

test_base = TestBase()

@given(u'We Navigate To BAN Window')
def step_impl(context):
    try:
        print('click ban window')
        context.csm_page.method_ban_window()
        print('enter ctn and get')
        context.csm_page.set_ctn('07996705028')
        print('open suspnd ctn window')
        context.csm_page.open_suspend_ban_window()
        print('suspend ctn')
        time.sleep(12)
        context.suspend_form.suspend_ctn()
        time.sleep(10)
    except Exception as e:
        print(e)
