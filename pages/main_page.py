from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure

class MainPage(BasePage):
    ABOUT_SECTION = (By.XPATH, "//a[contains(text(), 'О нас') or contains(@href, '#about')]")
    CONTACTS_SECTION = (By.XPATH, "//a[contains(text(), 'Контакты') or contains(@href, '#contact')]")
    VACANCIES_SECTION = (By.XPATH, "//a[contains(text(), 'Вакансии') or contains(@href, '#specializations')]")
    SERVICES_SECTION = (By.XPATH, "//a[contains(text(), 'Аутстафф') or contains(text(), 'Трудоустройство') or contains(@href, '#services')]")
    REVIEWS_SECTION = (By.XPATH, "//a[contains(text(), 'Отзывы') or contains(@href, '#testimonials')]")

    BASE_URL = "https://www.effective-mobile.ru"

    EXPECTED_URLS = {
        'about': f"{BASE_URL}/#about",
        'contacts': f"{BASE_URL}/#contact",
        'vacancies': f"{BASE_URL}/#specializations",
        'services': f"{BASE_URL}/#services",
        'reviews': f"{BASE_URL}/#testimonials"
    }

    @allure.step("Открыть главную страницу")
    def open(self):
        self.go_to_url(self.BASE_URL)

    @allure.step("Нажать на раздел 'О нас'")
    def click_about_section(self):
        self.click_element(self.ABOUT_SECTION)

    @allure.step("Нажать на раздел 'Контакты'")
    def click_contacts_section(self):
        self.click_element(self.CONTACTS_SECTION)

    @allure.step("Нажать на раздел 'Вакансии'")
    def click_vacancies_section(self):
        self.click_element(self.VACANCIES_SECTION)

    @allure.step("Нажать на раздел 'Услуги'")
    def click_services_section(self):
        self.click_element(self.SERVICES_SECTION)

    @allure.step("Нажать на раздел 'Отзывы'")
    def click_reviews_section(self):
        self.click_element(self.REVIEWS_SECTION)

    @allure.step("Проверить URL раздела {section_name}")
    def verify_section_url(self, section_name):
        current_url = self.get_current_url()
        expected_url = self.EXPECTED_URLS.get(section_name)
        assert current_url == expected_url, f"Ожидался URL: {expected_url}, но получен: {current_url}"
        return True

    @allure.step("Проверить наличие всех основных разделов")
    def verify_all_sections_present(self):
        sections = {
            "О нас": self.ABOUT_SECTION,
            "Контакты": self.CONTACTS_SECTION,
            "Вакансии": self.VACANCIES_SECTION,
            "Услуги": self.SERVICES_SECTION,
            "Отзывы": self.REVIEWS_SECTION
        }

        missing_sections = []
        for section_name, locator in sections.items():
            try:
                self.find_element(locator, timeout=5)
            except:
                missing_sections.append(section_name)

        assert len(missing_sections) == 0, f"Не найдены разделы: {missing_sections}"
        return True