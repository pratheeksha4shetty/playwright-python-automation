#"http://192.168.10.165:6002/"
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://192.168.10.165:6002/")
    page.get_by_role("textbox", name="Enter a valid ZIP Code (12345").click()
    page.get_by_role("textbox", name="Enter a valid ZIP Code (12345").fill("55555")
    page.get_by_text("Remove Add").click()
    page.get_by_role("radio").nth(2).check()
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("textbox", name="First Name").click()
    page.get_by_role("textbox", name="First Name").fill("trdfgdhgdc")
    page.get_by_role("textbox", name="Billing Address").click()
    page.get_by_role("textbox", name="Billing Address").fill("cfghcfghcghcncgchc,nkjgiuyfyfv")
    page.get_by_role("textbox", name="Last Name").click()
    page.get_by_role("textbox", name="Last Name").fill("shetty")
    page.get_by_role("textbox", name="Phone").click()
    page.get_by_role("textbox", name="Phone").fill("9449660908")
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("pratheekshashetty84@gmail.com")
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("button", name="Checkout").click()
    page.locator("#card-element").click()

    # Use ^= ("starts with") to match Stripe's dynamic iframe name on every run
    stripe_frame = page.frame_locator('iframe[name^="__privateStripeFrame"]').first

    stripe_frame.get_by_role("textbox", name="Credit or debit card number").fill("4242 4242 4242 4242")
    stripe_frame.get_by_role("textbox", name="Credit or debit card expiration date").fill("01 / 37")
    stripe_frame.get_by_role("textbox", name="Credit or debit card CVC/CVV").fill("454")
    stripe_frame.get_by_role("textbox", name="ZIP").fill("55555")

    page.get_by_role("textbox", name="Name on card").fill("kkkkkkkkk")
    page.get_by_role("button", name="Place Order").click()
    page.get_by_role("button", name="OK").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
