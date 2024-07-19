 <?php
    $servername="localhost";
    $username="root";
    $password="201583";
    $dbname="liuyanban";
    // 创建链接
    $conn = new mysqli($servername,$username,$password,$dbname);
    // 检测链接
    if($conn->connect_error){
        die("连接失败：".$conn->connect_error);
    }
    $title = "我的留言板";
?>