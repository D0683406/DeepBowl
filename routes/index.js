var express = require('express');
var router = express.Router();

// home page
router.get('/', function(req, res, next) {
    //建立 var db 賦予 req.con 連線物件資訊
    var db = req.con;
    var cpu_data = "";
    var gpu_data = "";
    var ram_data = "";
    var ssd_data = "";
    var hdd_data = "";
    var mb_data = "";
    var list_data = "";
    db.query('SELECT * FROM hardwarelist', function(err, rows) {
        
        if (err) throw err;{
            console.log(rows);
        }
        //回傳資料 rows 以陣列格式儲存
        list_data = rows;
    });
    db.query('SELECT * FROM cpu', function(err, rows) {
        //在Shell輸出rows
        if (err) throw err;{
            console.log(rows);
        }
        //回傳資料 rows 以陣列格式儲存
        cpu_data = rows;
    });
    db.query('SELECT * FROM gpu', function(err, rows) {
        if (err) throw err;{
            console.log(rows);
        }
        //回傳資料 rows 以陣列格式儲存
        gpu_data = rows;
    });
    db.query('SELECT * FROM ram', function(err, rows) {
        if (err) throw err;{
            console.log(rows);
        }
        //回傳資料 rows 以陣列格式儲存
        ram_data = rows;
    });
    db.query('SELECT * FROM ssd', function(err, rows) {
        //在Shell輸出rows
        if (err) throw err;{
            console.log(rows);
        }
        //回傳資料 rows 以陣列格式儲存
        ssd_data = rows;
    });
    db.query('SELECT * FROM ssd', function(err, rows) {
        //在Shell輸出rows
        if (err) throw err;{
            console.log(rows);
        }
        //回傳資料 rows 以陣列格式儲存
        ssd_data = rows;
    });
    db.query('SELECT * FROM hdd', function(err, rows) {
        //在Shell輸出rows
        if (err) throw err;{
            console.log(rows);
        }
        //回傳資料 rows 以陣列格式儲存
        hdd_data = rows;
    });
    db.query('SELECT * FROM mb', function(err, rows) {
        //在Shell輸出rows
        if (err) throw err;{
            console.log(rows);
        }
        //回傳資料 rows 以陣列格式儲存
        mb_data = rows;

        //運行index.ejs,在 render 部分，我們將 rows 指定到 cpu_data 變數,cpu_data: cpu_data，此為給予名稱 cpu_data，其內容為 cpu_data，將於 ejs 樣板部分使用
        res.render('index', {cpu_data: cpu_data,gpu_data: gpu_data,ram_data: ram_data,ssd_data:ssd_data,hdd_data:hdd_data,mb_data:mb_data,list_data:list_data});
    });

});
router.post('/addlist', function(req, res, next) {
    
    var db = req.con;

    var sql = {
        cpu_id: req.body.cpu_id,
        gpu_id: req.body.gpu_id,
        hdd_id: req.body.hdd_id,
        ssd_id: req.body.ssd_id,
        ram_id: req.body.ram_id,
        id: req.body.id
    };

    //console.log(sql);
    var qur = db.query('INSERT INTO hardwarelist SET ?', sql, function(err, rows) {
        if (err) {
            console.log(err);
        }
        res.setHeader('Content-Type', 'application/json');
        res.redirect('/cpu_rank');
    });

});
router.get('/userDelete', function(req, res, next) {

    var id = req.query.id;
    var db = req.con;

    var qur = db.query('DELETE FROM hardwarelist WHERE id = ?', id, function(err, rows) {
        if (err) {
            console.log(err);
        }
        res.redirect('/');
    });
});
//cpu_rank
router.get('/cpu_rank', function(req, res, next) {

    //運行rank.ejs
    res.render('cpu_rank');
});
//gpu_rank
router.get('/gpu_rank', function(req, res, next) {

    //運行rank.ejs
    res.render('gpu_rank');
});


//qa
router.get('/qa', function(req, res, next) {

    
    res.render('qa');
});

//qa_cpu

router.get('/qa_cpu', function(req, res, next) {

    
    res.render('qa_cpu');
});


//qa_gpu
router.get('/qa_gpu', function(req, res, next) {

    
    res.render('qa_gpu');
});

//qa_ram
router.get('/qa_ram', function(req, res, next) {

    
    res.render('qa_ram');
});


//qa_disk
router.get('/qa_disk', function(req, res, next) {

    
    res.render('qa_disk');
});


//qa_mb
router.get('/qa_mb', function(req, res, next) {

    
    res.render('qa_mb');
});


module.exports = router;