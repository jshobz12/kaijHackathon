DROP DATABASE IF EXISTS INSTA;

CREATE DATABASE INSTA;

USE INSTA;

CREATE TABLE profileInformation (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,   
  username VARCHAR(256) NOT NULL,
  email VARCHAR(256) NOT NULL,
  password VARCHAR(256) NOT NULL,
  handle VARCHAR(256) NOT NULL,
  totalPoints INT NULL
); 


CREATE TABLE entries (
   id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
   userId INT UNSIGNED NOT NULL,
   FOREIGN KEY (userId) REFERENCES profileInformation(id),
   dateAndTime DATETIME NOT NULL,
   insta VARCHAR(2000) NOT NULL,
   instaPostId INT UNSIGNED NOT NULL,
   points INT UNSIGNED NOT NULL
);

Describe profileInformation;
Describe entries;


INSERT INTO profileInformation (username,email,password,handle,totalPoints)
VALUES("kweiss20","kiraweiss@me.com","dog1234","@kiraweiss",0);

INSERT INTO entries (userId,dateAndTime,insta,instaPostId,points)
VALUES(1,'2018-06-19 12:34:22',"linkToInsta.com",1111,2);

INSERT INTO entries (userId,dateAndTime,insta,instaPostId,points)
VALUES(1,'2018-06-20 15:07:20',"linkToInsta.com",1112,2);



INSERT INTO profileInformation (username,email,password,handle,totalPoints)
VALUES("JoeSmith","JoeSmith@gmail.com","rockon665","@joe_the_rock",0);

INSERT INTO entries (userId,dateAndTime,insta,instaPostId,points)
VALUES(2,'2018-06-16 13:55:01',"linkToInsta.com",1113,2);

INSERT INTO entries (userId,dateAndTime,insta,instaPostId,points)
VALUES(2,'2018-06-17 21:34:37',"linkToInsta.com",1114,2);

INSERT INTO entries (userId,dateAndTime,insta,instaPostId,points)
VALUES(2,'2018-06-19 19:14:48',"linkToInsta.com",1115,2);



INSERT INTO profileInformation (username,email,password,handle,totalPoints)
VALUES("fitgirl22","sarah_fitness@hotmail.com","smoothiesonly0","@fitgirl220",0);

INSERT INTO entries (userId,dateAndTime,insta,instaPostId,points)
VALUES(3,'2018-06-20 8:31:03',"linkToInsta.com",1116,2);



