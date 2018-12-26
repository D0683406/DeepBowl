var express = require('express');
var router = express.Router();

// home page
router.get('/', function(req, res, next) {

    var db = req.con;
    var data = "";

    db.query('SELECT * FROM cpu', function(err, rows) {
        //在Shell輸出rows
        if (err) throw err;{
            console.log(rows);
        }
        //存資料
        var data = rows;

        //運行index.ejs
        res.render('index2', { title: 'Account Information', data: data});
    });

});
module.exports = router;