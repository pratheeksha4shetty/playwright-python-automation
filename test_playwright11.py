import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/automation-practice-form")
    page.get_by_role("textbox", name="First Name").click()
    page.get_by_role("textbox", name="First Name").press("CapsLock")
    page.get_by_role("textbox", name="First Name").fill("P")
    page.get_by_role("textbox", name="First Name").press("CapsLock")
    page.get_by_role("textbox", name="First Name").fill("Pratheeksha")
    page.get_by_role("textbox", name="Last Name").click()
    page.get_by_role("textbox", name="Last Name").press("CapsLock")
    page.get_by_role("textbox", name="Last Name").fill("S")
    page.get_by_role("textbox", name="Last Name").press("CapsLock")
    page.get_by_role("textbox", name="Last Name").fill("Shetty")
    page.get_by_role("textbox", name="name@example.com").click()
    page.get_by_role("textbox", name="name@example.com").fill("pratheekshashetty84@gmail.com")
    page.get_by_role("radio", name="Female").check()
    page.get_by_role("textbox", name="Mobile Number").click()
    page.get_by_role("textbox", name="Mobile Number").fill("6360249514")
    page.locator("#dateOfBirthInput").click()
    page.get_by_role("combobox").first.select_option("2")
    page.get_by_role("combobox").nth(1).select_option("2004")
    page.get_by_role("gridcell", name="Choose Thursday, March 4th,").click()
    page.locator("#subjectsInput").click()
    page.locator("#subjectsInput").fill("playwright")
    page.get_by_role("checkbox", name="Reading").check()
    page.get_by_role("button", name="Choose File").set_input_files(r"C:\Users\Pratheeksha.Intern\Pictures\Screenshots\Screenshot 2026-11-23 120306.png")
    page.get_by_role("textbox", name="Current Address").click()
    page.get_by_role("textbox", name="Current Address").press("CapsLock")
    page.get_by_role("textbox", name="Current Address").fill("G")
    page.get_by_role("textbox", name="Current Address").press("CapsLock")
    page.get_by_role("textbox", name="Current Address").fill("Gowreshwara nilaya shambhu building tm road koppa -577126")
    page.locator(".css-8mmkcg").first.click()
    page.get_by_role("option", name="NCR").click()
    page.get_by_role("option", name="Delhi").click()
    page.get_by_role("button", name="Submit").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)


import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/select-menu")
    page.locator(".css-19bb58m").first.click()
    page.get_by_role("option", name="Group 1, option 1").click()
    page.locator("#react-select-3-input").click()
    page.get_by_role("option", name="Ms.").click()
    page.locator("#react-select-4-input").click()
    page.locator("#react-select-4-option-0").click()
    page.locator("#react-select-4-option-2").click()
    page.locator("#react-select-4-option-3").click()
    page.locator("#react-select-4-option-1").click()
    page.locator("#cars").select_option("volvo")
    page.locator("#cars").select_option("saab")
    page.locator("#cars").select_option("opel")
    page.locator("#cars").select_option("audi")
    page.locator(".col-12.mt-4.col-md-6 > div:nth-child(2)").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)


import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/progress-bar")
    page.get_by_role("button", name="Start").click()
    page.get_by_role("button", name="Reset").click()
    page.get_by_role("button", name="Start").click()
    page.get_by_role("button", name="Start").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

