from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome("./chromedriver.exe")
driver.get("https://www.makemytrip.com/")
time.sleep(2)
driver.find_element_by_xpath("//div[@class='login__card makeFlex hrtlCenter cursorPointer appendBottom10']").click()
#driver.find_element_by_id('yDmH0d').click()
#driver.find_element_by_id('yDmH0d').send_keys("dhamu")
#driver.find_element_by_class_name().send_keys("dhamu")
#driver.find_element_by_id("identifierId").send_keys("dhamu")
#driver.find_element_by_class_name("nyoS7c UzCXuf EIlDfe").send_keys("dhamua459@gmail.com")
#driver.find_element(By.ID,'yDmH0d').send_keys("dhamu")
#driver.find_element(By.CLASS_NAME,"VfPpkd-RLmnJb").click()
#driver.find_element_by_class_name('makeFlex hrtlCenter font10 makeRelative lhUser').click()