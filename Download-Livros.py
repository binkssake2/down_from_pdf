#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import PyPDF2
import re

import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


# In[ ]:


pdfFileObj = open(r"C:\Users\binks\Springer Ebooks.pdf.pdf", 'rb')


# In[ ]:


pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 


# In[ ]:


link_livros = []
for i in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(i)
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', pageObj.extractText())
    link_livros.extend(urls)


# In[ ]:


download_dir = r"C:\Users\binks\Desktop\LIVROS_DONW"
options = webdriver.ChromeOptions()

chrome_options = Options()
chrome_options.add_experimental_option('prefs',  {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
    }
)

for link in link_livros:
    chromedriver = r"C:\Users\binks\Desktop\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver, options=chrome_options)
    driver.get(link)
    sleep(8)
    driver.execute_script("window.scrollTo(0, 250)") 
    try:    
        botao = driver.find_element_by_xpath('//*[@id="main-content"]/article[1]/div/div/div[2]/div/div')
    except:
        botao = driver.find_element_by_xpath('//*[@id="main-content"]/article[1]/div/div/div[2]/div[1]/a')
    botao.click()
    sleep(60)
    driver.close()


# In[ ]:




