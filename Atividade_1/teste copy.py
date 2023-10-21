from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Configurando o caminho para o Chrome WebDriver
driver_path = 'Caminho/para/o/seu/chromedriver.exe'  # Substitua pelo caminho correto

# Inicializando o navegador Chrome
driver = webdriver.Chrome(executable_path=driver_path)

# Abrindo o site UOL
driver.get("https://www.uol.com.br")

# Defina um atraso para permitir que a página seja carregada completamente
time.sleep(3)

# Rolar a página para baixo
while True:
    # Simule a rolagem pressionando a tecla 'END' (fim)
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    
    # Aguarde um curto período de tempo para a página rolar
    time.sleep(1)
    
    # Verifique se chegou ao final da página
    if driver.execute_script("return window.innerHeight + window.scrollY") >= driver.execute_script("return document.body.scrollHeight"):
        break

# Aguarde algum tempo adicional após a rolagem antes de fechar o navegador (opcional)
time.sleep(3)

# Feche o navegador
driver.quit()
