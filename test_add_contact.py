# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver

import unittest


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_test_add_contact(self):
        wd = self.wd
        # Login
        self.login(wd, username="admin", password="secret")
        self.add_new_contact(wd, Contacts(first_name="John", last_name="Smith", initials="JS", nickname="Johny",
                                          home_phone="38491123", email="js_smith@yandex.ru"))
        self.logout(wd)

    def test_add_empty_contact(self):
        wd = self.wd
        # Login
        self.login(wd, username="admin", password="secret")
        self.add_new_contact(wd, Contacts(first_name="", last_name="", initials="", nickname="",
                                          home_phone="", email=""))
=======
        self.add_new_contact(wd, "John", "Smith", "JS", "Johny", "38491123", "js_smith@yandex.ru")
>>>>>>> parent of 1a06058... Добавлен класс Contacts и передача его объектов
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def add_new_contact(self, wd, first_name, last_name, initials, nickname, home_phone, email):
        # Init new contact
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(first_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(last_name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(initials)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(nickname)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(home_phone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(email)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def login(self, wd, username, password):
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_id("content").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
