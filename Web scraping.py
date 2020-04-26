#!/usr/bin/env python
# coding: utf-8

# In[35]:



from selenium import webdriver
import pandas as pd
from time import sleep
from numpy import nan



driver= webdriver.Chrome('chromedriver')




#code for grtting the column names


driver.get('http://ictcf.biocuckoo.cn/view.php?id=Patient%201')

sleep(5)
cols=[]
tab_data = driver.find_element_by_class_name('array1')
list= [[cell.text for cell in row.find_elements_by_tag_name('td')]
             for row in tab_data.find_elements_by_tag_name('tr')]

for l in list:
    if l[0]:
        cols.append(l[0][:-1])



tab_data = driver.find_element_by_id("Routine_Blood Test")
list= [[cell.text for cell in row.find_elements_by_tag_name('td')]
             for row in tab_data.find_elements_by_tag_name('tr')]

data=[]
d=[]
for l in list:
    if l:
        cols.append(l[0])
        #x=l[2].split(" ")
        #d.append(x[0])
        
tab_data = driver.find_element_by_id("Inflammation")
list= [[cell.text for cell in row.find_elements_by_tag_name('td')]
             for row in tab_data.find_elements_by_tag_name('tr')]

for l in list:
    if l:
        cols.append(l[0])

tab_data = driver.find_element_by_id("Blood_Coagulation Test")
list= [[cell.text for cell in row.find_elements_by_tag_name('td')]
             for row in tab_data.find_elements_by_tag_name('tr')]

for l in list:
    if l:
        cols.append(l[0])

tab_data = driver.find_element_by_id("Biochemical_Test")
list= [[cell.text for cell in row.find_elements_by_tag_name('td')]
             for row in tab_data.find_elements_by_tag_name('tr')]

for l in list:
    if l:
        cols.append(l[0])
        
        
tab_data = driver.find_element_by_id("Immune_Cell Typing")
list= [[cell.text for cell in row.find_elements_by_tag_name('td')]
             for row in tab_data.find_elements_by_tag_name('tr')]

for l in list:
    if l:
        cols.append(l[0])
        
tab_data = driver.find_element_by_id("Cytokine_Profile Test")
list= [[cell.text for cell in row.find_elements_by_tag_name('td')]
             for row in tab_data.find_elements_by_tag_name('tr')]

for l in list:
    if l:
        cols.append(l[0])




#Code for getting data


url='http://ictcf.biocuckoo.cn/view.php?id=Patient%20'
p_id=1
data=[]
for i in range(1170):
    driver.get(url+str(p_id))
    d=[]
    sleep(3)
    
    
    tab_data = driver.find_element_by_class_name('array1')
    list= [[cell.text for cell in row.find_elements_by_tag_name('td')]
                 for row in tab_data.find_elements_by_tag_name('tr')]

    for l in list:
        if l[1]:
            d.append(l[1])
    
    if driver.find_elements_by_xpath('//div[@id="container"]/div[@id="mainContent"]/div[@id="CrossRef"]/div[@id="ref"]/table[@id="Routine_Blood Test"]'):
    
        tab_data = driver.find_element_by_id("Routine_Blood Test")
        list= [[cell.text for cell in row.find_elements_by_tag_name('td')]
                     for row in tab_data.find_elements_by_tag_name('tr')]

    
        for l in list:
            if l:
                #cols.append(l[0])
                x=l[2].split(" ")
                d.append(x[0])
    else:
        for j in range(24):
            d.append(nan)
    if driver.find_elements_by_xpath('//div[@id="container"]/div[@id="mainContent"]/div[@id="CrossRef"]/div[@id="ref"]/table[@id="Inflammation"]'):
    
        tab_data = driver.find_element_by_id("Inflammation")
        list= [[cell.text for cell in row.find_elements_by_tag_name('td')]
                     for row in tab_data.find_elements_by_tag_name('tr')]

        for l in list:
            if l:
                x=l[2].split(" ")
                d.append(x[0])
    else:
        for j in range(3):
            d.append(nan)
    if driver.find_elements_by_xpath('//div[@id="container"]/div[@id="mainContent"]/div[@id="CrossRef"]/div[@id="ref"]/table[@id="Blood_Coagulation Test"]'):
    
        tab_data = driver.find_element_by_id("Blood_Coagulation Test")
        list= [[cell.text for cell in row.find_elements_by_tag_name('td')]
                     for row in tab_data.find_elements_by_tag_name('tr')]

        for l in list:
            if l:
                x=l[2].split(" ")
                d.append(x[0])
    else:
        for j in range(6):
            d.append(nan)
    if driver.find_elements_by_xpath('//div[@id="container"]/div[@id="mainContent"]/div[@id="CrossRef"]/div[@id="ref"]/table[@id="Biochemical_Test"]'):
    
        tab_data = driver.find_element_by_id("Biochemical_Test")
        list= [[cell.text for cell in row.find_elements_by_tag_name('td')]
                     for row in tab_data.find_elements_by_tag_name('tr')]

        for l in list:
            if l:
                x=l[2].split(" ")
                d.append(x[0])
    else:
        for j in range(38):
            d.append(nan)

    if driver.find_elements_by_xpath('//div[@id="container"]/div[@id="mainContent"]/div[@id="CrossRef"]/div[@id="ref"]/table[@id="Immune_Cell Typing"]'):
        tab_data = driver.find_element_by_id("Immune_Cell Typing")
        list= [[cell.text for cell in row.find_elements_by_tag_name('td')]
                     for row in tab_data.find_elements_by_tag_name('tr')]

        for l in list:
            if l:
                x=l[2].split(" ")
                d.append(x[0])
    else:
        for j in range(6):
            d.append(nan)
    if driver.find_elements_by_xpath('//div[@id="container"]/div[@id="mainContent"]/div[@id="CrossRef"]/div[@id="ref"]/table[@id="Cytokine_Profile Test"]'):
    
        tab_data = driver.find_element_by_id("Cytokine_Profile Test")
        list= [[cell.text for cell in row.find_elements_by_tag_name('td')]
                     for row in tab_data.find_elements_by_tag_name('tr')]

        for l in list:
            if l:
                x=l[2].split(" ")
                d.append(x[0])
    else:
        for j in range(6):
            d.append(nan)
            
            
    p_id=p_id+1
    data.append(d)
    


#Convert scraped data to a panda dataframe


df = pd.DataFrame(data, columns = cols) 


#Export the datafram to csv


df.to_csv (r'export_dataframe.csv', index = False, header=True)







