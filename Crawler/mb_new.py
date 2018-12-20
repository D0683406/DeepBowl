#%%
import re
import pandas as pd
import requests
import lxml
from bs4 import BeautifulSoup
html = requests.get("https://www.coolpc.com.tw/eachview.php?IGrp=5")
soup = BeautifulSoup(html.content,'html5lib')
soup
#%%
mb_all = soup.find_all("span")
countt=0
mb_all=mb_all[32:]

for i in mb_all:
    str(i).strip("\"")
    print(countt)
    print(i)
    print('\n\n\n')
    countt+=1
#%%
cpu_type_list = []
size_list = []
display_port_list =[]
storage_list = []
built_in_list = []
network_list = []
warranty_list = []
price = []

cpu_pattern='CPU：.*<'

location=0
for i in mb_all:
    print(re.findall(cpu_pattern,i))



#%%
print(re.findall(cpu_pattern,i))

#%%
a="img src"
temp=a.find_all("i")
temp




#%%
