var express = require("express");
var path = require('path');
var favicon = require('serve-favicon');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');
var app = express();
var users = require('./routes/users');
const port = 3000;

// 設定 Route
app.get("/", function(req, res) {
    res.sendFile(__dirname + "/" + "index.html");
});

// DataBase 
var mysql = require("mysql");

var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "",
    database: "test"
});

con.connect(function(err) {
    if (err) {
        console.log('connecting error');
        return;
    }
    console.log('connecting success');
});

// 建立 application/x-www-form-urlencoded 編碼解析處理函式
const bodyParser = require('body-parser');
const urlencodedParser = bodyParser.urlencoded({ extended: false });
//404 not found
app.get("*", function(req, res) {
    res.status(404).send("oops, 404 not found");
  });

app.post("/process_post", urlencodedParser, function(req, res) {
    const firstName = req.body.first_name;
    const lastName = req.body.last_name;
    if(firstName=='s'){res.send('Hello, 你成功了');}
    else{res.send('你失敗了')}
    
    
    //else{res.send(`你失敗了`)}
});
app.listen(port, () => console.log(`Example app listening on port ${port}!`));

//透過引入的 express 模組，產生一個 App server，並且讓 server 監聽 3000 port，
//當有人發送請求到 3000 時，server 就可以監聽到請求，並且依照 Route 的設定，進行不同的處理，
//最後回傳內容給請求者。 