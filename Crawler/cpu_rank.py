import re
import pandas as pd
import requests
from bs4 import BeautifulSoup

html = requests.get("https://www.cpubenchmark.net/cpu_list.php")

soup = BeautifulSoup(html.content,'lxml')

content = soup.find("table",{"id":"cputable"}).find("tbody")

rows = content.find_all("tr")

name = []
score = []
rank = []

for row in rows:
    td = row.find_all("td")
    name.append(td[0].text)
    score.append(td[1].text)
    rank.append(td[2].text)
    
table = pd.DataFrame({"name":name,"score":score,"rank":rank})

df = table

#把排名超過1200的給drop掉（最便宜NT1190的Celeron G4900排名為1139/2795）
df['rank'] = df['rank'].astype('int')
df = df.drop(df[ df['rank'] > 1300].index)

df.to_csv("./DATA/cpu_rank_list.csv", index=False, encoding="utf_8_sig")

