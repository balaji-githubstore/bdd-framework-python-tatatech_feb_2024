from assertpy import assert_that
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'I have browser with OpenEMR application')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get("https://demo.openemr.io/b/openemr")




@when(u'I enter username as "{text}"')
def step_impl(context, text):
    context.driver.find_element(By.ID, "authUser").send_keys(text)


@when(u'I enter password as "{text}"')
def step_impl(context, text):
    context.driver.find_element(By.ID, "clearPass").send_keys(text)


@when(u'I click on LOGIN')
def step_impl(context):
    context.driver.find_element(By.ID, "login-button").click()


@then(u'I should get access to portal with title "{text}"')
def step_impl(context, text):
    actual_error = context.driver.title
    assert_that(text).is_equal_to(actual_error)


@then(u'I should not get access to portal with error "{text}"')
def step_impl(context, text):
    actual_error = context.driver.find_element(By.XPATH, "//p[contains(text(),'Invalid')]").text
    assert_that(actual_error).contains(text)
