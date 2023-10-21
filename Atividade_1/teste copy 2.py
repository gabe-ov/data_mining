from selenium import webdriver
import time
# Configurando o driver do Microsoft Edge
driver = webdriver.Firefox()

driver.get("https://www.uol.com.br/")


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