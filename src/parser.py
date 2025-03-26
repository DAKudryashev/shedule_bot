from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup


class Parser:
    def __init__(self):
        self.department = ''
        self.course = ''
        self.group = ''
        self.parsed_week = []
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://mai.ru/education/studies/schedule/index.php?group=М3О-312Б-22")

    def get_departments(self):
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        departments = soup.find(name='select', attrs='form-select form-select-lg').text
        departments = [department.strip() for department in departments.split('\n') if department.strip()][1:]
        return departments

    def get_courses(self):
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        courses = (soup.find(name='select', attrs='form-select form-select-lg').
                   find_next(name='select', attrs='form-select form-select-lg').text)
        courses = [course.strip() for course in courses.split('\n') if course.strip()][2:]
        print(courses)

    def choose_department_and_course(self, department, course):
        # Выбор института
        element = self.driver.find_element(By.ID, 'department')
        # print(element.is_displayed(), element.is_enabled())
        select = Select(element)
        select.select_by_value(value=department)

        # Выбор курса и переход на следующую страницу
        element1 = self.driver.find_element(By.ID, 'course')
        # print(element1.is_displayed(), element1.is_enabled())
        select1 = Select(element1)
        select1.select_by_value(value=course)
        self.driver.find_element(By.CSS_SELECTOR, 'div.col-md-3.col-5.mb-2.mb-md-0').click()

    def get_groups(self):
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        groups = soup.find(name='div', attrs='tab-pane fade show active').text
        groups = [group for group in groups.split('\n') if group]
        print(groups)
        return groups

    def choose_group(self, group):
        # Ожидание загрузки кнопки и выбор группы
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, group)))
        self.driver.execute_script('arguments[0].click();', button)

    def go_to_previous_page(self):
        self.driver.execute_script('window.history.go(-1)')

    def get_week_schedule(self):
        # Парсинг страницы с открывшимся расписанием
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        days = soup.find_all('div', class_='step-content')
        week = []
        for day in days:
            day_date = day.find('span', class_='step-title')

            if day_date:
                print(f"\nДата: {day_date.get_text(strip=True)}")
            else:
                continue

            disciplines = []
            for div in day.find_all('div', class_='mb-4'):
                discipline = div.find('div', class_='d-flex align-items-center justify-content-between')
                subject = []
                if discipline:
                    subject.append(discipline.get_text(strip=True, separator=" "))
                for li in div.find_all('li', class_='list-inline-item'):
                    if li:
                        subject.append(li.get_text(strip=True))
                disciplines.append(subject)
            print(disciplines)
            week.append([day_date.get_text(strip=True).replace('\xa0', ' '), disciplines])
        # print(week)
        return week


if __name__ == '__main__':
    parser_a = Parser()
    parser_a.choose_department_and_course('Институт №3', '3')
    parser_a.choose_group('М3О-312Б-22')
    parser_a.get_week_schedule()
    parser_a.driver.close()
