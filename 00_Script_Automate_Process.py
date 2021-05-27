# -*- coding: utf-8 -*-
#
#
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.command import Command
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

#"""
#from instapy import InstaPy
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time
import os
import requests
import random
import datetime as dt
import codecs

from func import get_proxies,bs_request,Get_Url,WebShare_Proxies
####################################################################################
df_proxies=WebShare_Proxies()
####################################################################################
lst_countries=['Germany','France','Italy','Norway','United States','South Africa','Austria',
'Poland','Spain','Romania','Egypt','Serbia','Denmark','Sweden','Hungary','Turkey','Nigeria',
'Netherlands','Ireland','Albania','Croatia','Portugal','Brazil','Lithuania','Bosnia and Herzegovina',
'Switzerland','Europe','Malaysia','Qatar','Canada']
mode=3

df_proxies_2=get_proxies(lst_countries,mode)
df_proxies_3=df_proxies_2.iloc[:25]
args=df_proxies_3.values[random.choice(df_proxies.index)].tolist()
"""
myproxies=df_proxies.iloc[:30]['Proxy'].tolist()
print('Proxies of len:',len(myproxies))
proxy=random.choice(myproxies)
"""

####################################################################################
print('Initializing Profile...\n')
print('-----------------------------------------------------------------')
#SELENIUM ENTRIES
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = True
cap['acceptInsecureCerts'] = True
binary = FirefoxBinary('/usr/bin/firefox')
##
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
#options.add_argument('--load-images=no')
#options.add_argument("window-size=1400,600")
#options.add_argument('--ignore-certificate-errors')
#options.add_argument('--proxy-server=%s' % proxy)
##
profile = webdriver.FirefoxProfile()
#profile.set_preference("general.useragent.override", "[user-agent string]")
profile.set_preference("general.useragent.override", 
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:63.0) Gecko/20100101 Firefox/63.0")
####################################################################################
url='https://www.wizcase.com/tools/whats-my-ip/'
####################################################################################
##BS TEST PROXY
header = {'user-agent': 
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0'}
args,r,df_proxies_3=bs_request(header,url,df_proxies_3,args)

####################################################################################

url='https://www.fastmail.com/signup/'

driver = webdriver.Firefox(profile,options = options,capabilities=cap,firefox_binary=binary)


name_input=driver.find_element_by_id('name')
mail_input=driver.find_element_by_id('email-localpart')
password_input=driver.find_element_by_id('password')
#
#NAME EMAIL PASSWORD
name_input.send_keys("John Smithh")
mail_input.send_keys('John_Smith3456')
password_input.send_keys('GogoKaJa@/1')

#AGREE BUTTON
check_box=driver.find_element_by_id("tos")

check_box.click()

#SUBMIT BUTTON
submit_button=driver.find_element_by_xpath("//button[@type='submit']")
submit_button.click()
#
#
#
#
#
#
#
#
#
