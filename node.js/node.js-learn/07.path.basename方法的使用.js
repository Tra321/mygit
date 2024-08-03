const path = require('path')

//定义文件路径
const fpath = '/a/b/c/index.html'

// const fullName = path.basename(fpath)
// console.log(fullName)

const nameWithoutExt = path.basename(fpath,'html')
console.log(nameWithoutExt)