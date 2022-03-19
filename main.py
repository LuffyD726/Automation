from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import PyQt5
from PyQt5 import QtGui, QtWidgets, Qt5
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys


s = Service("C:\Program Files (x86)\chromedriver.exe")
URL = input("pls enter the URL \n")

while len(URL) < 10:
    print("please make sure that's the right URL")
    URL = input("please enter the URL \n")
else:
    Before = "https://www."
    ExtraURL = Before + URL
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(service=s)
# https://get-in.com/160093?seller_code=EidW7EJvy6G

first_names = "שהם", "אורי", "רון","מאי"
last_names = "ברוק", "מלכה", "רוזנר","ברהום"
phone_nums = "0524206836", "0535247588", "0508765442","0505612385"
emails = "shoambruk@gmail.com", "orimalka113@gmail.com","rozner95@gmail.com","maybr1744@gmail.com"

for x in range(len(first_names)):
    driver.get(URL)
    time.sleep(8)
    first_name = driver.find_element(By.ID, 'first_name')
    first_name.send_keys(first_names[x])

    last_name = driver.find_element(By.ID, 'last_name')
    last_name.send_keys(last_names[x])

    phone_num = driver.find_element(By.ID, 'user_phone')
    phone_num.send_keys(phone_nums[x])

    email = driver.find_element(By.ID, 'user_email')
    email.send_keys(emails[x])

    age = driver.find_element(By.ID, 'age')
    age.send_keys("20")

    gander = driver.find_element(By.ID, 'gender_dummy')
    gander.click()
    time.sleep(5)

time.sleep(15)
driver.quit()
