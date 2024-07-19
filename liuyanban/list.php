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
                <p>
                    <a href="edit.php?id=<?php echo $row['id'];?>">编辑</a>
                    <a href="del.php?id=<?php echo $row['id'];?>">删除</a>
                </p>
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