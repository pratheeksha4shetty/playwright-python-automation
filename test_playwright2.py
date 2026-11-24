import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,slow_mo=1000,  args=["--start-maximized", "--window-position=0,0"])
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")
    page.get_by_role("textbox", name="Enter Name").click()
    page.get_by_role("textbox", name="Enter Name").fill("pratheeksha")
    page.get_by_role("textbox", name="Enter EMail").click()
    page.get_by_role("textbox", name="Enter EMail").fill("pratheekshashetty84@gmail")
    page.get_by_role("textbox", name="Enter Phone").click()
    page.get_by_role("textbox", name="Enter Phone").fill("6360249514")
    page.get_by_role("textbox", name="Address:").click()
    page.get_by_role("textbox", name="Address:").fill("gowreshwara nilaya shambhu building tm road koppa-577126")
    page.get_by_role("radio", name="Female").check()
    page.get_by_role("checkbox", name="Monday").check()
    page.get_by_label("Country:").select_option("india")
    page.get_by_label("Colors:").select_option("blue")
    page.get_by_label("Sorted List:").select_option("cheetah")
    page.locator("#datepicker").click()
    page.get_by_role("link", name="23").click()
    page.locator("#txtDate").click()
    page.get_by_role("link", name="24").click()
    page.get_by_placeholder("Start Date").fill("2026-11-25")
    page.get_by_placeholder("End Date").fill("2026-11-30")
    page.locator("#post-body-1307673142697428135").get_by_role("button", name="Submit").click()
    page.locator("#singleFileInput").set_input_files(r"C:\Users\Pratheeksha.Intern\Pictures\Screenshots\Screenshot 2026-11-20 160627.png")
    page.locator("#multipleFilesInput").set_input_files([r"C:\Users\Pratheeksha.Intern\Pictures\Screenshots\Screenshot 2026-11-20 110136.png",r"C:\Users\Pratheeksha.Intern\Pictures\Screenshots\Screenshot 2026-11-20 111442.png"])
        # Drag and Drop
    page.locator("#draggable").drag_to(page.locator("#droppable"))

    slider = page.locator(".ui-slider-handle").first
    slider.click()
    for _ in range(10):
        page.keyboard.press("ArrowLeft")
    page.get_by_role("textbox", name="Select an item").click()
    page.get_by_text("Item 2", exact=True).click()
    page.get_by_role("link", name="Apple").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
