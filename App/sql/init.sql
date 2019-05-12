use tour;

INSERT INTO `user` (
	`userName`,
	`sex`,
	`password`,
	`nickName`,
	`location`,
	`pic`,
	`type`
)
VALUES
	(
		'fan',
		'男',
		'123',
		'范某人',
		'广东-深圳市-龙岗',
		'//img.mukewang.com/57bf09700001c20201000100-140-140.jpg',
		'ordinary'
	);

INSERT INTO `user` (
	`userName`,
	`sex`,
	`password`,
	`nickName`,
	`location`,
	`pic`,
	`type`
)
VALUES
	(
		'admin',
		'女',
		'123',
		'管理员',
		'广东-深圳市-龙岗',
		'//img.mukewang.com/57bf09700001c20201000100-140-140.jpg',
		'admin'
	);

INSERT INTO `hotel`
(
	`hotelName`,
	`price`,
	`score`,
	`number`,
	`address`,
	`introduction`,
	`pic`
)
VALUES
	(
		'七天',
		'99',
		'4',
		'100',
		'北京-市辖区-东城区',
		'额',
		NULL
	);

INSERT INTO
`hotel` (
	`hotelName`,
	`price`,
	`score`,
	`number`,
	`address`,
	`introduction`,
	`pic`
)
VALUES
	(
		'如家',
		'999',
		'3',
		'99',
		'北京-市辖区-东城区',
		'很好的酒店',
		NULL
	);

INSERT INTO
`hotel` (
	`hotelName`,
	`price`,
	`score`,
	`number`,
	`address`,
	`introduction`,
	`pic`
)
VALUES
	(
		'如家2',
		'999',
		'3',
		'99',
		'北京-市辖区-东城区',
		'很好的酒店',
		NULL
	);

INSERT INTO
`hotel` (
	`hotelName`,
	`price`,
	`score`,
	`number`,
	`address`,
	`introduction`,
	`pic`
)
VALUES
	(
		'如家2',
		'999',
		'3',
		'99',
		'广东-深圳市-宝安区',
		'很好的酒店',
		NULL
	);

INSERT INTO
`hotel` (
	`hotelName`,
	`price`,
	`score`,
	`number`,
	`address`,
	`introduction`,
	`pic`
)
VALUES
	(
		'如家',
		'999',
		'3',
		'99',
		'广东-深圳市-宝安区',
		'很好的酒店',
		NULL
	);

INSERT INTO
`hotel` (
	`hotelName`,
	`price`,
	`score`,
	`number`,
	`address`,
	`introduction`,
	`pic`
)
VALUES
	(
		'如家',
		'999',
		'3',
		'99',
		'广东-深圳市-宝安区',
		'很好的酒店',
		NULL
	);

INSERT INTO
`flight` (
	`startingPlace`,
	`endPlace`,
	`startTime`,
	`endTime`,
	`flightNumber`,
	`price`,
	`flightName`,
	`number`
)
VALUES
	(
		'北京-市辖区-东城区',
		'北京-市辖区-东城区',
		'2019-05-04',
		'2019-05-18',
		'121',
		'111',
		'北京航空公司',
		'111'
	);

INSERT INTO
`flight` (
	`startingPlace`,
	`endPlace`,
	`startTime`,
	`endTime`,
	`flightNumber`,
	`price`,
	`flightName`,
	`number`
)
VALUES
	(
		'上海-县-崇明县',
		'贵州-贵阳市-白云区',
		'2019-05-01',
		'2019-05-15',
		'A00',
		'99',
		'北京航空公司',
		'100'
	);

INSERT INTO
`landscape` (
	`address`,
	`landscapeName`,
	`price`,
	`score`,
	`Introduction`,
	`pic`
)
VALUES
	(
		'安徽-黄山市-黄山区',
		'黄山',
		'99',
		'5',
		'黄山很好',
		NULL
	);

INSERT INTO
`landscape` (
	`address`,
	`landscapeName`,
	`price`,
	`score`,
	`Introduction`,
	`pic`
)
VALUES
	(
		'安徽-黄山市-黄山区',
		'黄山景区',
		'99',
		'5',
		'黄山很好',
		NULL
	);

