<!DOCTYPE html>
			<html>
<?php
$sqlitedb = new SQLiteDatabase('mydb.sqli');
$sqlReturn = $sqlitedb->query("SELECT * FROM members WHERE name = \"John\"");
?>
