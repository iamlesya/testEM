from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
import allure
import time


class MainPage(BasePage):
    ABOUT_SECTION = (By.XPATH, "//a[contains(text(), 'О нас')]")
    CONTACTS_SECTION = (By.XPATH, "//a[contains(text(), 'Контакты')]")
    VACANCIES_SECTION = (By.XPATH, "//a[contains(text(), 'Вакансии')]")
    SERVICES_SECTION = (By.XPATH, "//a[contains(text(), 'Услуги') or contains(text(), 'Аутстафф')]")
    REVIEWS_SECTION = (By.XPATH, "//a[contains(text(), 'Отзывы')]")

    BASE_URL = "https://www.effective-mobile.ru"

    @allure.step("Открыть главную страницу")
    def open(self):
        self.go_to_url(self.BASE_URL)
        # Ждем загрузки страницы
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    @allure.step("Нажать на раздел 'О нас'")
    def click_about_section(self):
        self._click_with_wait(self.ABOUT_SECTION)

    @allure.step("Нажать на раздел 'Контакты'")
    def click_contacts_section(self):
        self._click_with_wait(self.CONTACTS_SECTION)

    @allure.step("Нажать на раздел 'Вакансии'")
    def click_vacancies_section(self):
        self._click_with_wait(self.VACANCIES_SECTION)

    @allure.step("Нажать на раздел 'Услуги'")
    def click_services_section(self):
        self._click_with_wait(self.SERVICES_SECTION)

    @allure.step("Нажать на раздел 'Отзывы'")
    def click_reviews_section(self):
        self._click_with_wait(self.REVIEWS_SECTION)

    def _click_with_wait(self, locator):
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(locator)
            )
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            time.sleep(1)
            element.click()
            time.sleep(2)
        except Exception as e:
            self.driver.save_screenshot(f"error_{locator[1]}.png")
            raise e

    @allure.step("Проверить URL раздела {section_name}")
    def verify_section_url(self, section_name):
        time.sleep(3)
        current_url = self.get_current_url()

        expected_patterns = [
            f"{self.BASE_URL}/#{section_name}",
            f"{self.BASE_URL}/#/{section_name}",
            f"{self.BASE_URL}/{section_name}"
        ]

        for pattern in expected_patterns:
            if pattern in current_url:
                return True

        section_keywords = {
            'about': ['about', 'о-нас'],
            'contacts': ['contact', 'контакты'],
            'vacancies': ['vacancies', 'вакансии', 'specializations'],
            'services': ['services', 'услуги'],
            'reviews': ['reviews', 'отзывы', 'testimonials']
        }

        keywords = section_keywords.get(section_name, [])
        for keyword in keywords:
            if keyword in current_url.lower():
                return True

        allure.attach(f"Текущий URL: {current_url}", name="Current URL")
        assert False, f"URL не соответствует ожидаемому для раздела '{section_name}'. Текущий URL: {current_url}"

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
                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(locator)
                )
                # Проверим, что элемент видим
                if not element.is_displayed():
                    missing_sections.append(f"{section_name} (не видим)")
            except:
                missing_sections.append(section_name)

        assert len(missing_sections) == 0, f"Не найдены разделы: {missing_sections}"
        return True