INSERT INTO
`landscape` (
	`address`,
	`landscapeName`,
	`price`,
	`score`,
	`Introduction`,
	`pic`
)
VALUES
	(
		'广东-深圳市-宝安区',
		'平安大厦',
		'99',
		'5',
		'黄山很好',
		NULL
	);

INSERT INTO
`landscape` (
	`address`,
	`landscapeName`,
	`price`,
	`score`,
	`Introduction`,
	`pic`
)
VALUES
	(
		'广东-深圳市-福田区',
		'平安大厦',
		'99',
		'5',
		'黄山很好',
		NULL
	);

INSERT INTO `reply`
VALUES
	(
		1,
		'张三',
		'这是张三的回复',
		'2019-05-20',
		1,
		'GJUHKLHJFGHDFGNDFGNGHKGHJKHKHJKGHKVGJCNXCBVXFBXFH'
	);

INSERT INTO `post_record`
VALUES
	(
		8,
		'wenzhihao',
		'这是帖子内容',
		'这是帖子标题',
		'2019-05-12 11:24:50',
		'这是图片'
	);

INSERT INTO `post_record`
VALUES
	(
		9,
		'wenzhihao',
		'这是帖子内容',
		'这是帖子标题',
		'2019-05-12 12:01:19',
		'这是图片'
	);

INSERT INTO `user` (
	`userName`,
	`sex`,
	`password`,
	`nickName`,
	`location`,
	`pic`,
	`type`
)
VALUES
	(
		'fan',
		'男',
		'123',
		'范某人',
		'广东-深圳市-龙岗',
		'//img.mukewang.com/57bf09700001c20201000100-140-140.jpg',
		'ordinary'
	);

INSERT INTO `user` (
	`userName`,
	`sex`,
	`password`,
	`nickName`,
	`location`,
	`pic`,
	`type`
)
VALUES
	(
		'admin',
		'女',
		'123',
		'管理员',
		'广东-深圳市-龙岗',
		'//img.mukewang.com/57bf09700001c20201000100-140-140.jpg',
		'admin'
	);

INSERT INTO
`hotel` (
	`hotelName`,
	`price`,
	`score`,
	`number`,
	`address`,
	`introduction`,
	`pic`
)
VALUES
	(
		'七天',
		'99',
		'4',
		'100',
		'北京-市辖区-东城区',
		'额',
		NULL
	);

INSERT INTO
`hotel` (
	`hotelName`,
	`price`,
	`score`,
	`number`,
	`address`,
	`introduction`,
	`pic`
)
VALUES
	(
		'如家',
		'999',
		'3',
		'99',
		'北京-市辖区-东城区',
		'很好的酒店',
		NULL
	);

INSERT INTO
`hotel` (
	`hotelName`,
	`price`,
	`score`,
	`number`,
	`address`,
	`introduction`,
	`pic`
)
VALUES
	(
		'如家2',
		'999',
		'3',
		'99',
		'北京-市辖区-东城区',
		'很好的酒店',
		NULL
	);

INSERT INTO
`hotel` (
	`hotelName`,
	`price`,
	`score`,
	`number`,
	`address`,
	`introduction`,
	`pic`
)
VALUES
	(
		'如家2',
		'999',
		'3',
		'99',
		'广东-深圳市-宝安区',
		'很好的酒店',
		NULL
	);

INSERT INTO
`hotel` (
	`hotelName`,
	`price`,
	`score`,
	`number`,
	`address`,
	`introduction`,
	`pic`
)
VALUES
	(
		'如家',
		'999',
		'3',
		'99',
		'广东-深圳市-宝安区',
		'很好的酒店',
		NULL
	);

INSERT INTO
`hotel` (
	`hotelName`,
	`price`,
	`score`,
	`number`,
	`address`,
	`introduction`,
	`pic`
)
VALUES
	(
		'如家',
		'999',
		'3',
		'99',
		'广东-深圳市-宝安区',
		'很好的酒店',
		NULL
	);

