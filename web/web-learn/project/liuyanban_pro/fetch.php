<?php
require_once 'conn.php'; // 包含数据库连接文件

// 查询留言列表
$sql = "SELECT `id`, `username`, `text`, `time` FROM `liuyan` ORDER BY `id` DESC";

$result = $conn->query($sql);

if($result->num_rows>0){
    //输出数据
    while($row = $result->fetch_assoc()){
        // $result->fetch_assoc()执行一次显示第一条，执行第二次显示第二条
    ?>
    <li>
        <p><?php echo $row["id"];?>楼</p>
        <p>留言内容：<?php echo $row["text"];?></p>
        <p>留言人：<?php echo $row["username"];?></p>
        <p>留言时间：<?php echo $row["time"];?></p>
    </li>
    <?php
    }
} else {
    echo"暂无留言";
}

// 关闭数据库连接
$conn->close();
?>