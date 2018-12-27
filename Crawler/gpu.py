#%%
import re
import pandas as pd
import requests
import lxml
from bs4 import BeautifulSoup
html = requests.get("https://www.coolpc.com.tw/eachview.php?IGrp=12")
soup = BeautifulSoup(html.content,'html5lib')
gpu_all = soup.find_all("span")


#%%
brand_list=[]
name_list=[]
core_list=[]
clock_list=[]
cuda_sp_list=[]
video_interface_list=[]
power_interface_list=[]
length_list=[]
warranty_list = []
memory_list =[]
price_list=[]
fullname=[]
for i in gpu_all[27:-12]:
    temp=i.find_all("p")
    temp2=i.find_all("div")
    if re.search("MINING",temp[0].string) :
        gpu_all.remove(i)
    if re.search("同步卡",temp[0].string) :
        gpu_all.remove(i)
    if re.search("(記憶體：)(.*)",temp2[1].string):
        gpu_all.remove(i)
for i in gpu_all[27:-12]:
    temp=i.find_all("p")
    XD=re.search("\d{1,2}G",temp[0].string).group(0)
    print(XD)
    memory_list.append(XD)
    temp2=i.find_all("div")
    fullname.append(temp[0].string)
    #temp2[n].string n=0.core 1.clock 2.cuda|sp 3.video_interface 4.power_interface 5.length 6.warranty 8.price
    brand=re.search("華碩|麗臺|.{2,6}\s",temp[0].string).group(0)
    brand_list.append(brand)
    core=re.search("(繪圖核心：)(.*)",temp2[0].string).group(2)
    core_list.append(core)
    clock=re.search("(核心時脈：)(.*)(MHz)",temp2[1].string).group(2)
    clock_list.append(clock)
    
    cuda_sp=re.search("(CUDA 數：|SP 數:|SP 數：)(.*)",temp2[2].string).group(2)
    cuda_sp_list.append(cuda_sp)
    video_interface=re.search("(輸出介面：)(.*)",temp2[3].string).group(2)
    video_interface_list.append(video_interface)
    power_interface=re.search("(電源接口：)(.*)",temp2[4].string).group(2)
    power_interface_list.append(power_interface)
    length=re.search("(顯卡長度：)(.*)(公分)",temp2[5].string).group(2)
    length_list.append(length)
    warranty=re.search("(.)年",temp2[6].string).group(1)
    if warranty == '三':
        warranty='3'
    if warranty == '四':
        warranty='4'
    if warranty == '五':
        warranty='5'


    warranty_list.append(warranty)
    price=re.search("(含稅價：NT)(\d*)(.*)",temp[1].get_text()).group(2)
    price_list.append(price)

    table=pd.DataFrame({"brand":brand_list,"core":core_list,"memory":memory_list,"clock(MHz)":clock_list,"cuda_sp":cuda_sp_list,"video_interface":video_interface_list,"power_interface":power_interface_list,"legth(cm)":length_list,"warranty(years)":warranty_list,"price":price_list,"rank":"null","benchmark":"null"})
    table.to_csv('.gpu_list2.csv', encoding='utf_8_sig')

#%%


#%%
