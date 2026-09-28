import re
import time
#from playwright.sync_api import Playwright, expect
from playwright.sync_api import sync_playwright, expect

def test_datepicker():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://demo.automationtesting.in/Datepicker.html")
        #Check if the date_picker is enabled
        date_picker = page.locator("#datepicker1")
        date_picker.evaluate("e1 => e1.removeAttribute('readonly')")
        date_picker.fill("2024-06-15")
        page.wait_for_timeout(2000)
        #date_picker.evaluate("e1 => e1.addAttribute('readonly')")
        page.wait_for_timeout(2000)

