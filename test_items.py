#lesson 3_6_10
#запускаем командой pytest --language=es test_items.py
import time
from selenium.webdriver.common.by import By

class TestAddButton:
    def test_button_visibility(self, browser): # для проверки видимости кнопки
        browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
        browser.implicitly_wait(5)
        #time.sleep(30) # для ВИЗУАЛЬНОЙ проверки текста на кнопке 
        assert browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
