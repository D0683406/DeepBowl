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
ssd_all = selects[6].text.split("\n")

#%%
# 把空字串去掉
while '' in ssd_all:
    ssd_all.remove('')
# 去掉不需要的選項
for i in ssd_all:
    if ',' not in i:
        ssd_all.remove(i)
count=0
for i in ssd_all:    
    i=i.strip('◆ ★')
    i=i.strip('◆ ★ 熱賣')
    ssd_all[count]=i
    count+=1
    print(i)

#%%
brand_list=[]
name_list=[]
size_list=[]
interface_list=[]
read_list=[]
write_list=[]
warranty_list=[]
price_list=[]
name=' '
interface=''
for i in ssd_all:
    if re.match("Intel Optane Memory",i):
        ssd_all.remove(i)
for i in ssd_all:
    #廠牌
    brand=re.search("三星Samsung|三星 Samsung|UMAX|KLEVV\(科賦\)|威剛|GIGABYTE 技嘉|Liteon|Plextor|影馳 GALAX|Intel|海康|Pioneer|金士頓|美光Micron|WD|美光|Pioneer",i).group(0)
    brand_list.append(brand)
    #名字和容量
    temp=i.strip(brand)
    size=re.search("32GB|32G|128GB|128G|256GB|256G|280G|480GB|480G|512GB|512G|960GB|960G|16GB|16G|240GB|240G|500GB|500G|120GB|120G|250GB|250G|1TB|2TB|4TB",temp).group(0)
    name=re.search(".*32GB|.*32G|.*128GB|.*128G|.*256GB|.*256G|.*280G|.*480GB|.*480G|.*512GB|.*512G|.*960GB|.*960G|.*16GB|.*16G|.*240GB|.*240G|.*500GB|.*500G|.*120GB|.*120G|.*250GB|.*250G|.*1TB|.*2TB|.*4TB",temp).group(0)
    size_list.append(size)
    name=name.strip(size)
    if name.strip(size) == '':
        name='Noname'
    if (re.match("\s",name[0])):
        name=re.sub("\s","",name,1)
    name_list.append(name)
    #接口
    #print(i)
    
    if not re.search("M.2 PCIe|M.2 SATA|m-SATA|2.5\" 7mm|7mm|M.2 SATA 2280|M.2 PCIe 2280|M.2 PCIe|PCIe",i):
        interface="2.5\" 7mm"
    else:
        interface=re.search("M.2 PCIe 2280|M.2 SATA 2280|m-SATA|2.5\" 7mm|7mm|M.2 SATA|M.2 PCIe|M.2 PCIe|PCIe",i).group(0)
    interface_list.append(interface)

    #讀取寫入
    read=re.search("讀\:\d*|3D TLC",i).group(0)
    if read=="3D TLC":
        read="讀:545"
    read_list.append(read)
    write=re.search("寫\:\d*|3D TLC|寫1000M",i).group(0)
    if write=="3D TLC":
        write="寫:525"
    if write=="寫1000":
        write="寫:1000"
    write_list.append(write)

    #保固
    if not (re.search(r".年",i)):
        warranty='向廠商詢問'
    else :
        warranty=re.search(r"(.)年",i).group(1)
        if warranty == '三':
            warranty='3'
        if warranty == '四':
            warranty='4'
        if warranty == '五':
            warranty='5'
        if warranty == '十':
            warranty='10'

    
    
    warranty_list.append(warranty)

    #價錢
    price=re.search("\$(\d*)",i).group(1)
    price_list.append(price)
    

    


table = pd.DataFrame({"brand_list":brand_list,"name":name_list,"size":size_list,"interface":interface_list,"read":read_list,"write":write_list,'warranty(year)':warranty_list,'price':price_list})
table.to_csv('./DATA/ssd_list.csv', encoding='utf_8_sig')

    
    
    




#%%
