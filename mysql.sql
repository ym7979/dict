--电子词典
--在dict数据库中建立words表存储单词
--        id   word  mean  三个字段
create table words (
id int primary key auto_increment,
word char(28),
mean varchar(1024),
index(word));


create table user(
id int primary key auto_increment,
name varchar(20) not null,
password char(64) not null);

create table hist1(
 uid int,
 wid int,
 primary key(uid,wid),
 `time` datetime default now()
 );

 create table hist2 (
 id int primary key auto_increment,
 name varchar(20) not null, word varchar(30),
 `time` datetime default now());
