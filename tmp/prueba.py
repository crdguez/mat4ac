from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.manager.showAlertOnComplete", False)
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/html")
fp.set_preference("browser.download.dir", os.getcwd())

driver = webdriver.Firefox(firefox_profile=fp)
driver.get("https://servicios.aragon.es/sigad-academica")
assert "Login" in driver.title
elem = driver.find_element_by_class_name('v-textfield')
elem.clear()
elem.send_keys("RODRIGUEZ.CARLOS20")
elem.send_keys(Keys.TAB)
elem2 = driver.switch_to_active_element()
elem2.send_keys("es3")
elem3 = driver.find_element_by_class_name('botonTexto')
elem3.click()
elem4 = driver.find_elements_by_class_name('v-caption')
elem4[6].click()
elem5 = driver.find_elements_by_class_name('v-icon')
elem5[15].click()
elem6 = driver.find_element_by_xpath("//div[@id='sigadacademica-1339463174']/div/div[2]/div/div/div[3]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div[3]/div/table/tbody/tr[22]/td/div")
elem6.click()
elem7 = driver.find_element_by_xpath("//div[@id='sigadacademica-1339463174']/div/div[2]/div/div/div[3]/div/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[4]/div/div/span/img")
elem7.click()
elem8 = driver.find_element_by_xpath("(//input[@type='text'])[10]")
elem8.click()
elem8.send_keys(Keys.ARROW_DOWN)
for i in range(11) :
        elem8.send_keys(Keys.ARROW_DOWN)

elem8.send_keys(Keys.RETURN)
elem8 = driver.find_element_by_xpath("(//input[@type='text'])[11]")
elem8.click()
elem8.send_keys(Keys.ARROW_DOWN)
for i in range(5) :
        elem8.send_keys(Keys.ARROW_DOWN)

elem8.send_keys(Keys.RETURN)
for i in range(1) :
        elem8.send_keys(Keys.ARROW_DOWN)

elem8.send_keys(Keys.RETURN)
elem8 = driver.find_element_by_xpath("(//input[@type='text'])[14]")
elem8.click()
elem8.send_keys(Keys.ARROW_DOWN)
for i in range(1) :
        elem8.send_keys(Keys.ARROW_DOWN)

elem8.send_keys(Keys.RETURN)
elem9 = driver.find_element_by_xpath("//div[3]/div/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[4]/div/div/span")
elem9.click()
elem10 = driver.find_element_by_xpath("(//input[@type='text'])[15]")
elem10.click()
elem10.send_keys(Keys.ARROW_DOWN)
for i in range(6) :
        elem10.send_keys(Keys.ARROW_DOWN)

elem10.send_keys(Keys.RETURN)
elem11 = driver.find_element_by_xpath("//div[3]/div/div/div/div[2]/div/div/div/div[2]/div/div/span/span")
elem11.click()
driver.close()
