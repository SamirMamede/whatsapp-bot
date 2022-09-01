import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://web.whatsapp.com/')
time.sleep(30)

contatos = ['Projeto NExT - Yara']
mensagem = 'Test bot whatsapp !! Hello humans !!'

def buscar_contato(contato):
    campo_pesquisa = driver.find_element(By.XPATH ,'//div[contains(@class, "copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)


def main() -> None:   
    for contato in contatos:
        buscar_contato(contato)
    # enviar_mensagem(mensagem)
    # campo de mensagem privada
    # 'copyable-text selectable-text'

if __name__ == "__main__":
    main()
