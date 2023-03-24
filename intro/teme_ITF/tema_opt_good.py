# import time
# from telnetlib import EC
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait


# # Exerciții obligatorii - grad de dificultate: Usor spre Mediu
# # Alege-ți unuul sau mai multe din sugestiile de site-uri de mai jos
# # - https://www.phptravels.net/
# # - http://automationpractice.com/index.php
# # - https://formy-project.herokuapp.com/
# # - https://the-internet.herokuapp.com/
# # - https://www.techlistic.com/p/selenium-practice-form.html
# # - jules.app
#
# driver = webdriver.Chrome()
# LINK = "https://www.techlistic.com/p/selenium-practice-form.html"
# driver.get(LINK)
# driver.maximize_window()
# time.sleep(1)
#
# # Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
# # ● Id
#
# # //input[@id="profession-0"]
# # //*[@id="profession-1"]
# # #tool-0
#
#
# # ● Link text
#
# link_text = driver.find_element(By.LINK_TEXT, "Click here to Download File")
# link_text = driver.find_element(By.LINK_TEXT, "Automate Amazon like E-Commerce website with Selenium")
# link_text = driver.find_element(By.LINK_TEXT, "Automate Handling Multiple Browser Tabs with Seleniume")
#
# # ● Parțial link text
#
# link_text = driver.find_element(By.LINK_TEXT, "Click here")
# link_text = driver.find_element(By.LINK_TEXT, "Automate Amazon")
# link_text = driver.find_element(By.LINK_TEXT, "Automate Handling")
#
# # ● Name
#
# link_name = driver.find_element(By.NAME, "firstname")
# link_name = driver.find_element(By.NAME, "lastname")
# link_name = driver.find_element(By.NAME, "continents")
#
# # ● Tag*
#
# tag_name = driver.find_element(By.TAG_NAME, 'input')
# tag_name = driver.find_element(By.TAG_NAME, 'link')
# tag_name = driver.find_element(By.TAG_NAME, 'script')
#
# # ● Class name*
#
# clas_name = driver.find_element(By.CLASS_NAME, "dropbtn")
# clas_name = driver.find_element(By.CLASS_NAME, "input-xlarge")
# clas_name = driver.find_element(By.CLASS_NAME, "btn btn-info")
#
# # ● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)
#
# #sex-0
# .controls
# //input[contains(@id, 'exp-3')]
#
# # Pentru xpath identifică elemente după criteriile de mai jos:
#
# # ● 3 după atribut valoare
#
# //*[@id='photo']
# //*[@name='photo']
# //*[@name='continents']
#
# # ● 3 după textul de pe element
#
# //span[text()='Profession']
# //label[text()=' Automation Tester']
# //span[text()='Selenium Commands']
#
# # ● 1 după parțial text
#
# //a[contains(text(), 'Click here')]
#
# # ● 1 cu SAU, folosind pipe |
#
# //input[@name='firstname'] | //input[@name='lastname']
#
# # ● 1 cu *
#
# //*[@name='firstname']
#
# # ● 1 în care le iei ca pe o listă de xpath și în python ajunge 1 element, deci
# # cu (xpath)[1]
#
# //div//div[3][@class][1]
#
# # ● 1 în care să folosești parent::
#
# //input[@name='firstname']/parent::*
#
# # ● 1 în care să folosești fratele anterior sau de după (la alegere)
#
# //div/div[@class]/*[2]/following-sibbling::*
#
# # ● 1 funcție ca și cea de la clasă prin care să pot alege eu prin parametru cu
# # ce element vreau să interacționez.
#
#
# # Exerciții extra - Opțional
# # https://www.automatetheplanet.com/most-exhaustive-xpath-locators-cheat-sh
# # eet/