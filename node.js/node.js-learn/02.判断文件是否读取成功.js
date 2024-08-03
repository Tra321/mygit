const fs = require('fs')

fs.readFile('./files/1.txt','utf8',function(err,dateStr) {
    if (err) {
        return console.log('读取文件失败！' + err.message)
    }
    console.log('读取文件成功' + dateStr)
})