INSERT INTO
`flight` (
	`startingPlace`,
	`endPlace`,
	`startTime`,
	`endTime`,
	`flightNumber`,
	`price`,
	`flightName`,
	`number`
)
VALUES
	(
		'北京-市辖区-东城区',
		'北京-市辖区-东城区',
		'2019-05-04',
		'2019-05-18',
		'121',
		'111',
		'北京航空公司',
		'111'
	);

INSERT INTO
`flight` (
	`startingPlace`,
	`endPlace`,
	`startTime`,
	`endTime`,
	`flightNumber`,
	`price`,
	`flightName`,
	`number`
)
VALUES
	(
		'上海-县-崇明县',
		'贵州-贵阳市-白云区',
		'2019-05-01',
		'2019-05-15',
		'A00',
		'99',
		'北京航空公司',
		'100'
	);

INSERT INTO
`landscape` (
	`address`,
	`landscapeName`,
	`price`,
	`score`,
	`Introduction`,
	`pic`
)
VALUES
	(
		'安徽-黄山市-黄山区',
		'黄山',
		'99',
		'5',
		'黄山很好',
		NULL
	);

INSERT INTO
`landscape` (
	`address`,
	`landscapeName`,
	`price`,
	`score`,
	`Introduction`,
	`pic`
)
VALUES
	(
		'安徽-黄山市-黄山区',
		'黄山景区',
		'99',
		'5',
		'黄山很好',
		NULL
	);

INSERT INTO
`landscape` (
	`address`,
	`landscapeName`,
	`price`,
	`score`,
	`Introduction`,
	`pic`
)
VALUES
	(
		'广东-深圳市-宝安区',
		'平安大厦',
		'99',
		'5',
		'黄山很好',
		NULL
	);

INSERT INTO
`landscape` (
	`address`,
	`landscapeName`,
	`price`,
	`score`,
	`Introduction`,
	`pic`
)
VALUES
	(
		'广东-深圳市-福田区',
		'平安大厦',
		'99',
		'5',
		'黄山很好',
		NULL
	);

INSERT INTO `reply`
VALUES
	(
		'张三',
		'这是张三的回复',
		'2019-05-20',
		1,
		'GJUHKLHJFGHDFGNDFGNGHKGHJKHKHJKGHKVGJCNXCBVXFBXFH'
	);


INSERT INTO `post_record` (`postBy`, `postContent`, `postTitle`, `postTime`, `postPic`) VALUES ('admin', '官方网址：http://www.bootcss.com/p/bootstrap-wysiwyg/bootstrap-wysiwyg 为Bootstrap定制的微型所见即所得（What you see is what you get）富文本编辑器。这个jQuery Bootstrap小插件（5KB, < 200 行代码）可以将任何一个DIV转变成一个WYSIWYG富文本编辑器，灵感来自于 CLEditor 和 bootstrap-wysihtml5.下面是他的主要特色：在Mac和Wndows平台上能够自动针对常用操作绑定标准热键 可以通过拖拽插入图片；支持图片上传（也可以获取移动设备上的照片）语音识别输入（仅限Chrome浏览器） 允许自定义工具条；不生成额外标签；支持网站充分利用Bootstrap、Font Awesome等工具库的优秀特性 没有强制规定的样式 - 一切都由你做主 依赖浏览器的标准特性，没有非标准代码；工具条和键盘功能均可定制，并且能够执行任何浏览器支持的命令 不会自己创建一个单独的frame、备份文本区等 - 本编辑器尽量保持简单，并仅仅运行在一个DIV内 （可选）清除尾部空格；清除空的div和span必须运行在现代浏览器上（在Chrome 26、Firefox 19、Safari 6上经过测试，用户报告称可以在IE10上工作）支持移动设备浏览器（在iOS 6 Ipad/Iphone 和 Android 4.1.1 Chrome上测试过）', '云南大理一游', '2019-05-12 14:40:48', NULL);
INSERT INTO `post_record` (`postBy`, `postContent`, `postTitle`, `postTime`, `postPic`) VALUES ('admin', '官方网址：http://yuilibrary.com/YUI Editor 是雅虎的 YUI 包中的一个可视化HTML编辑器组件。', '土耳其三日游', '2019-05-12 14:45:01', NULL);

