import re
import time
#from playwright.sync_api import Playwright, expect
from playwright.sync_api import sync_playwright, expect

def test_modals(playwright):
    #with sync_playwright() as p:
        browser = playwright.chromium.launch(headless = False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://demo.automationtesting.in/Modals.html")
        page.get_by_role("link", name="Launch modal").nth(0).click()
        #verify modal popup displayed
        modal=page.get_by_role("heading", name="Modal title")
        expect(modal).to_be_visible
        #Save modal and close
        page.get_by_role("button", name="Save changes").click()
        page.wait_for_timeout(5000)
        expect(modal).not_to_be_visible
        
        #Handling multiple Modallink
        page.get_by_role("link", name="Launch modal").nth(1).click()
        #verify modal popup displayed
        modal=page.get_by_role("heading", name="First Modal")
        expect(modal).to_be_visible
        #Select modal inside modal popup
        page.get_by_role("link", name="Launch modal").nth(2).click()
        #page.get_by_role("link", name="Launch modal").last.click()
        page.wait_for_timeout(3000)
        page.get_by_role("link", name="Save changes").last.click()
        page.wait_for_timeout(5000)
        expect(modal).not_to_be_visible
