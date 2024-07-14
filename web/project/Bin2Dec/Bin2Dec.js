function convertBinaryToDecimal() {
    //从输入框获取二进制数
    let binary = document.getElementById('binary-input').value;

    //检查是否输入有效的二进制数
    if(!/^[01]+$/.test(binary)) {
        alert("请输入有效的二进制数！");
        return;
    }

    let decimal = parseInt(binary, 2);

    document.getElementById('decimal-output').textContent = decimal.toString();
}