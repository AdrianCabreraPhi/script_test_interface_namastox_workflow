import pytest
from playwright.sync_api import Page, expect

USERNAME = "adrianupf"
PASSWORD = "adrianupf"


@pytest.fixture(scope="function")
def auth_page(page: Page):

    page.goto("https://namastox.upf.edu/auth/realms/namastox/protocol/openid-connect/auth?client_id=namastox-client&redirect_uri=https://namastox.upf.edu/callback&response_type=code&scope=openid%20profile%20email")

    page.locator("#username").fill(USERNAME)
    page.locator("#password").fill(PASSWORD)
    page.locator("#kc-login").click()
    
    expect(page.get_by_text("Select RA")).to_be_visible()

    yield page