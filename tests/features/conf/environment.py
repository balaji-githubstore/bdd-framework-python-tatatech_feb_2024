from selenium import webdriver

from tests.features.pages.login_page import LoginPage
from tests.features.pages.main_page import MainPage
from tests.features.pages.search_add_page import SearchOrAddPatientPage


def browser_config(context):
    context.driver = webdriver.Edge()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get("https://demo.openemr.io/b/openemr")


def init_page_objects(context):
    context.login = LoginPage(context.driver)
    context.main = MainPage(context.driver)
    # context.search = SearchOrAddPatientPage(context.driver)
