import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="/Users/eric/Documents/code/Py_selenium/chromedriver")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    
    #return driver

    

