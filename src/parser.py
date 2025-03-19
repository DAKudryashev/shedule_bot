from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://mai.ru/education/studies/schedule/index.php?group=М3О-312Б-22")

element = driver.find_element(By.ID,  'department')
# print(element.is_displayed(), element.is_enabled())
select = Select(element)
select.select_by_value('Институт №3')

element1 = driver.find_element(By.ID,  'course')
# print(element1.is_displayed(), element1.is_enabled())
select1 = Select(element1)
select1.select_by_value('3')

driver.find_element(By.CSS_SELECTOR, 'div.col-md-3.col-5.mb-2.mb-md-0').click()
groups = driver.find_elements(By.CSS_SELECTOR, 'a.btn.btn-soft-secondary.btn-xs.mb-1.fw-medium.btn-group')
# Явное ожидание, чтобы дождаться загрузки кнопки
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'М3О-312Б-22')))
driver.execute_script("arguments[0].click();", button)

soup = BeautifulSoup(driver.page_source, 'html.parser')

temp = soup.find_all('div', 'step-content-wrapper')
print(temp[0].text)
driver.close()
