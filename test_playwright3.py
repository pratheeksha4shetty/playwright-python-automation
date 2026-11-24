from playwright.sync_api import Playwright, sync_playwright, expect
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(
        headless=False,
        slow_mo=2000,
        args=["--start-maximized", "--window-position=0,0"]
    )
    context = browser.new_context(no_viewport=True)
    page = context.new_page()

    try:
        page.goto("https://testautomationpractice.blogspot.com/")
        page.once("dialog", lambda dialog: dialog.accept())
        page.get_by_role("button", name="Simple Alert").click()
        page.once("dialog", lambda dialog: dialog.dismiss())
        page.get_by_role("button", name="Confirmation Alert").click()
        page.once("dialog", lambda dialog: dialog.accept("Pratheeksha"))
        page.get_by_role("button", name="Prompt Alert").click()
        expect(page.locator("#demo")).to_contain_text("Pratheeksha")
        with context.expect_page() as new_tab_info:
            page.get_by_role("button", name="New Tab").click()
        
        new_tab = new_tab_info.value
        new_tab.wait_for_load_state()
        print("New Tab Title:", new_tab.title())
        new_tab.close() 
        with page.expect_popup() as popup_info:
            page.get_by_role("button", name="Popup Windows").click()
        popup = popup_info.value
        popup.wait_for_load_state()
        print("Popup Title:", popup.title())
        popup.close()
    finally:
        context.close()
        browser.close()
with sync_playwright() as playwright:
    run(playwright)
