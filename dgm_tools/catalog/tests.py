import os
import time
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


PATH_DRIVER_CHROME = os.environ.get('PATH_DRIVER_CHROME', '/Users/franciscovaquerociciliano/drivers/chromedriver')
USER_ADMIN_TEST = os.environ.get('USER_ADMIN_TEST') 
PASSWORD_ADMIN_TEST = os.environ.get('PASSWORD_ADMIN_TEST')


# Create your tests here.
class AdminTestCase(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(PATH_DRIVER_CHROME)

    def test_login(self):
        self.driver.get('http://130.211.112.164:8000/catalogo/admin/')
        user_name_field = self.driver.find_element_by_id('id_username')
        password_field = self.driver.find_element_by_id('id_password')
        send_buton = self.driver.find_element_by_css_selector('div.submit-row input')

        self.assertIsNotNone(user_name_field)
        self.assertIsNotNone(password_field)
        self.assertIsNotNone(send_buton)

        self.driver.save_screenshot('/Users/franciscovaquerociciliano/fc-evidence/admin/login_admin_1.png')
        user_name_field.send_keys(USER_ADMIN_TEST)
        password_field.send_keys(PASSWORD_ADMIN_TEST)
        self.driver.save_screenshot('/Users/franciscovaquerociciliano/fc-evidence/admin/login_admin_2.png')
        send_buton.click()

        self.driver.save_screenshot('/Users/franciscovaquerociciliano/fc-evidence/admin/login_admin_3.png')

        self.assertFalse('login' in self.driver.current_url)
        self.driver.quit()

    def test_login_failed(self):
        self.driver.get('http://130.211.112.164:8000/catalogo/admin/')
        user_name_field = self.driver.find_element_by_id('id_username')
        password_field = self.driver.find_element_by_id('id_password')
        send_buton = self.driver.find_element_by_css_selector('div.submit-row input')

        self.assertIsNotNone(user_name_field)
        self.assertIsNotNone(password_field)
        self.assertIsNotNone(send_buton)

        self.driver.save_screenshot('/Users/franciscovaquerociciliano/fc-evidence/admin/login_fail_admin_1.png')
        user_name_field.send_keys('fake_user')
        password_field.send_keys('fake_password')
        self.driver.save_screenshot('/Users/franciscovaquerociciliano/fc-evidence/admin/login_fail_admin_2.png')
        send_buton.click()

        self.driver.save_screenshot('/Users/franciscovaquerociciliano/fc-evidence/admin/login_fail_admin_3.png')

        self.assertTrue('login' in self.driver.current_url)
        self.driver.quit()

    def test_create_entry(self):
        self.driver.get('http://130.211.112.164:8000/catalogo/admin/')
        user_name_field = self.driver.find_element_by_id('id_username')
        password_field = self.driver.find_element_by_id('id_password')
        send_buton = self.driver.find_element_by_css_selector('div.submit-row input')

        self.assertIsNotNone(user_name_field)
        self.assertIsNotNone(password_field)
        self.assertIsNotNone(send_buton)

        # hide_djbar_button = self.driver.find_element_by_css_selector('a#djHideToolBarButton')
        # hide_djbar_button.click()

        self.driver.save_screenshot('/Users/franciscovaquerociciliano/fc-evidence/admin/create_entry_1.png')
        user_name_field.send_keys(USER_ADMIN_TEST)
        password_field.send_keys(PASSWORD_ADMIN_TEST)
        self.driver.save_screenshot('/Users/franciscovaquerociciliano/fc-evidence/admin/create_entry_2.png')
        send_buton.click()

        self.driver.save_screenshot('/Users/franciscovaquerociciliano/fc-evidence/admin/create_entry_3.png')

        self.assertFalse('login' in self.driver.current_url)
        user_name_field = password_field = send_buton = None
        link_entry = self.driver.find_element_by_css_selector('tr.model-post a')
        self.assertIsNotNone(link_entry)
        link_entry.click()

        self.assertTrue('/catalogo/admin/catalog/post/' in self.driver.current_url)
        self.driver.save_screenshot('/Users/franciscovaquerociciliano/fc-evidence/admin/create_entry_4.png')

        link_new = self.driver.find_element_by_css_selector('a.addlink')
        link_new.click()
        self.driver.save_screenshot('/Users/franciscovaquerociciliano/fc-evidence/admin/create_entry_5.png')
        self.assertTrue('/catalogo/admin/catalog/post/add/' in self.driver.current_url)

        mce_close = self.driver.find_element_by_css_selector('.mce-close')
        mce_close.click()

        title_field = self.driver.find_element_by_css_selector('#id_title')
        description_field = self.driver.find_element_by_css_selector('#id_description')
        link_field = self.driver.find_element_by_css_selector('#id_link_external_tool')
        level_field = self.driver.find_element_by_css_selector('#id_level')

        title_field.send_keys('Herramienta de prueba')
        description_field.send_keys('Herramienta de pruebas para qa automatizada')
        link_field.send_keys('https://dominio.com/herramineta/')

        self.driver.quit()

    def test_modify_entry(self):
        self.driver.get('http://130.211.112.164:8000/catalogo/admin/')
        user_name_field = self.driver.find_element_by_id('id_username')
        password_field = self.driver.find_element_by_id('id_password')
        send_buton = self.driver.find_element_by_css_selector('div.submit-row input')

        self.assertIsNotNone(user_name_field)
        self.assertIsNotNone(password_field)
        self.assertIsNotNone(send_buton)

        # hide_djbar_button = self.driver.find_element_by_css_selector('a#djHideToolBarButton')
        # hide_djbar_button.click()

        self.driver.save_screenshot('/Users/franciscovaquerociciliano/fc-evidence/admin/modify_entry_1.png')
        user_name_field.send_keys(USER_ADMIN_TEST)
        password_field.send_keys(PASSWORD_ADMIN_TEST)
        self.driver.save_screenshot('/Users/franciscovaquerociciliano/fc-evidence/admin/modify_entry_2.png')
        send_buton.click()

        self.driver.save_screenshot('/Users/franciscovaquerociciliano/fc-evidence/admin/modify_entry_3.png')

        self.assertFalse('login' in self.driver.current_url)
        user_name_field = password_field = send_buton = None
        link_entry = self.driver.find_element_by_css_selector('tr.model-post a')
        self.assertIsNotNone(link_entry)
        link_entry.click()

        self.assertTrue('/catalogo/admin/catalog/post/' in self.driver.current_url)
        self.driver.save_screenshot('/Users/franciscovaquerociciliano/fc-evidence/admin/modify_entry_4.png')

    def test_delete_entry(self):
        self.driver.get('http://130.211.112.164:8000/catalogo/admin/')
        user_name_field = self.driver.find_element_by_id('id_username')
        password_field = self.driver.find_element_by_id('id_password')
        send_buton = self.driver.find_element_by_css_selector('div.submit-row input')

        self.assertIsNotNone(user_name_field)
        self.assertIsNotNone(password_field)
        self.assertIsNotNone(send_buton)

        # hide_djbar_button = self.driver.find_element_by_css_selector('a#djHideToolBarButton')
        # hide_djbar_button.click()

        self.driver.save_screenshot('/Users/franciscovaquerociciliano/fc-evidence/admin/delete_entry_1.png')
        user_name_field.send_keys(USER_ADMIN_TEST)
        password_field.send_keys(PASSWORD_ADMIN_TEST)
        self.driver.save_screenshot('/Users/franciscovaquerociciliano/fc-evidence/admin/delete_entry_2.png')
        send_buton.click()

        self.driver.save_screenshot('/Users/franciscovaquerociciliano/fc-evidence/admin/delete_entry_3.png')

        self.assertFalse('login' in self.driver.current_url)
        user_name_field = password_field = send_buton = None

    def _wait_browser(self, driver, time=50, until=(By.NAME, 'year')):
        try:
            element = WebDriverWait(driver, time).until(
                EC.presence_of_element_located(until)
            )
        except:
            # driver.close()
            return False

        return True


class UserTestCase(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(PATH_DRIVER_CHROME)
    def setup_databases(self, **kwargs):
        """ Override the database creation defined in parent class """
        pass

    def teardown_databases(self, old_config, **kwargs):
        """ Override the database teardown defined in parent class """
        pass

    def test_entry_list(self):
        self.driver.get('http://130.211.112.164:8000/catalogo/')
        # hide_djbar_button = self.driver.find_element_by_css_selector('a#djHideToolBarButton')
        # hide_djbar_button.click()
        self.driver.save_screenshot('/Users/franciscovaquerociciliano/fc-evidence/user/list_entry_1.png')
        self.driver.execute_script("scroll(0, 450);")
        self.driver.save_screenshot('/Users/franciscovaquerociciliano/fc-evidence/user/list_entry_2.png')
        self.driver.quit()

    def test_filter_entry_list(self):
        self.driver.get('http://130.211.112.164:8000/catalogo/')
        # hide_djbar_button = self.driver.find_element_by_css_selector('a#djHideToolBarButton')
        # hide_djbar_button.click()
        self.driver.save_screenshot('/Users/franciscovaquerociciliano/fc-evidence/user/filter_entry_1.png')
        self.driver.execute_script("scroll(0, 450);")
        self.driver.save_screenshot('/Users/franciscovaquerociciliano/fc-evidence/user/filter_entry_2.png')
        title_field = self.driver.find_element_by_css_selector('#titulo-herramienta')
        title_field.send_keys("prueba")
        self.driver.save_screenshot('/Users/franciscovaquerociciliano/fc-evidence/user/filter_entry_3.png')
        title_field.send_keys(Keys.ENTER)
        self.driver.execute_script("scroll(0, 1750);")
        self.driver.save_screenshot('/Users/franciscovaquerociciliano/fc-evidence/user/filter_entry_4.png')
        self.driver.quit()

    def test_view_single_entry(self):
        self.driver.get('http://130.211.112.164:8000/catalogo/')
        # hide_djbar_button = self.driver.find_element_by_css_selector('a#djHideToolBarButton')
        # hide_djbar_button.click()
        self.driver.save_screenshot('/Users/franciscovaquerociciliano/fc-evidence/user/single_entry_1.png')
        self.driver.execute_script("scroll(0, 450);")
        self.driver.save_screenshot('/Users/franciscovaquerociciliano/fc-evidence/user/single_entry_2.png')
        title_field = self.driver.find_element_by_css_selector('#titulo-herramienta')
        title_field.send_keys("prueba")
        self.driver.save_screenshot('/Users/franciscovaquerociciliano/fc-evidence/user/single_entry_3.png')
        title_field.send_keys(Keys.ENTER)
        self.driver.execute_script("scroll(0, 1750);")
        self.driver.save_screenshot('/Users/franciscovaquerociciliano/fc-evidence/user/single_entry_4.png')

        posts = self.driver.find_elements_by_css_selector('.api-posts .post-item')
        posts[1].find_element_by_css_selector('.post-info h3 a').click()
        self.driver.save_screenshot('/Users/franciscovaquerociciliano/fc-evidence/user/single_entry_5.png')
        self.driver.quit()