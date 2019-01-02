#hardware
import requests
from bs4 import BeautifulSoup,Tag
import pandas as pd
from datetime import datetime
from dateutil import parser
import math
import  pymysql 

def get_one_hardware(hardware=None, price=None, function=None, brand=None, size=None, game=None):

    msg=''
    msg2=''
    msg3=''

    # 「全域功能」依「硬體」、「預算」推薦「硬體」
    if hardware != None and price != None:
        msg = '選擇硬體：' + str(hardware) 
        msg2 = ', 選擇價錢：' + str(int(price))

        conn  =  pymysql . connect ( host = '127.0.0.1' ,  user = 'root' ,  passwd = "" ,  db = 'deepbowl' ) 
        cur  =  conn . cursor () 
        #brand = '美光'
        #size= '16GB'
        msg = '選擇硬體：' + str(hardware) 
        msg2 = ', 選擇價錢：' + str(int(price))
        logN = int ( math.log10(price) ) 
        price1 = int(price) - math.pow(10,logN)
        price2 = int(price) + math.pow(10,logN)-1
        print(str(price1))
        print(str(price2))
        cur.execute("SELECT * FROM %s WHERE price > %d and price < %d"%(str(hardware).lower(), int(price1), int(price2)))
        result = cur.fetchall()
        cur . close () 
        conn . close()

        result = [[str(x) for x in tup] for tup in result]
        result[0]

        for r in result:
            r = [[str(x) for x in tup] for tup in r]
        result
        msg3='推薦硬體：'
        for r in result:
            if str(hardware).lower() == 'cpu':
                msg3 = msg3 + "廠牌：%s, 型號：%s, TDP：%s, 價格：%s, 分數：%s, 排名：%s"%(r[1],r[2],str(r[3]),str(r[4]),str(r[5]),str(r[7]))
            elif str(hardware).lower() == 'ram':
                msg3 = msg3 + "廠牌：%s, 大小：%s, 規格：%s, 頻率：%s, 價格：%s"%(r[1],r[2],r[3],r[4],r[6])
            elif str(hardware).lower() == 'ssd':
                msg3 = msg3 + "廠牌：%s, 型號：%s, 大小%s, 介面：%s, 讀取速度：%s, 寫入速度：%s, 保固年份：%s, 價格：%s"%(r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8])
            elif str(hardware).lower() == 'gpu':
                msg3 = msg3 + "廠牌：%s, 型號：%s, 大小：%s, 時脈：%s, 長度：%s, 保固：%s, 價格：%s"%(r[1],r[2],r[3],r[4],r[9],r[10],r[11])
            else:
                msg3 = msg3 + ''.join(r[0]) + ',\n'

    # 「全域功能」依「硬體」（功能）列出全部「廠牌」
    elif hardware != None and str(function) == '全部廠牌':
        conn  =  pymysql . connect ( host = '127.0.0.1' ,  user = 'root' ,  passwd = "" ,  db = 'deepbowl' ) 
        cur  =  conn . cursor () 

        msg = '選擇硬體：' + str(hardware) 
        msg2 = ', 選擇功能：' + str(function)

        cur.execute("SELECT DISTINCT brand FROM " + str(hardware).lower() )
        result = cur.fetchall()
        cur . close () 
        conn . close()
        result[0][0]
        msg3=', 全部廠牌：'
        for r in result:

            msg3 = msg3 + ''.join(r[0]) + ',\n'

    # 依CPU功能去推薦
    elif str(hardware).lower() == 'cpu':
        
        # 依「硬體」、「功能」推薦「硬體」
        if hardware != None and function != None:
            conn  =  pymysql . connect ( host = '127.0.0.1' ,  user = 'root' ,  passwd = "" ,  db = 'deepbowl' ) 
            cur  =  conn . cursor () 
            #hardware = 'gpu'
            #game = 'LOL'
            msg = '選擇硬體：' + str(hardware) 
            msg2 = ', 選擇功能：' + str(function)

            
            much_core=['繪圖', '算圖', '轉檔', '過檔', '渲染', 'render','多核']
            if function in much_core:
                cur.execute("SELECT * FROM cpu WHERE model like '%2700x%'")
            much_free='線上遊戲'
            if function in much_free:
                cur.execute("SELECT * FROM cpu WHERE model like '%8700k%'")
            simple=['文書處理', '瀏覽網頁', '簡單遊戲']
            if function in simple:
                cur.execute("SELECT * FROM cpu WHERE model like '%g5500%' || model like'%2200G%'")
            cheap=['便宜','低預算']
            if function in cheap:
                cur.execute("SELECT * FROM cpu WHERE model like '%g5500%' || model like'%2400G%'")

            result = cur.fetchall()
            cur . close () 
            conn . close()

            result = [[str(x) for x in tup] for tup in result]

            
            for r in result:
                r = [[str(x) for x in tup] for tup in r]
            result
            msg3=', 推薦硬體：'
            for r in result:
                msg3 = msg3 + "廠牌：%s, 型號：%s, TDP：%s, 價格：%s, 分數：%s, 排名：%s"%(r[1],r[2],str(r[3]),str(r[4]),str(r[5]),str(r[7]))
     
    elif str(hardware).lower() == 'ram':
        # 依ram廠牌、大小去推薦
        if brand != None and size !=None:
            
            conn  =  pymysql . connect ( host = '127.0.0.1' ,  user = 'root' ,  passwd = "" ,  db = 'deepbowl' ) 
            cur  =  conn . cursor () 
            #brand = '美光'
            #size= '16GB'
            msg = '選擇硬體：' + str(hardware) 
            msg2 = ', 選擇廠牌：' + str(brand)
            msg2 = msg2 + ', 選擇大小' + str(size)

            cur.execute("SELECT * FROM ram WHERE brand LIKE %s && size = %s",("%" + str(brand) + "%",size))
            result = cur.fetchall()
            cur . close () 
            conn . close()

            result = [[str(x) for x in tup] for tup in result]
            result[0]

            final = []
            for r in result:
                r = [[str(x) for x in tup] for tup in r]
            result
            msg3=''
            for r in result:
                msg3 = msg3 + "廠牌：%s, 大小：%s, 規格：%s, 頻率：%s, 價格：%s"%(r[1],r[2],r[3],r[4],r[6])
                #msg3 = msg3 + ','.join(r) + '\n'

    elif str(hardware).lower() == 'ssd':
        # 依ssd廠牌、大小去推薦
        if brand != None and size !=None:
            
            conn  =  pymysql . connect ( host = '127.0.0.1' ,  user = 'root' ,  passwd = "" ,  db = 'deepbowl' ) 
            cur  =  conn . cursor () 
            #brand = 'WD'
            #size= '256GB'
            msg = '選擇硬體：' + str(hardware) 
            msg2 = ', 選擇廠牌：' + str(brand)
            msg2 = msg2 + ', 選擇大小' + str(int(size))

            cur.execute("SELECT * FROM ssd WHERE brand LIKE %s && size like %s",("%" + str(brand) + "%",str(int(size))+"%"))
            result = cur.fetchall()
            cur . close () 
            conn . close()

            result = [[str(x) for x in tup] for tup in result]

            final = []
            for r in result:
                r = [[str(x) for x in tup] for tup in r]
            result
            msg3=''
            for r in result:
                msg3 = msg3 + "廠牌：%s, 型號：%s, 大小%s, 介面：%s, 讀取速度：%s, 寫入速度：%s, 保固年份：%s, 價格：%s"%(r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8])

        # 推薦MX500系列
        if str(function) == '推薦':
            
            conn  =  pymysql . connect ( host = '127.0.0.1' ,  user = 'root' ,  passwd = "" ,  db = 'deepbowl' ) 
            cur  =  conn . cursor () 
            #brand = 'WD'
            #size= '256GB'
            msg = '選擇硬體：' + str(hardware) 

            cur.execute("SELECT * FROM ssd WHERE model like '%MX500%'")
            result = cur.fetchall()
            cur . close () 
            conn . close()

            result = [[str(x) for x in tup] for tup in result]

            final = []
            for r in result:
                r = [[str(x) for x in tup] for tup in r]
            result
            msg3=', 推薦硬體：'
            for r in result:
                msg3 = msg3 + "廠牌：%s, 型號：%s, 大小%s, 介面：%s, 讀取速度：%s, 寫入速度：%s, 保固年份：%s, 價格：%s"%(r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8])

    elif str(hardware).lower() == 'gpu':

        conn  =  pymysql . connect ( host = '127.0.0.1' ,  user = 'root' ,  passwd = "" ,  db = 'deepbowl' ) 
        cur  =  conn . cursor () 
        #hardware = 'gpu'
        #game = 'LOL'
        msg = '選擇硬體：' + str(hardware) 
        msg2 = ', 選擇遊戲：' + str(game)

        if str(game) == 'LOL':
            cur.execute("SELECT * FROM gpu WHERE core like '%1050%'")
        if str(game).lower == 'over watch':
            cur.execute("SELECT * FROM gpu WHERE core like '%1050%' || core like'%1070%'")
        if str(game) in ['大型遊戲', 'GTA', '巫師3']:
            cur.execute("SELECT * FROM gpu WHERE core like '%1050%' || core like'%1060%' || core like'%1070%'")

        result = cur.fetchall()
        cur . close () 
        conn . close()

        result = [[str(x) for x in tup] for tup in result]

        final = []
        for r in result:
            r = [[str(x) for x in tup] for tup in r]
        result
        msg3=', 推薦硬體：'
        for r in result:
            msg3 = msg3 + "廠牌：%s, 型號：%s, 大小：%s, 時脈：%s, 長度：%s, 保固：%s, 價格：%s"%(r[1],r[2],r[3],r[4],r[9],r[10],r[11])

    return msg + msg2 + msg3
