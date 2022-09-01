import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://web.whatsapp.com/')
time.sleep(20)

contatos = ['Projeto NExT - Yara']
mensagem = 'Test bot whatsapp !! Hello Yara Team !!'

def buscar_contato(contato):
    campo_pesquisa = driver.find_element(By.XPATH ,'//div[contains(@class, "copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)
    time.sleep(3)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_element(By.CLASS_NAME ,'p3_M1')
    time.sleep(3)
    campo_mensagem.click()
    campo_mensagem.send_keys(mensagem)
    campo_mensagem.send_keys(Keys.ENTER)


def main() -> None:   
    for contato in contatos:
        buscar_contato(contato)
        enviar_mensagem(mensagem)

if __name__ == "__main__":
    main()
