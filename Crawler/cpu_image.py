#%%
import urllib
import urllib2
from bs4 import BeautifulSoup
 
def getContentFromUrl(url):
    req = urllib2.Request(url)
    content = urllib2.urlopen(req).read()
    content = BeautifulSoup(content, from_encoding='GB2312')
    return content

def getInfoFromContent(content):
    imgID = 0    
    imgs = content.find_all('img')
    for link in imgs:
        url = link.get('src')       
        urllib.urlretrieve(url, "data/%02d.jpg"%imgID)  
        print(link.get('src'))
        imgID =imgID+1

if __name__ == "__main__":
    #print(getContentFromUrl("http://www.sohu.com"))
    content = getContentFromUrl("https://www.coolpc.com.tw/eachview.php?IGrp=4")
    getInfoFromContent(content)

#%%
