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
 '广东-深圳市-龙岗', 
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
 '广东-深圳市-龙岗',
 '//img.mukewang.com/57bf09700001c20201000100-140-140.jpg',
 'admin'
 );


INSERT INTO `
tour`.`hotel
`
(`hotelName`, `price`, `score`, `number`, `address`, `introduction`, `pic`) VALUES
('七天', '99', '4', '100', '北京-市辖区-东城区', '额', NULL);
INSERT INTO `
tour`.`hotel
`
(`hotelName`, `price`, `score`, `number`, `address`, `introduction`, `pic`) VALUES
('如家', '999', '3', '99', '北京-市辖区-东城区', '很好的酒店', NULL);
INSERT INTO `
tour`.`hotel
`
(`hotelName`, `price`, `score`, `number`, `address`, `introduction`, `pic`) VALUES
('如家2', '999', '3', '99', '北京-市辖区-东城区', '很好的酒店', NULL);
INSERT INTO `
tour`.`hotel
`
(`hotelName`, `price`, `score`, `number`, `address`, `introduction`, `pic`) VALUES
('如家2', '999', '3', '99', '广东-深圳市-宝安区', '很好的酒店', NULL);
INSERT INTO `
tour`.`hotel
`
(`hotelName`, `price`, `score`, `number`, `address`, `introduction`, `pic`) VALUES
('如家', '999', '3', '99', '广东-深圳市-宝安区', '很好的酒店', NULL);
INSERT INTO `
tour`.`hotel
`
(`hotelName`, `price`, `score`, `number`, `address`, `introduction`, `pic`) VALUES
('如家', '999', '3', '99', '广东-深圳市-宝安区', '很好的酒店', NULL);


INSERT INTO `
tour`.`flight
`
(`startingPlace`, `endPlace`, `startTime`, `endTime`, `flightNumber`, `price`, `flightName`, `number`) VALUES
('北京-市辖区-东城区', '北京-市辖区-东城区', '2019-05-04', '2019-05-18', '121', '111', '北京航空公司', '111');
INSERT INTO `
tour`.`flight
`
(`startingPlace`, `endPlace`, `startTime`, `endTime`, `flightNumber`, `price`, `flightName`, `number`) VALUES
('上海-县-崇明县', '贵州-贵阳市-白云区', '2019-05-01', '2019-05-15', 'A00', '99', '北京航空公司', '100');


INSERT INTO `
tour`.`landscape
`
(`address`, `landscapeName`, `price`, `score`, `Introduction`, `pic`) VALUES
('安徽-黄山市-黄山区', '黄山', '99', '5', '黄山很好', NULL);
INSERT INTO `
tour`.`landscape
`
(`address`, `landscapeName`, `price`, `score`, `Introduction`, `pic`) VALUES
('安徽-黄山市-黄山区', '黄山景区', '99', '5', '黄山很好', NULL);
INSERT INTO `
tour`.`landscape
`
(`address`, `landscapeName`, `price`, `score`, `Introduction`, `pic`) VALUES
('广东-深圳市-宝安区', '平安大厦', '99', '5', '黄山很好', NULL);
INSERT INTO `
tour`.`landscape
`
(`address`, `landscapeName`, `price`, `score`, `Introduction`, `pic`) VALUES
('广东-深圳市-福田区', '平安大厦', '99', '5', '黄山很好', NULL);


INSERT INTO `reply` VALUES (1, '张三', '这是张三的回复', '2019-05-20', 1, 'GJUHKLHJFGHDFGNDFGNGHKGHJKHKHJKGHKVGJCNXCBVXFBXFH');

INSERT INTO `post_record` VALUES (8, 'wenzhihao', '这是帖子内容', '这是帖子标题', '2019-05-12 11:24:50', '这是图片');
INSERT INTO `post_record` VALUES (9, 'wenzhihao', '这是帖子内容', '这是帖子标题', '2019-05-12 12:01:19', '这是图片');
