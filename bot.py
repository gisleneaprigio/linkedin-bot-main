from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from config import login  - para arquivos com login automático
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(r'.\chromedriver.exe')

browser.get("https://www.linkedin.com/feed")




input_email = browser.find_element_by_id("username")
input_email.send_keys('gisleneaprigio@gmail.com')

input_senha = browser.find_element_by_id("password")
input_senha.send_keys('gi151207')

btn_login = browser.find_element_by_xpath("//button[@type='submit']")
btn_login.click()

busca = browser.find_element_by_xpath("//input[@placeholder='Pesquisar']")
busca.send_keys("Python")
busca.send_keys(Keys.RETURN)

time.sleep(3)

filtro_vagas = browser.find_element_by_xpath("//button[@aria-label='Vagas']")
filtro_vagas.click()

input('')