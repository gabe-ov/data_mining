from selenium import webdriver

# Inicializa o driver do Chrome
driver = webdriver.Firefox(executable_path='/home/gabe/anaconda3/geckodriver')

# Navega até o site do Google
driver.get("https://www.google.com")

# Localiza o campo de pesquisa e digita uma consulta
search_box = driver.find_element_by_name("q")
search_box.send_keys("Exemplo de pesquisa com Selenium")

# Submete o formulário de pesquisa
search_box.submit()

# Feche o navegador após a execução
driver.quit()
