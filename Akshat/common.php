<?php
    $servername = "localhost";
    $username = "root";
    $password = "";
    $conn = mysqli_connect($servername, $username,$password) or die(mysqli_error($conn));
    
    if(!isset($_SESSION)){
        session_start();
    } 
    $sql="CREATE DATABASE IF NOT EXISTS epiz_30090771_Shop";
    mysqli_query($conn, $sql);
   
   
   $sql="CREATE TABLE epiz_30090771_Shop.users(
       id INT(11) PRIMARY KEY AUTO_INCREMENT,
       name VARCHAR(255) NOT NULL,
       email VARCHAR(255) NOT NULL,
       password VARCHAR(255) NOT NULL,
       contact VARCHAR(255) NOT NULL,
       city VARCHAR(255) NOT NULL,
       address VARCHAR(255) NOT NULL)";
   
       mysqli_query($conn,$sql);
   
   
        
    ?>