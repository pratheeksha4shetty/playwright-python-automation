import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/form_validation")
    page.get_by_role("textbox", name="Username (lowercase letters").click()
    page.get_by_role("textbox", name="Username (lowercase letters").fill("prathi0908")
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("pratheekshashetty84@gmail.com")
    page.get_by_role("spinbutton", name="Age (18 to 120)").click()
    page.get_by_role("spinbutton", name="Age (18 to 120)").fill("21")
    page.get_by_role("textbox", name="Website (optional)").click()
    page.get_by_role("textbox", name="Website (optional)").fill("https://the-internet.herokuapp.com/form_validation")
    page.get_by_role("textbox", name="Password (at least 8").click()
    page.get_by_role("textbox", name="Password (at least 8").fill("@")
    page.get_by_role("textbox", name="Password (at least 8").press("CapsLock")
    page.get_by_role("textbox", name="Password (at least 8").fill("@P")
    page.get_by_role("textbox", name="Password (at least 8").press("CapsLock")
    page.get_by_role("textbox", name="Password (at least 8").fill("@Prathi09089")
    page.get_by_role("checkbox", name="I accept the terms").check()
    page.get_by_role("button", name="Create account").click()

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
    page.goto("https://demoqa.com/upload-download")
    with page.expect_download() as download_info:
        page.get_by_role("button", name="Download").click()
    download = download_info.value
    page.get_by_role("button", name="Choose File").set_input_files(r"C:\Users\Pratheeksha.Intern\Pictures\Screenshots\Screenshot 2026-11-20 110136.png")
    page.locator(".col-12.mt-4.col-md-6 > div:nth-child(2)").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)


from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(
        headless=False,
        slow_mo=1000,
        args=["--start-maximized", "--window-position=0,0"]
    )
    context = browser.new_context(no_viewport=True)
    page = context.new_page()

    try:
        page.goto("https://demoqa.com/alerts")

        # 1. Immediate Alert
        page.once("dialog", lambda dialog: dialog.accept())
        page.locator("#alertButton").click()

        # 2. Timer Alert (Appears after 5 seconds — wait 6s so it finishes before next alert)
        page.once("dialog", lambda dialog: dialog.accept())
        page.locator("#timerAlertButton").click()
        page.wait_for_timeout(6000)

        # 3. Confirm Box Alert (Click OK with accept(), or Cancel with dismiss())
        page.once("dialog", lambda dialog: dialog.dismiss())
        page.locator("#confirmButton").click()

        # 4. Prompt Box Alert (Pass your name inside accept())
        page.once("dialog", lambda dialog: dialog.accept("Pratheeksha"))
        page.locator("#promtButton").click()

    finally:
        context.close()
        browser.close()


with sync_playwright() as playwright:
    run(playwright)
