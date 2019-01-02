#hardware
import requests
from bs4 import BeautifulSoup,Tag
import pandas as pd
from datetime import datetime
from dateutil import parser
import math
import  pymysql 

def get_one_hardware(hardware=None, price=None, function=None, brand=None, size=None, game=None):

    #  給予絕對路徑
    LIST_CSV = '/Users/pandaoao/DeepBowl/DATA/cpu_list.csv'
    msg=''
    msg2=''
    msg3=''

    # 「全域功能」依「硬體」、「預算」推薦「硬體」
    if hardware != None and price != None:
        msg = '選擇硬體：' + str(hardware) 
        msg2 = ', 選擇價錢：' + str(int(price))

        LIST_CSV = '/Users/pandaoao/DeepBowl/DATA/' + str(hardware).lower() + '_list.csv'
        pd_cpu = pd.read_csv(LIST_CSV)
        pd_cpu['price'] = pd_cpu['price'].astype('int')
        price = price
        logN = int ( math.log10(price) ) 
        print(logN)
        print(math.pow(10,3)-1)
        filter1 = (pd_cpu['price'] > price - math.pow(10,3)-1 )
        filter2 = (pd_cpu['price'] < price + math.pow(10,3)-1 )
        msg3 = ', 推薦硬體：' + str ( pd_cpu[(filter1 & filter2)] )
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
            msg = '選擇硬體：' + str(hardware) 
            msg2 = ', 選擇功能：' + str(function)
            pd_cpu = pd.read_csv(LIST_CSV)
            
            much_core=['繪圖', '算圖', '轉檔', '過檔', '渲染', 'render','多核']
            if function in much_core:
                # pd_cpu[d_cpu['model'].str.cotains('2700X')]
                filter1 = pd_cpu['model'].str.lower().str.contains('2700x'.lower())
                msg3 = ', 推薦硬體：' + str ( pd_cpu[(filter1)] )

            much_free='線上遊戲'
            if function in much_free:
                filter1 = pd_cpu['model'].str.lower().str.contains('8700k'.lower())
                msg3 = ', 推薦硬體：' + str ( pd_cpu[(filter1)] )

            simple=['文書處理', '瀏覽網頁', '簡單遊戲']
            if function in simple:
                filter1 = pd_cpu['model'].str.lower().str.contains('g5500'.lower())
                filter2 = pd_cpu['model'].str.lower().str.contains('2200G'.lower())
                msg3 = ', 推薦硬體：' + str ( pd_cpu[(filter1 | filter2)] )

            cheap=['便宜','低預算']
            if function in cheap:
                filter1 = pd_cpu['model'].str.lower().str.contains('g5500'.lower())
                filter2 = pd_cpu['model'].str.lower().str.contains('2400G'.lower())
                msg3 = ', 推薦硬體：' + str ( pd_cpu[(filter1 | filter2)] )
    
    
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
                msg3 = msg3 + ','.join(r) + '\n'

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
                msg3 = msg3 + ','.join(r) + '\n'
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
                msg3 = msg3 + ','.join(r) + '\n'

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
            msg3 = msg3 + ','.join(r) + '\n'

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