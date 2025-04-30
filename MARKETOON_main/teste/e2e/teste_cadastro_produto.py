from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


def teste_cadastro_produto():
    driver = webdriver.Chrome()

    try:

        driver.get("http://127.0.0.1:8000/cadastro/") 

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "nome"))
        )

        driver.find_element(By.NAME, "nome").send_keys("Quadro")
        driver.find_element(By.NAME, "email").send_keys("joao@example.com")
        driver.find_element(By.NAME, "telefone").send_keys("11999999999")
        driver.find_element(By.NAME, "descricao").send_keys("Quadro abstrato em acrílico")
        driver.find_element(By.NAME, "preco").send_keys("150")

        caminho_imagem = os.path.abspath("imagem_teste.jpg") 
        driver.find_element(By.NAME, "imagem").send_keys(caminho_imagem)
        driver.find_element(By.XPATH, '//button[contains(text(), "Cadastrar")]').click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be("http://127.0.0.1:8000/")  
        )

        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "product-card"))
        )

        produtos = driver.find_elements(By.CLASS_NAME, "product-card")
        encontrado = any("Quadro" in produto.text for produto in produtos)

        assert encontrado, "Produto não foi exibido na home após cadastro."

        print("Teste de cadastro de produto: SUCESSO")

    except Exception as e:
        print(f"Erro no teste de cadastro: {str(e)}")

    finally:
        driver.quit()
