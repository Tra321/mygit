<?php
$host = 'localhost'; // 数据库服务器
$username = 'root';   // 数据库用户名
$password = '201583'; // 数据库密码
$database = 'liuyanban_pro'; // 数据库名

// 创建连接
$conn = new mysqli($host, $username, $password, $database);

// 检查连接
if ($conn->connect_error) {
    die("连接失败: " . $conn->connect_error);
}
?>