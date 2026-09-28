import re
import time
from playwright.sync_api import Page, expect
def test_locatorsdemo(page: Page):
    page.goto("https://www.saucedemo.com/")
    expect(page).to_have_title(re.compile("Swag Labs"))
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="login").click  # button - which type of element, name="what is the value text or text of that element"
    #page.locator("#login-button").click  # this is Id of element, here we have used CSS selector
    time.sleep(5)