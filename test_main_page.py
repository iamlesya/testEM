import pytest
import allure

@allure.epic("Главная страница Effective Mobile")
@allure.feature("Навигация по разделам")
class TestMainPageNavigation:
    @allure.title("Проверка наличия всех основных разделов")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_all_main_sections_present(self, main_page):
        with allure.step("Проверить наличие всех разделов"):
            main_page.verify_all_sections_present()

    @allure.title("Переход в раздел 'О нас'")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_navigate_to_about_section(self, main_page):
        with allure.step("Кликнуть на раздел 'О нас'"):
            main_page.click_about_section()

        with allure.step("Проверить URL раздела"):
            main_page.verify_section_url('about')

    @allure.title("Переход в раздел 'Контакты'")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_navigate_to_contacts_section(self, main_page):
        with allure.step("Кликнуть на раздел 'Контакты'"):
            main_page.click_contacts_section()

        with allure.step("Проверить URL раздела"):
            main_page.verify_section_url('contacts')

    @allure.title("Переход в раздел 'Вакансии'")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_navigate_to_vacancies_section(self, main_page):
        with allure.step("Кликнуть на раздел 'Вакансии'"):
            main_page.click_vacancies_section()

        with allure.step("Проверить URL раздела"):
            main_page.verify_section_url('vacancies')

    @allure.title("Переход в раздел 'Услуги'")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_navigate_to_services_section(self, main_page):
        with allure.step("Кликнуть на раздел 'Услуги'"):
            main_page.click_services_section()

        with allure.step("Проверить URL раздела"):
            main_page.verify_section_url('services')

    @allure.title("Переход в раздел 'Отзывы'")
    @allure.severity(allure.severity_level.NORMAL)
    def test_navigate_to_reviews_section(self, main_page):
        with allure.step("Кликнуть на раздел 'Отзывы'"):
            main_page.click_reviews_section()

        with allure.step("Проверить URL раздела"):
            main_page.verify_section_url('reviews')

    @allure.title("Комплексная проверка навигации по всем разделам")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_comprehensive_navigation(self, main_page):
        sections_to_test = [
            ('about', main_page.click_about_section),
            ('services', main_page.click_services_section),
            ('vacancies', main_page.click_vacancies_section),
            ('reviews', main_page.click_reviews_section),
            ('contacts', main_page.click_contacts_section)
        ]

        for section_name, click_method in sections_to_test:
            with allure.step(f"Тестирование раздела {section_name}"):
                main_page.open()

                click_method()

                main_page.verify_section_url(section_name)