import json

from flask import Flask, request, make_response, jsonify

app = Flask(__name__)


@app.route("/")
def verify():
    return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print(req)
    hardware=None
    price=None
    function=None
    brand=None
    size=None
    game=None

    if req.get("queryResult").get("action") in ['gpu']:
        if req['queryResult']['parameters']['game'] != '':
            game = req['queryResult']['parameters']['game'] 

    if req.get("queryResult").get("action") in ['brand','cpu','ram','price','ssd','gpu']:
        if req['queryResult']['parameters']['hardware'] != '':
            hardware = req['queryResult']['parameters']['hardware'] 

    if req.get("queryResult").get("action") in ['cpu','price']:
        if req['queryResult']['parameters']['price'] != '':
            price = req['queryResult']['parameters']['price']

    if req.get("queryResult").get("action") in ['brand','cpu','ssd']:
        if req['queryResult']['parameters']['function'] != '':
            function = req['queryResult']['parameters']['function']

    if req.get("queryResult").get("action") in ['ram','ssd']:
        if req['queryResult']['parameters']['brand'] != '':
            brand = req['queryResult']['parameters']['brand']

    if req.get("queryResult").get("action") in ['ram','ssd']:
        if req['queryResult']['parameters']['size'] != '':
            size = req['queryResult']['parameters']['size']

    res = {"fulfillmentText": get_one_hardware(hardware, price, function, brand, size, game)}
    return make_response(jsonify(res))

if __name__ == '__main__':
    app.run(port=5000)