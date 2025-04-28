import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_buscar_produto():
    driver = webdriver.Chrome()

    try:
    
        time.sleep(10)
        
        driver.get("http://127.0.0.1:8000/")  
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        
        barra_busca = driver.find_element(By.NAME, "q")
        barra_busca.send_keys("Aline")
        barra_busca.send_keys(Keys.RETURN)

        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "produto-item"))  
        )
        
        produtos = driver.find_elements(By.CLASS_NAME, "produto-item")
        for produto in produtos:
            assert "Aline" in produto.text, f"Produto inesperado: {produto.text}"

    finally:
        driver.quit()

