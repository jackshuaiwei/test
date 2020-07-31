<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
</head>
<body>
	<form action="test.php" method="post" enctype="multipart/form-data"> 
	<input type="file" name="myexcel">
	<br>
	<br>
	<textarea name="mycookies" id="cookies" placeholder="请复制你的 cookies" rows="15" cols="80"></textarea>
	<br>
	<br>
	<input type="submit" name="" value="提交">
</form>
</body>
</html>
<?php
system("python weather.py  >> hhh.txt &");

?>







