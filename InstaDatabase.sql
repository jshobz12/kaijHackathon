DROP DATABASE IF EXISTS INSTADB;

CREATE DATABASE INSTADB;

USE INSTADB;

CREATE TABLE profileInformation (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,   
  username VARCHAR(256) NOT NULL,
  email VARCHAR(256) NOT NULL,
  password VARCHAR(256) NOT NULL,
  handle VARCHAR(256) NOT NULL
);


CREATE TABLE entries (
   id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
   userId INT UNSIGNED NOT NULL,
   FOREIGN KEY (userId) REFERENCES profileInformation(id),
   dateAndTime DATETIME NOT NULL,
   postURL VARCHAR(2000) NOT NULL,
   imgURL VARCHAR(2000) NOT NULL,
   instaPostId VARCHAR(256) NOT NULL,
   points INT UNSIGNED NULL
);

Describe profileInformation;
Describe entries;


INSERT INTO profileInformation (username,email,password,handle)
VALUES("kweiss20","kiraweiss@me.com","dog1234","@kiraweiss");

INSERT INTO entries (userId,dateAndTime,postURL,imgURL,instaPostId,points)
VALUES(1,'2018-06-19 12:34:22',"linkToInsta.com",'linktoimg.com',1111,2);

INSERT INTO entries (userId,dateAndTime,postURL,imgURL,instaPostId,points)
VALUES(1,'2018-06-20 15:07:20',"linkToInsta.com",'linktoimg.com',1112,2);



INSERT INTO profileInformation (username,email,password,handle)
VALUES("JoeSmith","JoeSmith@gmail.com","rockon665","@joe_the_rock");

INSERT INTO entries (userId,dateAndTime,postURL,imgURL,instaPostId,points)
VALUES(2,'2018-06-16 13:55:01',"linkToInsta.com",'images/health_imgs/running.jpg',1113,2);

INSERT INTO entries (userId,dateAndTime,postURL,imgURL,instaPostId,points)
VALUES(2,'2018-06-17 21:34:37',"linkToInsta.com",'images/health_imgs/biking.jpg',1114,2);

INSERT INTO entries (userId,dateAndTime,postURL,imgURL,instaPostId,points)
VALUES(2,'2018-06-19 19:14:48',"linkToInsta.com",'images/health_imgs/running2.jpg',1115,2);



INSERT INTO profileInformation (username,email,password,handle)
VALUES("fitgirl22","sarah_fitness@hotmail.com","smoothiesonly0","@fitgirl220");

INSERT INTO entries (userId,dateAndTime,postURL,imgURL,instaPostId,points)
VALUES(3,'2018-06-20 8:31:03',"linkToInsta.com",'images/health_imgs/salad.jpg',1116,2);

INSERT INTO profileInformation (username,email,password,handle)
VALUES("aritheuser","ari@ari.com","password","aritherobot");




/*SOME QUERIES*/





