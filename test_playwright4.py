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
        book_table = page.locator("table[name='BookTable']")
        rows = book_table.locator("tbody tr")
        print("Total rows in BookTable:", rows.count())

        for i in range(1, rows.count()):  
            cells = rows.nth(i).locator("td")
            book_name = cells.nth(0).inner_text()
            price = cells.nth(3).inner_text()
            print(f"Book: {book_name} | Price: {price}")

        chrome_row = page.locator("#taskTable tbody tr").filter(has_text="Chrome")
        cpu_load = chrome_row.locator("td").filter(has_text="%").inner_text()
        print("Chrome CPU Load:", cpu_load)

        target_product = "Router"  
        pages = page.locator("#pagination li a")

        for p in range(pages.count()):
            pages.nth(p).click()
            product_row = page.locator("#productTable tbody tr").filter(has_text=target_product)

            if product_row.count() > 0:
                checkbox = product_row.locator("input[type='checkbox']")
                checkbox.check()
                expect(checkbox).to_be_checked()
                price = product_row.locator("td").nth(2).inner_text()
                print(f"Found '{target_product}' on Page {p + 1} | Price: {price}")
                break

    finally:
        context.close()
        browser.close()

with sync_playwright() as playwright:
    run(playwright)


