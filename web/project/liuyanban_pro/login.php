<?php
    //接受前端传过来的数据
    $username = $_POST["username"];
    $password = $_POST["password"];

    //链接数据库
    $conn = mysqli_connect("localhost","root","201583","liuyanban_pro");

    //定义查询语句
    $selectSQL = "SELECT * FROM login WHERE username= '$username' and password= '$password'";

    //是否查询到
    $result = mysqli_query($conn,$selectSQL);

    //获取结果集中的数据条数
    $num = mysqli_num_rows($result);

    //根据条数做判断
    if($num == 1) {
        //查到了数据，允许登录
        echo json_encode(array("error" => 0, "date" => "登录成功"));
    }else{
        //没有查询到数据 不允许登录
        echo json_encode(array("error" => 1, "date" => "登录失败"));
    }
?>