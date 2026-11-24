import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()

    page.goto("http://devujjval.mortiles.com/")
    page.locator('input[name="username"]').fill("mamta.gondi")
    page.locator('input[name="userpwd"]').fill("Password@123")
    page.get_by_role("button", name="Sign In").click()

    page.get_by_role("heading", name="Order").click()
    page.get_by_role("link", name="Order Management").click()
    page.get_by_role("link", name="Order Search (List)").click()
    page.get_by_role("button", name="Search").click()

    page.get_by_role("link", name="261121468").first.click()

    page.locator('input[name="ZipCode"]').dblclick()
    page.locator('input[name="ZipCode"]').press("ControlOrMeta+c")

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
    page.goto("http://192.168.10.165:6002/")
    page.get_by_role("textbox", name="Enter a valid ZIP Code (12345").click()
    page.get_by_role("textbox", name="Enter a valid ZIP Code (12345").fill("20901")
    page.get_by_text("Services Service Details :").click()
    page.locator("#radioContainer > div:nth-child(6) > .col-md-8").click()
    page.locator("#radioContainer > div:nth-child(6) > .col-md-8").click()
    page.get_by_role("radio").nth(1).check()
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("textbox", name="First Name").click()
    page.get_by_role("textbox", name="First Name").fill("pratheeksha")
    page.get_by_role("textbox", name="Billing Address").click()
    page.get_by_role("textbox", name="Billing Address").fill("ghesrtshserhesheshwh")
    page.get_by_role("textbox", name="Last Name").click()
    page.get_by_role("textbox", name="Last Name").fill("rrrrrrrrrrr")
    page.get_by_role("textbox", name="Phone").click()
    page.get_by_role("textbox", name="Phone").click()
    page.get_by_role("textbox", name="Phone").fill("6779878675675")
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("pratheekshashetty84@gmail.com")
    page.get_by_role("button", name="Checkout").click()
    stripe_frame = page.frame_locator('iframe[name^="__privateStripeFrame"]').first

    stripe_frame.get_by_role("textbox", name="Credit or debit card number").fill("4242 4242 4242 4242")
    stripe_frame.get_by_role("textbox", name="Credit or debit card expiration date").fill("01 / 37")
    stripe_frame.get_by_role("textbox", name="Credit or debit card CVC/CVV").fill("454")
    stripe_frame.get_by_role("textbox", name="ZIP").fill("20901")

    page.get_by_role("textbox", name="Name on card").fill("pppppppppp")
    page.get_by_role("button", name="Place Order").click()
    page.get_by_role("button", name="OK").click()

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

