from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()

# Inicializar o driver do Chrome com as opções
driver = webdriver.Chrome(options=chrome_options)

# Abrir o site UOL
url = "https://www.uol.com.br/"
driver.get(url)

# Aguarde alguns segundos para que a página seja carregada e você possa visualizá-la
time.sleep(5)

# Rolar a página até o fim
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Fechar o navegador
driver.quit()
