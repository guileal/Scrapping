from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        # Navegar até a página do iFood
        page.goto('https://www.ifood.com.br/restaurantes')
        
        input = page.wait_for_selector('.address-search-input__field', state='visible')
        # Esperar pelo botão de pesquisa

        input.evaluate('el => el.removeAttribute("disabled")')
        print(page.wait_for_selector('.address-search-input__field', state='visible').is_disabled())

        

        # Localização + Formulario de input de localização
        localizacao = 'Carvoeira'
        # inputLocalizacao = page.locator('address-search-input__field')
        # input.fill(localizacao)
        input.type(localizacao, delay=100)

        input.press("Enter")
        
        # Pegar Lista
        # ul -> .address-search-list
        page.wait_for_timeout(5000)

        page.screenshot(path="screenshot.png", full_page=True)
        addressSearchList = page.wait_for_selector('.address-search-list li', state='visible')

        # clicar no primeiro item -> li .button-address-ChIJ-WE4j6w5J5URja6WKHqK5Tk
        # .btn-address__info--label
        elementoEscolhido = page.locator('.address-search-list li:has-text("{localizacao}")')

        elementoEscolhido.click()

        page.screenshot(path="screenshot.png", full_page=True)




        codigo_html = page.content()

        with open('scraping.html', 'w') as arquivo:
            arquivo.write(codigo_html)

        # print('AAAAAAAAAAAAAAA',html_elemento)
        # with open('scrapping.html', 'w') as arquivo:
        #     print('Entrando1')
        #     arquivo.write(html_elemento)
        
        # # Preenchendo input
        # inputLocalizacao.fill(localizacao)

        # # Pegando value para printar
        # inputValue = page.input_value()
        # print('input value: ', inputValue)

        # # Salvar o conteúdo HTML da página
        # html_content = page.content()

        # with open('scrapping.html', 'w') as arquivo:
        #     print('Entrando')
        #     arquivo.write(html_content)

        # Aguardar o carregamento da lista
        # page.wait_for_selector('.address-search-list')
        # Agora você pode continuar com as interações na lista, como clicar em um botão dentro dela.

        # Fechar o navegador
        browser.close()

if __name__ == "__main__":
    main()
