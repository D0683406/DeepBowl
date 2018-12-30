#hardware
import requests
from bs4 import BeautifulSoup,Tag
import pandas as pd
from datetime import datetime
from dateutil import parser
import math

def get_one_hardware(hardware=None, price=None):
    CPU_LIST_CSV = '/Users/pandaoao/DeepBowl/DATA/cpu_list.csv'
    msg=''
    msg2=''
    msg3=''
    if hardware != None and price!= None:
        msg = '選擇硬體：' + str(hardware) 
        msg2 = '\n  \n, 選擇價錢：' + str(int(price))

        pd_cpu = pd.read_csv(CPU_LIST_CSV)
        pd_cpu['price'] = pd_cpu['price'].astype('int')
        number = price
        logN = int ( math.log10(number) ) 
        print(logN)
        print(math.pow(10,3)-1)
        filter1 = (pd_cpu['price'] > number - math.pow(10,3)-1 )
        filter2 = (pd_cpu['price'] < number + math.pow(10,3)-1 )
        msg3 = ', 推薦列表：' + str ( pd_cpu[(filter1 & filter2)] )

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
    if req['queryResult']['parameters']['number'] != '':
        price = req['queryResult']['parameters']['number']
    if req['queryResult']['parameters']['hardware'] != '':
        hardware = req['queryResult']['parameters']['hardware']
    res = {"fulfillmentText": get_one_hardware(hardware, price)}
    return make_response(jsonify(res))

if __name__ == '__main__':
    app.run(port=5000)