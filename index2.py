from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://google.com.br')
    
    input = page.locator('id=APjFqb')
    input.type('Ama', delay=100)

    page.wait_for_timeout(3000)

    page.screenshot(path='screenshot google.jpg', full_page=True)

    browser.close()