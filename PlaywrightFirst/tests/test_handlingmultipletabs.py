import re
import time
#from playwright.sync_api import Playwright, expect
from playwright.sync_api import sync_playwright, expect

def test_multiple_tab_window(playwright):
        """Handling multpile tabs and multiple window are same, no separate script for both of these"""
    #with sync_playwright() as p:
        browser = playwright.chromium.launch(headless = False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://demo.automationtesting.in/Windows.html")
        #Handling new page tab before clicking link to open new tab. Stor new page in to a new_page variable
        with page.expect_popup() as popup_info:
            #page.get_by_role("button", name="click").click()  # Opens new window in separate tab..this also works
            page.get_by_role("link", name="Open New Seperate Windows").click()
            page.get_by_role("button", name="click").click()
            new_page=popup_info.value
        new_page.wait_for_load_state()
        #Validating new_page title and clicking Read More link in new_page
        expect(new_page).to_have_title("Selenium")
        print("Title of new page:", new_page.title())
        print("Url of new page:", new_page.url)
        new_page.get_by_role("link", name="Read more").nth(0).click()
        new_page.wait_for_timeout(3000)
        #Navigating back to Main page keeping new page opened
        page.bring_to_front()
        #Doing some activity in new_page
        page.get_by_role("link", name="Open New Seperate Windows")
        page.wait_for_timeout(3000)
        #Navigating back to new_page again to do some more activity
        new_page.bring_to_front()
        new_page.get_by_role("link", name="W3C Recommendation").click()
        page.wait_for_timeout(300)
        #Closing new_page, Automatically focus will shift to main page or the previuos page from where new page opened up
        new_page.close()
        page.wait_for_timeout(300)
        page.get_by_role("link", name="Open Seperate Multiple Windows").click()
        page.wait_for_timeout(300)
