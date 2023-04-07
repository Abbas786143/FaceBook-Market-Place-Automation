#!/usr/bin/env python
# coding: utf-8

# In[164]:


import time
import os
import csv
import pyautogui
import pandas as pd
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


# In[165]:


browser = uc.Chrome(use_subprocess=True)
browser.get('https://web.facebook.com')
# implicit wait for 5 seconds
browser.implicitly_wait(5)
# maximize with maximize_window() 
browser.maximize_window()


# In[166]:


username=browser.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input")
username.send_keys("m.qasir786@gmail.com")

pswd=browser.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input")
pswd.send_keys("PAK!@#pak123")

login=browser.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button")
browser.execute_script("arguments[0].click();", login)


# In[169]:


with open('detail.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        a1=str(row[0])
        a2=str(row[1])
        a3=str(row[2])
        a4=str(row[3])
        a5=str(row[4])
        browser.get('https://web.facebook.com/marketplace/create/item')
        time.sleep(5)
        browser.find_element(By.XPATH, "//input[@type='file']").send_keys("E:/new projects of python/facebook market place automation/picture/1.jpg")
        title=browser.find_element(By.XPATH, '*//span[text()="Title"]')
        ActionChains(browser).move_to_element(title).click(title).send_keys('My Title').perform()

        price=browser.find_element(By.XPATH, '*//span[text()="Price"]')
        ActionChains(browser).move_to_element(price).click(price).send_keys('1200').perform()
        
        catogory=browser.find_element(By.XPATH, '*//span[text()="Category"]')
        browser.execute_script("arguments[0].click()", catogory);
        time.sleep(5)
        
        fur=browser.find_element(By.XPATH, '*//span[text()="Furniture"]')
        browser.execute_script("arguments[0].click()", fur);
        time.sleep(5)
        
        condition=browser.find_element(By.XPATH, '*//span[text()="Condition"]')
        browser.execute_script("arguments[0].click()", condition);
        time.sleep(5)
        con=browser.find_element(By.XPATH, '*//span[text()="New"]')
        browser.execute_script("arguments[0].click()", con);
        time.sleep(5)
        
        des=browser.find_element(By.XPATH, '*//span[text()="Description"]')
        ActionChains(browser).move_to_element(des).click(des).send_keys('this is the description of item').perform()
        time.sleep(5)
        
        loc=browser.find_element(By.XPATH, '*//span[text()="Location"]')
        ActionChains(browser).move_to_element(loc).click(loc).send_keys('Multan').perform()
        time.sleep(2)

        pyautogui.press('down')

        time.sleep(2)

        ActionChains(browser).move_to_element(loc).click(loc).send_keys(Keys.ENTER).perform()
        browser.find_element(by=By.XPATH, value="*//span[text()='Next']").click()
        time.sleep(2)
        browser.find_element(by=By.XPATH, value="*//span[text()='Publish']").click()
        time.sleep(20)


# In[ ]:




