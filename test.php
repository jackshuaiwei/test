<?php

$flag =0;
$filename = time().".";
$mycookie = $_POST['mycookies'];
$file = $_FILES['myexcel'];
if($file['name'] != ""){
	if($file['error']>0){
		echo "文件上传出错！";
		exit;
	}
	if(!in_array(explode(".",$file['name'])[1],['xlsx','xls'])){
		echo "文件格式有误,你上传的格式为".explode(".",$file['name'])[1];
		exit;
	}
	$filename_t = $filename.explode(".",$file['name'])[1];
	if (move_uploaded_file($file['tmp_name'],$filename_t)) {
            echo "文件上传成功";
            $flag = 1;
        }
}

$redis = new Redis();
$redis->connect('127.0.0.1',6379);
if($mycookie && $flag){
	$re = $redis->set("ama_cookie",$mycookie);
	$re2 = $redis->set("filename",$filename_t);
	if($re && $re2){
		header("refresh:3;url=download.php"); 
		echo "数据上传成功，开始抓取数据.......";
	}

}


















// for($i=0;$i<30000;$i++){
// 	$json_data = json_encode($new1[$i]);
// 	$redis->set($new1[$i]["supplier"],$json_data);

// }
// echo "ok";
// print_r(end($new1));
// $json_new = json_encode($new1);
// $redis = new Redis();
// $redis->connect('127.0.0.1',6379);
// $redis->auth(123456);
// $redis->setex('fba',3600,$json_new);




 


