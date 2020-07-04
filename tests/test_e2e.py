import pytest
#from conftest import setup
from utility.BaseClass import BaseClass
from pageObject.HomePage import HomePage
from pageObject.ShopPage import ShopPage
from pageObject.CheckOut import CheckOut
import time

#@pytest.mark.usefixtures("setup")
class Test1 (BaseClass):

    def test_e2e(self):
        #driver = setup()
        time.sleep(1)

        homePage = HomePage(self.driver)
        homePage.getName().send_keys("yyyy hhhh")
        homePage.getEmail().send_keys("abcd@qq.com")
        homePage.getPassword().send_keys("12345")
        homePage.getSubmit().click()
        alertMsg = homePage.getSuccMsgs().text
        print ("\n>>>>>>>>>>>>>>>>>>>>> \n")
        print (alertMsg)
        assert ("success" in alertMsg)
        homePage.getShop().click()
        shopPage = ShopPage(self.driver)
        time.sleep(1)

        listitem = shopPage.getItemTitle()
        i = 0
        for item in listitem:
            shopPage.getAddItems()[i].click()
            i = i + 1
        time.sleep(1)

        shopPage.getCheckOut().click()

        checkOut = CheckOut(self.driver)
        checkOut.getCheckOutBut().click()
        time.sleep(0.5)
        checkOut.getCheckbox().click()
        checkOut.getLocation().send_keys("SG")
        time.sleep(0.5)
        checkOut.getPurchase().click()
        time.sleep(2)
        msg = checkOut.getSuccMsg().text
        print (msg)
        print ("\n>>>>>>>>>>>>>>>>>>>>> \n")
        assert ("Success" in msg)


        # self.driver.find_element_by_xpath("//div[@class='form-group']//input[@name='name']").send_keys("yh")
        # self.driver.find_element_by_name("email").send_keys("abcd@gg.com")
        # self.driver.find_element_by_css_selector("input[placeholder='Password']").send_keys("aaaa")
        # self.driver.find_element_by_css_selector("input[type='checkbox']").click()
        # #self.driver.find_
 