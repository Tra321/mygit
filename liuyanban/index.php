<?php
require_once 'conn.php';
?>
<!DOCTYPE html>
<html lang="zh-CN">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>

<body>
    <h1><a href="./index.php"><?php echo $title; ?></a></h1>

    <h2>写留言</h2>
    <form action="add.php" method="GET">
        <textarea name="t" cols="30" rows="10" placeholder="说点什么..."></textarea>
        <p><input name="n" type="text" placeholder="你的名字"></p>
        <p><input type="submit" value="发表"></p>
    </form>
    <button><a href="./login.html">管理</a></button>

    <hr>

    <h2>留言列表</h2>
    <ul>
        <?php
        // 最新留言展示前面
        $sql = "SELECT * FROM `liuyan` ORDER BY `liuyan`.`id` DESC";
        // ORDER BY `liuyan`.`id` DESC 加上这个是降序排列
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
        ?>        
    </ul>

</body>

</html>