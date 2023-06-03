# Libs para web scraping
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import matplotlib.pyplot as plt

# Lib para manipulação de dados
import pandas as pd

service = Service(ChromeDriverManager().install())

# Abre o google chrome
driver = webdriver.Chrome(service=service)

# Entra no site do linkedin
driver.get('https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0')
time.sleep(5)

# Cargo de interesse
cargo = 'Analista de dados'

# XPATH do local onde digitamos o cargo de interesse
xpath_cargo = '/html/body/div[1]/header/nav/section/section[2]/form/section[1]/input'

# Digita o cargo no local indicado
box_cargo = driver.find_element(By.XPATH, xpath_cargo)
box_cargo.send_keys(cargo)

# País de interesse
pais = 'São Paulo'

# XPATH do local onde apagamos o que já vem escrito por padrão
xpath_clear = '/html/body/div[1]/header/nav/section/section[2]/form/section[2]/button'
driver.find_element(By.XPATH, xpath_clear).click()

# XPATH do local onde digitamos o país de interesse
xpath_pais = '/html/body/div[1]/header/nav/section/section[2]/form/section[2]/input'

# Digita o país no local indicado
box_pais = driver.find_element(By.XPATH, xpath_pais)
box_pais.send_keys(pais)
time.sleep(2)

# XPATH que seleciona o país indicado
xpath_selecao_pais = '//*[@id="location-1"]'
driver.find_element(By.XPATH, xpath_selecao_pais).click()
time.sleep(5)

# Coleta o tamanho da página
height_inicil = driver.execute_script('return document.body.scrollHeight')

# Looping infinito para carregar toda a página
while True:
    # Leva para o final da página
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(3)
    
    # Coleta o tamnho da página
    height_final = driver.execute_script('return document.body.scrollHeight')
    
    try:
        # Clica no botão de carrega mais vagas
        driver.find_element(By.XPATH, '//*[@id="main-content"]/section[2]/button').click()
        time.sleep(3)
        # Leva para o final da página
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        # Coleta o tamnho da página
        height_final = driver.execute_script('return document.body.scrollHeight')
    except:
        pass
    
    # Compara se houve mudança no tamanho da página
    if height_inicil < height_final:
        height_inicil = height_final
    else:
        break

    # Coletando o html da página
soup = BeautifulSoup(driver.page_source, 'lxml')
all_vagas = soup.find('ul', {'class': 'jobs-search__results-list'})
box_vagas = all_vagas.find_all('li')

# Cria um dataframe
df = pd.DataFrame(columns = [
    'Link Vaga',
    'Link Empresa',
    'Cargo',
    'Nome Empresa',
    'Local',
    'Tempo de Abertura',
    'Status'
])

# Looping para coletar cada informação da vaga
for vaga in box_vagas:
    try:
        link = vaga.find('a', {'class': 'base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]'}).get('href')
    except:
        link = vaga.find('a', {'class': 'base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card'}).get('href')
    
    try:
        cargo = vaga.find('span', {'class': 'sr-only'}).text.strip()
    except:
        cargo = vaga.find('h3', {'class': 'base-search-card__title'}).text.strip()
    
    try:
        linkedin_empresa = vaga.find('a', {'class': 'hidden-nested-link'}).get('href')
    except:
        linkedin_empresa = vaga.find('a', {'class': 'base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card'}).get('href')
    
    try:
        nome_empresa = vaga.find('a', {'class': 'hidden-nested-link'}).text.strip()
    except:
        nome_empresa = vaga.find('h4', {'class': 'base-search-card__subtitle'}).text.strip()
    
    local = vaga.find('span', {'class': 'job-search-card__location'}).text.strip()
    
    try:
        tempo = vaga.find('time', {'class': 'job-search-card__listdate'}).text.strip()
    except:
        tempo = vaga.find('time', {'class': 'job-search-card__listdate--new'}).text.strip()
    
    try:
        status = vaga.find('span', {'class': 'result-benefits__text'}).text.strip()
    except:
        status = ''
        
    # Adiciona as informações no dataframe
    df.loc[len(df)] = [
        link,
        linkedin_empresa,
        cargo,
        nome_empresa,
        local,
        tempo,
        status
    ]

    df.head()

    # Save DataFrame to a CSV file
    df.to_csv('job_data.csv', index=False)


# Example: Bar chart of job count by location
location_counts = df['Local'].value_counts()
plt.bar(location_counts.index, location_counts.values)
plt.xlabel('Location')
plt.ylabel('Job Count')
plt.title('Job Count by Location')
plt.xticks(rotation=90)
plt.show()

# Example: Pie chart of job status
status_counts = df['Status'].value_counts()
plt.pie(status_counts.values, labels=status_counts.index, autopct='%1.1f%%')
plt.title('Job Status')
plt.show()
