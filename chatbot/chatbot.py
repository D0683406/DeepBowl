# %%
import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def makeWebhookResult(req):
    speech = ""
    # actionname的地方是Dialogflow>Intent>Action 取名的內容
    # if req.get("result").get("action") != "actionname":
    #    return {}
    result = req.get("queryResult")
    parameters = result.get("parameters")
    # parameters.get("parameters")的parametersxxx是Dialogflow > Entitiy
    # 也就是步驟josn格式中parameters>parametersxxx
    type = parameters.get("type")
    price = parameters.get("price")

    # fulfillmentText就是回應的內容，下面就能用if,else來判斷怎麼回應了
    if(price == "30000"):
        speech=type
        fulfillmentText = speech
        print("Response:")
        print(fulfillmentText)
    # 回傳
    return {
        "fulfillmentText": fulfillmentText,
        "fulfillmentText": fulfillmentText,
        # "payload": {},
        # "outputContexts": [],
        "source": "agent"
    }


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)

# %%
