# pip install playwright
from playwright.sync_api import sync_playwright

def getHTML(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        codigo_html = page.content()
        browser.close()
    return codigo_html

# Exemplo de uso
url = 'https://www.google.com'
contentHTML = getHTML(url)

# Criação de cópia
with open('index.html', 'w') as arquivo:
    arquivo.write(contentHTML)
print(contentHTML)


