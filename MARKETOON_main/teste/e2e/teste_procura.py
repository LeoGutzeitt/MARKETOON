from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def teste_produto_existente():
    driver = webdriver.Chrome()


    try:
        driver.get("http://127.0.0.1:8000/")  
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        barra_busca = driver.find_element(By.NAME, "q")
        barra_busca.send_keys("Aline")  
        barra_busca.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "product-card"))
        )


        produtos = driver.find_elements(By.CLASS_NAME, "product-card")
        assert len(produtos) > 0, "Nenhum produto encontrado para a busca."


        for produto in produtos:
            assert "Aline" in produto.text, f"Produto inesperado: {produto.text}"


    except Exception as e:
        print(f"Erro no teste: {str(e)}")


    finally:
        driver.quit()




def test_produto_inexistente():
    driver = webdriver.Chrome()


    try:
        driver.get("http://127.0.0.1:8000/")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        barra_busca = driver.find_element(By.NAME, "q")
        barra_busca.send_keys("ProdutoInexistente")  
        barra_busca.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "no-results-message"))
        )


        mensagem_erro = driver.find_element(By.CLASS_NAME, "no-results-message")
        assert "Nenhum produto encontrado" in mensagem_erro.text, f"Mensagem de erro inesperada: {mensagem_erro.text}"


    except Exception as e:
        print(f"Erro no teste: {str(e)}")


    finally:
        driver.quit()


