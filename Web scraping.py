#!/usr/bin/env python
# coding: utf-8





from selenium import webdriver
import pandas as pd
from time import sleep
from numpy import nan



driver= webdriver.Chrome('chromedriver')




#code for grtting the column names


driver.get('http://ictcf.biocuckoo.cn/view.php?id=Patient%201')

col=[]
tab_data = driver.find_element_by_class_name('array1')
list= [[cell.text for cell in row.find_elements_by_tag_name('td')]
             for row in tab_data.find_elements_by_tag_name('tr')]

for l in list:
    if l[0]:
        col.append(l[0][:-1])

url='http://ictcf.biocuckoo.cn/view.php?id=Patient%20'
p_id=1
for i in range(1170):
    driver.get(url+str(p_id))
    sleep(1)
    tab_data = driver.find_element_by_xpath('//div[@id="container"]/div[@id="mainContent"]/div[@id="CrossRef"]/div[@id="ref"]')
    list= [[cell.text for cell in row.find_elements_by_tag_name('td')]
             for row in tab_data.find_elements_by_tag_name('tr')]
    #print(list)
    for l in list:
        if l:
            if l[0] not in col:
                col.append(l[0])
    p_id=p_id+1
len(col)        

#Code for getting data
data={}
for c in col:
    data[c]=[]
    
url='http://ictcf.biocuckoo.cn/view.php?id=Patient%20'
p_id=1
for i in range(1170):
    driver.get(url+str(p_id))
    sleep(1)
    tab_data = driver.find_element_by_class_name('array1')
    list= [[cell.text for cell in row.find_elements_by_tag_name('td')]
                 for row in tab_data.find_elements_by_tag_name('tr')]

    
    for l in list:
        if l[0]:
            data[l[0][:-1]].append(l[1])
    tab_data = driver.find_element_by_xpath('//div[@id="container"]/div[@id="mainContent"]/div[@id="CrossRef"]/div[@id="ref"]')
    list= [[cell.text for cell in row.find_elements_by_tag_name('td')]
             for row in tab_data.find_elements_by_tag_name('tr')]
    #print(list)
    for l in list:
        if l:
            x=l[2].split(" ")
            data[l[0]].append(x[0])
    for c in col:
        if len(data[c])< len(data["Age"]):
            data[c].append(nan)
    p_id=p_id+1


#Convert scraped data to a panda dataframe


df = pd.DataFrame(data)



#Export the datafram to csv


df.to_csv(r'Dataset.csv', index = False)







