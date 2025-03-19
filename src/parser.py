from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import string


class Parser:
    def __init__(self, department, course, group):
        self.department = department
        self.course = course
        self.group = group
        self.text_by_days = []

    def get_schedule_by_days(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://mai.ru/education/studies/schedule/index.php?group=М3О-312Б-22")

        # Выбор института
        element = driver.find_element(By.ID, 'department')
        # print(element.is_displayed(), element.is_enabled())
        select = Select(element)
        select.select_by_value('Институт №3')

        # Выбор курса и переход на следующую страницу
        element1 = driver.find_element(By.ID, 'course')
        # print(element1.is_displayed(), element1.is_enabled())
        select1 = Select(element1)
        select1.select_by_value('3')
        driver.find_element(By.CSS_SELECTOR, 'div.col-md-3.col-5.mb-2.mb-md-0').click()

        # Ожидание загрузки кнопки и выбор группы
        wait = WebDriverWait(driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'М3О-312Б-22')))
        driver.execute_script("arguments[0].click();", button)

        # Парсинг страницы с открывшимся расписанием
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        if self.group not in soup.find('h1', 'mb-5').text:
            print('incorrect open of group page')
        else:
            days = soup.find_all('div', 'step-content-wrapper')
            self.text_by_days = [i.text for i in days]
            # print(self.text_by_days)
            driver.close()

    def normalize_text(self):
        for i in range(len(self.text_by_days)):
            tmp = self.text_by_days[i].replace('\xa0', ' ')
            tmp = tmp.split('\t')
            while '' in tmp:
                tmp.remove('')
            tmp = ' '.join(tmp)
            tmp = tmp.replace('\n', '')
            tmp = tmp.replace('  ', ' ')
            print(tmp)
            self.text_by_days[i] = tmp


if __name__ == '__main__':
    parser_a = Parser('Институт №3', '3', 'М3О-312Б-22')
    parser_a.get_schedule_by_days()
    parser_a.normalize_text()
