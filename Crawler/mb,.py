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
mb_all = selects[4].text.split("\n")
#去除非消費級主機板
mb_all=mb_all[46:]
 
#%%

#去除不需要選項
while '' in mb_all:
    mb_all.remove('')
for i in mb_all:
    if '❤' in i:
        mb_all.remove(i)
count=0
for i in mb_all:    
    i=i.strip('【推薦】')
    i=i.strip('超值】')
    i=i.strip('優惠】')
    i=i.replace('◆','')
    i=i.replace('★','')
    i=i.replace('熱賣','')
    i=re.sub('↓.*↓','',i)
    i=re.sub('\$.*↘','',i)
    mb_all[count]=i
    count+=1
countt=0
for i in mb_all:
    print(str(countt)+'.'+i)
    countt+=1


#%%
for i in mb_all: 
    brand_list = []
    name_list = []
    type_list=[]
    


#%%
