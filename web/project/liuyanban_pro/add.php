<?php
require_once 'conn.php'; // 包含数据库连接文件

// 获取表单数据
$messageText = $_POST['t'];
$userName = $_POST['n'];
$time = date("Y-m-d H:i:s");

// 插入留言到数据库
$sql = "INSERT INTO `liuyan` (`username`, `text`, `time`) VALUES ('$userName', '$messageText', '$time')";

if ($conn->query($sql) === TRUE) {
    // 返回成功的响应
    echo json_encode(['success' => true]);
} else {
    // 返回失败的响应
    echo json_encode(['success' => false, 'liuyan' => '留言存储失败']);
}

// 关闭数据库连接
$conn->close();
?>