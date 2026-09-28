import re
import time
#from playwright.sync_api import Playwright, expect
from playwright.sync_api import sync_playwright, expect

def test_datepicker():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://demo.automationtesting.in/Register.html")
        page.get_by_placeholder("First Name").fill("Sayed")
        page.get_by_placeholder("Last Name").fill("Hasan")
        page.locator("textarea[ng-model=Adress]").fill("test registraion")
        page.locator("input[type=email]").fill("jahid476@gmail.com")
        page.locator("input[type=tel]").fill("7008955488")
        page.get_by_role("radio", name="Male").check
        page.wait_for_timeout(5000)