#vikas
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://vikas.mortiles.com/")
    page.get_by_role("textbox", name="Enter your username").click()
    page.get_by_role("textbox", name="Enter your username").fill("mamta.gondi")
    page.get_by_role("textbox", name="Enter your password").click()
    page.get_by_role("textbox", name="Enter your password").press("CapsLock")
    page.get_by_role("textbox", name="Enter your password").fill("P")
    page.get_by_role("textbox", name="Enter your password").press("CapsLock")
    page.get_by_role("textbox", name="Enter your password").fill("Password@123")
    page.get_by_role("button", name="Log In").click()
    page.get_by_role("button", name="Generate Invoice").nth(1).click()
    page.get_by_role("button", name="OK").click()
    page.get_by_role("button", name="Charge").first.click()
    page.get_by_role("button", name="Charge").click()
    page.get_by_role("button", name="OK").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
