truncate table `tour`.`user`;

INSERT INTO `tour`.`user` (
 `userName`, 
 `sex`, 
 `password`, 
 `nickName`, 
 `location`, 
 `pic`, 
 `type`
) 
VALUES (
 'fan', 
 '男', 
 '123', 
 '范某人', 
 '广东-深圳-龙岗', 
 '//img.mukewang.com/57bf09700001c20201000100-140-140.jpg', 
 'ordinary'
);

INSERT INTO `tour`.`user` (
 `userName`, 
 `sex`, 
 `password`,
 `nickName`,
 `location`,
 `pic`,
 `type`
)
VALUES (
 'admin',
 '女',
 '123',
 '管理员',
 '广东-深圳-龙岗',
 '//img.mukewang.com/57bf09700001c20201000100-140-140.jpg',
 'admin'
 );
