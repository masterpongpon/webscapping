#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install selenium')


# In[3]:


from selenium import webdriver


# In[6]:


driver = webdriver.Edge(executable_path='C:\\Users\\MIzP\\Downloads\\work\\msedgedriver.exe')


# In[7]:


driver.get('https://shopee.co.th/')


# In[8]:


driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/div[3]/div[1]/button').click()


# In[13]:


driver.execute_script('return document.querySelector("shopee-banner-popup-stateful").shadowRoot.querySelector("div.shopee-popup__close-btn")').click()


# In[25]:


search =  driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/form/input')


# In[27]:


search.send_keys("เซรั่มแก้ฝ้า")


# In[28]:


from selenium.webdriver.common.keys import Keys


# In[30]:


search.send_keys(Keys.ENTER)


# In[38]:


driver.execute_script("document.body.style.zoom='100%' ")


# In[33]:


data = driver.page_source


# In[34]:


get_ipython().system('pip install bs4')


# In[35]:


import bs4


# In[36]:


soup = bs4.BeautifulSoup(data)


# In[52]:


all_product = soup.find_all('div',{'class':'_10Wbs- _2STCsK _3IqNCf'})


# In[53]:


all_product_list = []
for product in all_product:
    all_product_list.append(product.text)
all_product_list
    


# In[58]:


all_price = soup.find_all('div',{'class':'zp9xm9 kNGSLn l-u0xK'})


# In[59]:


all_price_list = []
for price in all_price:
    all_price_list.append(price.text)
all_price_list


# In[60]:


all_sales = soup.find_all('div',{'class':'_1uq9fs'})


# In[61]:


all_sales_list = []
for sales in all_sales:
    all_sales_list.append(sales.text)
all_sales_list


# In[64]:


get_ipython().system('pip install pandas')


# In[65]:


import pandas as pd


# In[87]:


shopee_data = pd.DataFrame([all_product_list,all_price_list,all_sales_list])


# In[88]:


shopee_data = shopee_data.transpose()
shopee_data.columns = ['Name','Price','Amount']


# In[91]:


shopee_data.to_excel(r'C:\Users\MIzP\Downloads\work\shopee_เซรั่มแก้ฝ้า.xlsx')

