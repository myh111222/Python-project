from selenium.webdriver.common.by import By



class HomePage():
    def __init__(self, driver):
        self.driver = driver

    def GetObject(self, method, locator):
        name = (method, locator)
        return self.driver.find_element(*name)

    def HomePageObject(self):
        self.GetObject(By.XPATH, "//div[@class='form-group']//input[@name='name']")


    def getName(self):
        name = (By.XPATH, "//div[@class='form-group']//input[@name='name']")
        return self.driver.find_element(*name)

    def getEmail(self):
        email = (By.NAME, "email")
        return self.driver.find_element(*email)

    def getPassword(self):
        paswd = (By.CSS_SELECTOR, "input[placeholder='Password']")
        return self.driver.find_element(*paswd)
    
    def getCheck(self):
        check = (By.CSS_SELECTOR, "input[type='checkbox']")
        return self.driver.find_element(*check)

    def getGender(self):
        gender = (By.ID, "exampleFormControlSelect1")
        return self.driver.find_element(*gender)

    def getSubmit(self):
        sub = (By.XPATH, "//input[@value='Submit']")
        return self.driver.find_element(*sub)

    def getSuccMsgs(self):
        succMsg = (By.CSS_SELECTOR, "[class*='alert-success']")
        return self.driver.find_element(*succMsg)

    def getShop(self):
        shop = (By.CSS_SELECTOR,"a[href*='shop']")
        return self.driver.find_element(*shop)