import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


link1 = "https://www.phptravels.net/"
link2 = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
link3 = "https://formy-project.herokuapp.com/"
link4 = "https://the-internet.herokuapp.com/"
link5 = "https://www.techlistic.com/p/selenium-practice-form.html"
link6 = "jules.app"
link7 = "https://magento.softwaretestingboard.com/"

# driver.get(link1)
# driver.maximize_window()
#
# link_by_id = driver.find_element(By.ID, "ACCOUNT")
# link_by_id.click()
# time.sleep(3)
#
# link_by_id = driver.find_element(By.ID, "currency")
# link_by_id.click()
# time.sleep(3)
#
# link_by_id = driver.find_element(By.ID, "checkin")
# link_by_id.click()
# time.sleep(3)

# driver.get(link3)
# driver.maximize_window()
# #
# link_by_link_text = driver.find_element(By.LINK_TEXT, "Enabled and disabled elements")
# time.sleep(3)
# link_by_link_text.click()
# time.sleep(3)
# driver.back()
# time.sleep(3)

# link_by_partial_link_text = driver.find_element(By.PARTIAL_LINK_TEXT, "Complete")
# time.sleep(3)
# link_by_partial_link_text.click()
# time.sleep(3)
# driver.back()
# time.sleep(3)

# driver.get(link2)
# driver.maximize_window()
# # link_by_name = driver.find_element(By.NAME, "username")
# # link_by_name.click()
# # time.sleep()
# # driver.back()
# # time.sleep()
# link_by_tag = driver.find_element(By.TAG_NAME, "input")
# link_by_class_name = driver.find_element((By.CLASS_NAME, 'orangehrm-login-forgot'))

driver.get(link7)
driver.maximize_window()
link_by_css_id = driver.find_element(By.CSS_SELECTOR, "input[id='search']")
time.sleep(3)
link_by_css_id.click()
time.sleep(3)






