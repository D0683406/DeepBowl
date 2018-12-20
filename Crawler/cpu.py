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


#%%

#選取項目 (3.處理器 CPU 4.主機板 MB 5.記憶體 RAM 6.固態硬碟M.2 SSD 7.傳統內接硬碟HDD 12.電源供應器 PSU)
cpu_all = selects[3].text.split("\n")

# 把空字串去掉
while '' in cpu_all:
    cpu_all.remove('')
# 去掉不需要的選項
for i in cpu_all:
    if ',' not in i:
        cpu_all.remove(i)
count=0
for i in cpu_all:    
    i=i.strip('◆ ★')
    i=i.strip('◆ ★ 熱賣')
    i=re.sub(r'\*[^,]*\,',' ',i)
    i=re.sub(r'限量送[^,]*\,',' ',i)
    i=re.sub(r'搭板[^,]*\,',' ',i)
    cpu_all[count]=i
    count+=1

#%%
brand_list = []
name_list = []
core_list =[]
price_list = []
speed_list=[]
for i in cpu_all:
    #分割前面的廠牌與型號
    temp = i.split('【')
    temp = temp[0].split(' ',1)
    brand_list.append(temp[0])
    name_list.append(temp[1])
    #取最後的價錢
    temp = i.split('$')
    price_list.append(temp[-1])
    #core
    temp=re.findall('【[^】]*】',i)
    core_list.append(temp[0])
    #speed
    temp=re.findall(r'】[^/]*/',i)
    #speed_list.append(temp[0])
    
    
table = pd.DataFrame({"brand":brand_list,"name":name_list,"core":core_list,"price":price_list})
table.to_csv('./DATA/cpu_list.csv', encoding='utf_8_sig')


#%%
