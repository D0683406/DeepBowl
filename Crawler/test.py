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
mb_all2 = mb_all.find_all("a")

#%%