INSERT INTO `coupon` (`username`, `price`) VALUES ( 'fan', '100');
INSERT INTO `coupon` (`username`, `price`) VALUES ('wenzhihao', '200');



INSERT INTO `user_buy_record` (`productId`, `productType`,`userName`) VALUES ('1', 'hotel', 'fan');
INSERT INTO `user_buy_record` (`productId`, `productType`,`userName`) VALUES ('4', 'hotel', 'fan');
INSERT INTO `user_buy_record` (`productId`, `productType`,`userName`) VALUES ('1', 'hotel', 'fan');
INSERT INTO `user_buy_record` (`productId`, `productType`,`userName`) VALUES ('1', 'hotel', 'fan');
INSERT INTO `user_buy_record` (`productId`, `productType`,`userName`) VALUES ('1', 'hotel', 'fan');
INSERT INTO `user_buy_record` (`productId`, `productType`,`userName`) VALUES ('2', 'hotel', 'fan');
INSERT INTO `user_buy_record` (`productId`, `productType`,`userName`) VALUES ('2', 'hotel', 'fan');
INSERT INTO `user_buy_record` (`productId`, `productType`,`userName`) VALUES ('2', 'hotel', 'fan');
INSERT INTO `user_buy_record` (`productId`, `productType`,`userName`) VALUES ('4', 'hotel', 'fan');
INSERT INTO `user_buy_record` (`productId`, `productType`,`userName`) VALUES ('1', 'hotel', 'fan');
INSERT INTO `user_buy_record` (`productId`, `productType`,`userName`) VALUES ('4', 'hotel', 'fan');
INSERT INTO `user_buy_record` (`productId`, `productType`,`userName`) VALUES ('1', 'hotel', 'fan');
INSERT INTO `user_buy_record` (`productId`, `productType`,`userName`) VALUES ('1', 'hotel', 'fan');
INSERT INTO `user_buy_record` (`productId`, `productType`,`userName`) VALUES ('1', 'hotel', 'fan');
INSERT INTO `user_buy_record` (`productId`, `productType`,`userName`) VALUES ('1', 'hotel', 'fan');
INSERT INTO `user_buy_record` (`productId`, `productType`,`userName`) VALUES ('1', 'hotel', 'fan');
INSERT INTO `user_buy_record` (`productId`, `productType`,`userName`) VALUES ('3', 'landscape', 'fan');




INSERT INTO `reply` (`replyBy`, `replyContent`,`replyTime`,`replyPostId`,`postPic`) VALUES ('张三', '这是张三的回复', '2019-05-20', 1, 'GJUHKLHJFGHDFGNDFGNGHKGHJKHKHJKGHKVGJCNXCBVXFBXFH');
INSERT INTO `reply` (`replyBy`, `replyContent`,`replyTime`,`replyPostId`,`postPic`) VALUES ('fan', '你好', '2019-05-12 16:37:34', 8, NULL);
INSERT INTO `reply` (`replyBy`, `replyContent`,`replyTime`,`replyPostId`,`postPic`) VALUES ('fan', '你好', '2019-05-12 16:37:39', 8, NULL);
INSERT INTO `reply` (`replyBy`, `replyContent`,`replyTime`,`replyPostId`,`postPic`) VALUES ('fan', '你好', '2019-05-12 16:37:41', 8, NULL);
INSERT INTO `reply` (`replyBy`, `replyContent`,`replyTime`,`replyPostId`,`postPic`) VALUES ('fan', '你好', '2019-05-12 16:38:26', 11, NULL);
INSERT INTO `reply` (`replyBy`, `replyContent`,`replyTime`,`replyPostId`,`postPic`) VALUES ('fan', '你好', '2019-05-12 16:38:28', 11, NULL);