var express = require('express');
var path = require('path');
var app = express();
var routes = require('./routes/index');
var users = require('./routes/users');

// 在port 3000
var port = process.env.PORT || 3000;

// create
app.listen(port);

// 判斷有沒有建立成功
if(port === 3000){
  console.log('RUN http://localhost:3000/')
}


// 連接資料庫 
var mysql = require("mysql");
// 連接資料庫訊息 "deepbowl"為資料庫名稱
var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "",
    database: "deepbowl"
});
//判斷有沒有連線成功
con.connect(function(err) {
    if (err) {
        console.log('connecting error');
        return;
    }
    console.log('connecting success');
});

// 使用ejs模板 *ejs模板跟html差不多 但功能比較多
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

// 登入資料庫
app.use(function(req, res, next) {
    req.con = con;
    next();
});

//使用下面的js檔與檔案
app.use(express.static(__dirname + '/images'));
app.use(express.static(__dirname + '/views'));
app.use('/', routes);
app.use('/users', users);

//這個沒打不能跑 我也不知道幹嘛的
module.exports = app;