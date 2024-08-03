const fs = require('fs')

// 出现路径拼接错误这个问题，是因为提供了./或 ../开头的相对路径
//./files/1.txt
//要解决这个问题，可以直接提供一个完整的文件存放路径就行
//移植性差，不利于维护
// fs.readFile('D:\\Hub\\Git\\mygit\\node.js-learn\\code\\files\\1.txt','utf8',function(err, dataStr) {
//     if(err) {
//         return console.log('读取文件失败！' + err.message)
//     }
//     console.log('读取文件成功！' + dataStr)
// })

//__dirname 表示当前文件所处的目录
// console.log(__dirname)

fs.readFile(__dirname + '/files/1.txt','utf8',function(err, dataStr) {
        if(err) {
            return console.log('读取文件失败！' + err.message)
        }
        console.log('读取文件成功！' + dataStr)
    })