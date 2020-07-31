<form action="download.php" method="post"> 
	<input type="hidden" name="getdata" value="1">
	<input type="submit" name="" value="请求下载链接">
</form>

<?php
// echo "<br>如果出现错误404，请等一分钟再尝试点击下载";
$download_flag = $_POST['getdata'];
if($download_flag){
	$redis = new Redis();
	$redis->connect('127.0.0.1',6379);
	$save_name = $redis->get("save_name");
	if($save_name){
		echo "<a href = ".$save_name.">下载废物excel</a>";
		$redis->flushDB();
	}
	else{
		// header("refresh:3;url=download.php");
		echo "请等一分钟在尝试";
	}

}


