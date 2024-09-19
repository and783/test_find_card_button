import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_find_card_button(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(30)
        button = browser.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
        assert button, "Add to card button is not present"
       
        
      
        

