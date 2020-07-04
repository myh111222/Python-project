from selenium.webdriver.common.by import By



class CheckOut():
    def __init__(self, driver):
        self.driver = driver

    def getCheckOutBut(self):
        checkout = (By.CSS_SELECTOR, "[class='btn btn-success']")
        return self.driver.find_element(*checkout)

    def getLocation(self):
        loc = (By.ID, 'country')
        return self.driver.find_element(*loc)

    def getCheckbox(self):
        checkbox = (By.XPATH, '//label[@for="checkbox2"]')
        return self.driver.find_element(*checkbox)

    def getPurchase(self):
        purchase = (By.CSS_SELECTOR, '[class="btn btn-success btn-lg"]')
        return self.driver.find_element(*purchase)

    def getSuccMsg(self):
        msg = (By.XPATH, "//strong[contains(text(),'Success!')]")
        return self.driver.find_element(*msg)

