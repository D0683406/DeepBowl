#%%
import re
import pandas as pd
import requests
import lxml
from bs4 import BeautifulSoup
html = requests.get("https://www.coolpc.com.tw/eachview.php?IGrp=5")
soup = BeautifulSoup(html.content,'html5lib')
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
brand_list = []
name_list = []
cpu_type_list = []
size_list = []
display_port_list =[]
storage_list = []
built_in_list = []
network_list = []
warranty_list = []
price_list = []

for i in mb_all:
    temp=i.findAll("div")
    for u in temp:
        if(re.match('CPU：',u.string)):
            cpu_type_list.append(u.string.strip('CPU：'))
        if(re.match('尺寸：',u.string)):
            size_list.append(u.string.strip('尺寸：'))
        if(re.match('顯示：',u.string)):
            display_port_list.append(u.string.strip('顯示：'))
        if(re.match('儲存：',u.string)):
            storage_list.append(u.string.strip('儲存：'))
        if(re.match('內建：',u.string)):
            built_in_list.append(u.string.strip('內建：'))
        if(re.match('網路：',u.string)):
            network_list.append(u.string.strip('網路：'))
        if(re.match('保固：',u.string)):
            warranty_list.append(u.string.strip('保固：'))
    temp=i.findAll("p")
    if  not (re.match('.*Cooling Kit.*',temp[0].string)):
        tempp=re.sub('【.*】',"",temp[0].string)
        brand_list.append(tempp[:2])
        name_list.append(re.search("(.*)\(",tempp[3:]).group(1))
        money=re.search(r"NT\d*",i.get_text())
        price_list.append(money.group().strip("NT"))
table = pd.DataFrame({"brand":brand_list,"name":name_list,"cpu_type":cpu_type_list,"size":size_list,"display_port":display_port_list,"storage":storage_list,"built_in":built_in_list,"network":network_list,"warranty":warranty_list,"price":price_list})
table
table.to_csv('./DATA/mb_list.csv', encoding='utf_8_sig')





        

#%%
test="技嘉 78LMT-USB3 R2(M-ATX/1A1D1H/U3/三年保)*支援最高125W CPU"
xx=re.search("(.*)\(",test[3:])
xx.group(1)


#%%
