from selenium.webdriver.common.by import By



class ShopPage():
    def __init__(self, driver):
        self.driver = driver

    def getAddItems(self):
        additem = (By.CSS_SELECTOR, "[class*='btn btn-info']")
        return self.driver.find_elements(*additem)

    def getItemTitle(self):
        titles = (By.CSS_SELECTOR, "[class='card-title'] a")
        return self.driver.find_elements(*titles)

    def getCheckOut(self):
        checkout = (By.CSS_SELECTOR, "a[class*='nav-link btn']")
        return self.driver.find_element(*checkout)