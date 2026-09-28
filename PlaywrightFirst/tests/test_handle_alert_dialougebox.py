import re
import time
#from playwright.sync_api import Playwright, expect
from playwright.sync_api import sync_playwright, expect

def test_modals(playwright):
    #with sync_playwright() as p:
        browser = playwright.chromium.launch(headless = False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://demo.automationtesting.in/Alerts.html")
        #Handling alert box
        page.on("dialog", lambda dialog: dialog.accept())
        #Click on the button which triggers alert box
        page.get_by_role("button", name="click the button to display an alert box:").click()
        page.wait_for_timeout(3000)

        page.get_by_role("link", name="Alert with OK & Cancel").click()
        page.on("dialog", lambda dialog: dialog.accept())
        #Click on the button which triggers alert box
        page.get_by_role("button", name="click the button to display a confirm box").click()
        page.wait_for_timeout(3000)

        page.get_by_role("link", name="Alert with Textbox").click()
        page.on("dialog", lambda dialog: dialog.accept("Sayed"))
        #Click on the button which triggers alert box
        page.get_by_role("button", name="click the button to demonstrate the prompt box").click()
        page.wait_for_timeout(3000)

