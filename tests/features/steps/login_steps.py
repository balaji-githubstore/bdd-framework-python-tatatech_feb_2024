from assertpy import assert_that
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from tests.features.conf.environment import browser_config, init_page_objects
from tests.features.pages.login_page import LoginPage
from tests.features.pages.main_page import MainPage
from tests.features.pages.search_add_page import SearchOrAddPatientPage


@given(u'I have browser with OpenEMR application')
def step_impl(context):
    browser_config(context)
    init_page_objects(context)

@when(u'I enter username as "{text}"')
def step_impl(context, text):
    # context.driver.find_element(By.ID, "authUser").send_keys(text)
    context.login.enter_username(text)


@when(u'I enter password as "{text}"')
def step_impl(context, text):
    # context.driver.find_element(By.ID, "clearPass").send_keys
    context.login.enter_password(text)


@when(u'I click on LOGIN')
def step_impl(context):
    # context.driver.find_element(By.ID, "login-button").click()
    context.login.click_on_login()

@then(u'I should get access to portal with title "{text}"')
def step_impl(context, text):
    actual_error = context.driver.title
    assert_that(text).is_equal_to(actual_error)


@then(u'I should not get access to portal with error "{text}"')
def step_impl(context, text):
    actual_error = context.driver.find_element(By.XPATH, "//p[contains(text(),'Invalid')]").text
    assert_that(actual_error).contains(text)
