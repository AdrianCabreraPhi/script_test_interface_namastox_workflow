import pytest,os
from getpass import getpass
from playwright.sync_api import Page, expect
from dotenv import load_dotenv
from pages.login_page import LoginPage


load_dotenv()

USERNAME = os.getenv("NAMASTOX_USER")
PASSWORD = os.getenv("NAMASTOX_PASSWORD")

if USERNAME is None or PASSWORD is None:
    print("Not found environment variables in your directory")
    print("Recommendation: configure .env with your credentials")
    USERNAME = input("Introduce your username: ")
    PASSWORD = getpass(prompt="Introduce your password: ")

@pytest.fixture(scope="function")
def login_page(page: Page):
    return LoginPage(page)


@pytest.fixture(scope="function")
def auth_page(page:Page,login_page: LoginPage):
    login_page.navigate()
    login_page.login(USERNAME,PASSWORD)
    assert login_page.is_logged(), "Incorrect credentials"

    return page
