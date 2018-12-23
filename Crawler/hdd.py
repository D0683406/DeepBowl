#%%
import re
import pandas as pd
import requests
import lxml
from bs4 import BeautifulSoup
html = requests.get("http://www.coolpc.com.tw/evaluate.php")
soup = BeautifulSoup(html.content,'html5lib')
##擷取完整選項
selects = soup.find_all("select",{"class":"s"})
#選取項目 (3.處理器 CPU 4.主機板 MB 5.記憶體 RAM 6.固態硬碟M.2 SSD 7.傳統內接硬碟HDD 12.電源供應器 PSU)
hdd_all = selects[7].text.split("\n")

#%%
count=0
brand_list=[]
size_list=[]
name_list=[]
cache_list=[]
rpm_list=[]
warranty_list=[]
price_list=[]

#僅留一般用途硬碟
for i in hdd_all[10:48]:
    brand=re.search("Toshiba|Seagate|WD",i).group(0)
    brand_list.append(brand)
    size=re.search("\d{1,2}TB|500G",i).group(0)
    size_list.append(size)
    if not(re.search("【(.*)】",i)):
        name=""
    else:
        name=re.search("【(.*)】",i).group(1)
    name_list.append(name)
    cache=re.search("(\d*)M",i).group(1)
    cache_list.append(cache)
    rpm=re.search("(\d*)轉",i).group(1)
    rpm_list.append(rpm)
    warranty=re.search("(.)(年)",i).group(1)
    if warranty == '三':
        warranty='3'
    if warranty == '四':
        warranty='4'
    if warranty == '五':
        warranty='5'
    warranty_list.append(warranty)
    price=re.search("\$(\d*)",i).group(1)
    price_list.append(price)
print(len(brand_list),len(size_list),len(name_list),len(cache_list),len(rpm_list),len(warranty_list),len(price_list))
table=pd.DataFrame({"brand":brand_list,"size":size_list,"name":name_list,"cache(M)":cache_list,"rpm(轉)":rpm_list,"warranty(years)":warranty_list,"price":price_list})
table.to_csv('./DATA/hdd_list.csv', encoding='utf_8_sig')
#%%
