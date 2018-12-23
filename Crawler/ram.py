#%%
import re
import pandas as pd
import requests
import lxml
from bs4 import BeautifulSoup
html = requests.get("https://www.coolpc.com.tw/eachview.php?IGrp=6")
soup = BeautifulSoup(html.content,'html5lib')
soup
#%%
ram_all = soup.find_all("span")
countt=0
#前220筆為桌上型記憶體
ram_all=ram_all[:220]

#%% 秀資料方塊
for i in ram_all:
    str(i).strip("\"")
    print(countt)
    print(i)
    print('\n\n\n')
    countt+=1

#%%
brand_list=[]
size_list=[]
type_list=[]
frequency_list=[]
name_list = []
price_list=[]
for i in ram_all:
    temp=i.findAll("p")
    for u in temp:
        if not (re.match('含稅價：',u.get_text())):
            #廠牌
            brand=re.search("KLEVV\(科賦\)|芝奇 G\.SKILL|芝奇G\.SKILL|CORSAIR|UMAX|威剛|金士頓|V-color全何|V-color|美光 Micron|技嘉 AORUS",u.get_text()).group(0)
            brand_list.append(brand)
            #大小
            size=re.search("\d{1,2}GB\*2|\d{1,2}GB|\d{1,2}G",u.get_text()).group(0)
            if size=='2G':
                size='2GB'
            if size=='4G':
                size='4GB'
            if size=='8G':
                size='8GB'
            if size=='16G':
                size='16GB'
            size_list.append(size)
            #DDR幾
            type=re.search("DDR4|DDR3|D4|DDR|DDR2",u.get_text()).group(0)
            if type=="D4":
                type="DDR4"
            type_list.append(type)
            #頻率
            frequency=re.search("\d{4}|\d{3}",u.get_text()).group(0)
            frequency_list.append(frequency)
            #全名
            name_list.append(u.get_text())
            #價錢
    price=re.search("NT\d*",i.get_text()).group(0)
    price_list.append(price.strip('NT'))

table = pd.DataFrame({"brand":brand_list,"size":size_list,"type":type_list,"frequency":frequency_list,"name":name_list,"price":price_list})
table.to_csv('./DATA/ram_list.csv', encoding='utf_8_sig')
                



            
        







#%%
