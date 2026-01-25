import pytest,os
from getpass import getpass
from playwright.sync_api import Page, expect
from dotenv import load_dotenv
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.general_information_tab import GeneralInformationTab
load_dotenv()

USERNAME = os.getenv("NAMASTOX_USER")
PASSWORD = os.getenv("NAMASTOX_PASSWORD")

if USERNAME is None or PASSWORD is None:
    print("Not found environment variables in your directory")
    print("Recommendation: configure .env with your credentials")
    USERNAME = input("Introduce your username: ")
    PASSWORD = getpass(prompt="Introduce your password: ")

@pytest.fixture()
def login_page(page: Page):
    return LoginPage(page)

@pytest.fixture()
def auth_page(page:Page,login_page: LoginPage):
    login_page.navigate()
    login_page.login(USERNAME,PASSWORD)
    assert login_page.is_logged(), "Incorrect credentials"

    return page

@pytest.fixture()
def dashboard_page(auth_page):
    return DashboardPage(auth_page)

@pytest.fixture()
def general_information_tab(page):
    return GeneralInformationTab(page)
