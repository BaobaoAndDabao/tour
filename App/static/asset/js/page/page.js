
// 插件开发者---柴柴胖子

(function($,undefined){

	$.fn.page = function(obj){

		// 实现几个底层的工具方法

		var btnShow = new BtnShow();

		var pageArrive = new PageArrive();

		var utils = new Utils();

		//全局变量
		var param = {

			// 语言的设置
			olang:obj['olang'],

			// 接收的json数据
			data:obj['info']['data'],

			//缓存当前页的数据
			dataLast:{},

			// 点击的页码
			pageIndex:(obj['info']['pageIndex']==0?1:obj['info']['pageIndex']),

			// 显示的的条数
			pageCount:obj['info']['pageCount'],

			//数据总共的页数
			pageNum:0,

			//生成html的根节点的$对象
			pageNode:null,

			//生成页码容器的根节点的$对象
			pageIndexNode:null,

			//按钮长度，默认为5 
			btnLen:(obj['btnLen']==undefined?5:obj['btnLen']),

			//返回数据的回调函数
			callBack:obj['fn'],

			//接收的排序方法
			sort:obj['sort'],

			//筛选的条件(数组)
			fitler:obj['fitler'],

			// 是否执行筛选
			bFitler:(obj['bFiter']==undefined?false:obj['bFiter'])

		};

		/*================ 一、数据过滤 ===================*/

		/*  1. 筛选的实现,前面执行效率最高*/
		(function(bFitler,ArrFitler,data){
			if( bFitler && (!!ArrFitler) ){
				// console.log(ArrFitler);
				param.data = utils.fitler(ArrFitler,data);
			}
		})(param.bFitler,param.fitler,param.data);

		/*  2.  排序的方法，必须首先执行*/
		(function(fn,data){
			//如果排序方法有传入，则执行排序方法
			if(!!fn){
				var sortRtn = fn(data);
				var key = sortRtn.key;
				var method =sortRtn.method;
				// var sort =  new Sort(data,key);
				if( method == 1){
					//实现正排序;
					param.data = utils.sortSevice.plus(data,key);
				}
				else if( method == -1){
					//实现逆排序
					param.data = utils.sortSevice.minus(data,key);
				}
				else if( method == 'p'){
					param.data = utils.sortSevice.plus_US(data,key);
				}
				else if( method == 'm'){
					param.data = utils.sortSevice.minus_US(data,key);
				}
				else if( method == 0 ){
					// 实现不排序
					param.data = utils.sortSevice.defau(data,key);
				}
				else{
					// 按顾客的要求排序
					param.data = fn(data);
				}
			}
		})(param.sort,param.data);


		/* 3.数据过滤后计算出总共的页数*/
		param.pageNum = Math.ceil(param.data.length/param.pageCount);


		/*================ 二、html结构的加载 ===================*/

		/*  1、绘制外头根容器  */
		(function(num,_this){
			_this.addClass('i_page_js_out_content');
			var strHtml = '<div class="i_page_js_in_content">\
								<div class="page_js">\
									<span class="last">&lt;&lt</span>\
									<span class="fir_num">1</span>\
									<span class="lastElips">...</span>\
									<div class="numContent">\
									</div>\
									<span class="nextElips">...</span>\
									<span class="next_num">'+ num +'</span>\
									<span class="next">&gt;&gt</span>\
								</div>\
							</div>';
			_this.html(strHtml);
		})(param.pageNum,this);

		//将节点存住
		param.pageNode = $(this).find('.page_js');
		param.pageIndexNode = $(this).find('.numContent');

		
		var dataLen = param.data.length;//数据长度
		var showLen = 0;//按钮的显示长度
		var showAllBtn = true;//页码是否足够按钮长度 true为够

		/*  2.加载页码的div */
		(function(pageIndexNode,btnLen){
			var btnStr = '';
			if (dataLen / param.pageCount >= btnLen){
				showLen = btnLen;
				showAllBtn = true;
			}
			else if (dataLen / param.pageCount < btnLen){
				showLen = Math.ceil(dataLen/btnLen);
				showAllBtn = false;
			}
			for(var i = 0 ; i < showLen ; i++){
				if( i == 0){
					btnStr += '<span class="num first" data_num = "' + ( i*1 + 1 ) + '">' + ( i*1 + 1 ) + '</span>';
				}else if(i == (showLen-1)){
					btnStr += '<span class="num end" data_num = "' + ( i*1 + 1 ) + '">' + ( i*1 + 1 ) + '</span>';
				}else{
					btnStr += '<span class="num" data_num = "' + ( i*1 + 1 ) + '">' + ( i*1 + 1 ) + '</span>';
				}
			}
			pageIndexNode.html(btnStr);
		})(param.pageIndexNode,param.btnLen);
		

		/*============== 三、 事件的绑定=================*/

		/*--- 1、页码点击事件---*/
		param.pageIndexNode.find('span').on('click',function(fn){
			var $this = $(this);
			param.pageIndexNode.find('span').removeClass('on');
			$this.addClass('on');

			var rtnJson = utils.returnJsonData();

			//提供一个回调函数的对外方法
			//这是插件的核心之一
			fn = param.callBack;
			if(!!param.callBack){
				fn(rtnJson);
			}
		});

		/*--- 2 、上一页点击事件---*/
		param.pageNode.find('.last').on('click',function(){
			var rtnJson = pageArrive.gotoLast();
			//提供一个回调函数的对外方法
			//这是插件的核心之一
			fn = param.callBack;
			if(!!param.callBack){
				fn(rtnJson);
			}
		});


		/*--- 3 、下一页点击事件---*/
		param.pageNode.find('.next').on('click',function(){
			var rtnJson = pageArrive.gotoNext();
			//提供一个回调函数的对外方法
			//这是插件的核心之一
			fn = param.callBack;
			if(!!param.callBack){
				fn(rtnJson);
			}
		});

		/*--- 4 、首页点击事件---*/
		param.pageNode.find('.fir_num').on('click',function(){
			btnShow.showFristBtn();
			param.pageIndexNode.find('.first').trigger('click');
			
		});

		/*--- 5 、尾页点击事件---*/
		param.pageNode.find('.next_num').on('click',function(){
			debugger;
			btnShow.showLastBtn();
			param.pageIndexNode.find('.end').trigger('click');
			
		});

		/*--- 6 、检查按钮的显示点击事件---*/
		param.pageNode.find('span').on('click',function(){
			pageArrive.controllShowAndHide();
		});



		/*============== 四、 默认加载的事件=================*/

		/* 1. 根据传入的参数默认的一个点击行为  */
		(function(pageNum,pageIndex,pageIndexNode){
			var firBtnLen = showLen;
			var lastBtnLen = pageNum - showLen;
			if(pageIndex <= firBtnLen){
				// 表示能在前五个按钮找到
				btnShow.showFristBtn();
			}else if(pageIndex > lastBtnLen){
				// 表示能在最后五个按钮找到
				btnShow.showLastBtn()
			}else{
				// 表示能在中间找到
				btnShow.showMidBtn(pageIndex);
			}
			pageIndexNode.find('span.num').each(function(){
				var $this = $(this);
				var dataTemp = $this.attr('data_num');
				if(dataTemp==pageIndex){
					$this.trigger('click');
				}
			});

			//最后检查一下左右的显隐
			pageArrive.controllShowAndHide();

		})(param.pageNum,param.pageIndex,param.pageIndexNode);



		

		
		/*============== 五、 底层的工具类 =================*/


		/*------1、展示按钮类--------*/
		function BtnShow(){
			//显示开始几个按钮的方法
			this.showFristBtn = function(){
				param.pageIndexNode.find('span.num').each(function(i){
					var $this = $(this);
					$this.text( i*1 + 1 );
					$this.attr('data_num',(i*1 + 1 ));
				});
			}
			//显示最后一个按钮的方法
			this.showLastBtn = function(){
				var lastBtnLen = param.pageNum - showLen;
				param.pageIndexNode.find('span.num').each(function(i){
					var $this = $(this);
					$this.text( i*1 + lastBtnLen + 1);
					$this.attr('data_num',(i*1 + lastBtnLen + 1));
				});
			}
			//显示中间按钮的方法
			this.showMidBtn = function(pageIndex){
				param.pageIndexNode.find('span.num').each(function(i){
					var $this = $(this);
					$this.text( i*1 + pageIndex );
					$this.attr('data_num',(i*1 + pageIndex ));
				});
			}
		}



		/*----- 2、到达某一页的类------*/
		function PageArrive(){
			//到达上一页的方法
			this.gotoLast = function (){
				var rtnJson;
				var thisInfo  = utils.getCurrentPageInfo();
				//组织越界的光标移动
				if($(thisInfo.dom).prev().length !== 0){
					$(thisInfo.dom).removeClass('on').prev().addClass('on');
				}
				else{
					if(thisInfo.num == 1){
						//到达临界值不做反应
					}else{
						param.pageIndexNode.find('span.num').each(function(){
							var $this = $(this);
							var dataTemp = $this.attr('data_num');
						
							$this.text( dataTemp*1 - 1 );
							$this.attr('data_num',(dataTemp*1 - 1 ));
						});
					}
				}
				rtnJson = utils.returnJsonData();
				return rtnJson;
			}
			//到达下一页的方法
			this.gotoNext = function(){
				var rtnJson;
				var thisInfo  = utils.getCurrentPageInfo();
				//组织越界的光标移动
				if($(thisInfo.dom).next().length !== 0){
					$(thisInfo.dom).removeClass('on').next().addClass('on');
				}
				else{
					if(thisInfo.num >= param.pageNum){
						//到达临界值不做反应
					}else{
						param.pageIndexNode.find('span.num').each(function(){
							var $this = $(this);
							var dataTemp = $this.attr('data_num');
						
							$this.text( dataTemp*1 + 1 );
							$this.attr('data_num',(dataTemp*1 + 1 ));
						});
					}
					
				}
				rtnJson = utils.returnJsonData();
				return rtnJson;
			}
			//控制左右省略显隐的方法
			this.controllShowAndHide = function(){
				var hasFri = false;
				var hasLast = false;
				if(!showAllBtn){
					param.pageNode.find('.fir_num').hide();
					param.pageNode.find('.lastElips').hide();
					param.pageNode.find('.nextElips').hide();
					param.pageNode.find('.next_num').hide();
					return;
				}
				showAllBtn&&param.pageIndexNode.find('span.num').each(function(i){
					var $this = $(this);
					var dataTemp = $this.attr('data_num');
					if(dataTemp == 1){
						hasFri = true;
					}
					if(dataTemp == param.pageNum){
						hasLast = true;
					}
				});
				if(hasFri){
					param.pageNode.find('.fir_num').hide();
					param.pageNode.find('.lastElips').hide();
				}else{
					param.pageNode.find('.fir_num').show();
					param.pageNode.find('.lastElips').show();
				}
				if(hasLast){
					param.pageNode.find('.nextElips').hide();
					param.pageNode.find('.next_num').hide();
				}else{
					param.pageNode.find('.nextElips').show();
					param.pageNode.find('.next_num').show();
				}
			}
		}


		/*----- 3、工具方法的类------*/		
		function Utils(){
			// 1.得到当前页码和dom节点信息的私有函数
			this.getCurrentPageInfo = function(){
				var rtnNum;
				var rtnDom;
				var numArrSpan = param.pageIndexNode.find('.num');
				for( var i = 0 ; i < numArrSpan.length ; i++ ){
					if($(numArrSpan[i]).hasClass('on')){
						rtnDom = numArrSpan[i];
						rtnNum = $(numArrSpan[i]).attr('data_num');
						break;
					}
				}
				return {
					num:rtnNum,
					dom:rtnDom
				}
			}

			//2.截断数据的方法
			this.returnJsonData = function(){
				var thisInfo  = utils.getCurrentPageInfo();
				var num_this = thisInfo.num;
				var rtnJson = [];

				/*------缓存机制----------*/
				if(num_this != undefined){
					param.dataLast.num_this = num_this;
				}
				if(num_this == undefined){
					num_this = param.dataLast.num_this;
				}

				// console.log((num_this - 1)*param.pageCount + '|' + (num_this)*param.pageCount);

				// 数据的裁剪
				for(var i = (num_this - 1)*param.pageCount ; i < (num_this)*param.pageCount ; i++ ){
					if(param.data[i] == undefined){

					}else{
						rtnJson.push(param.data[i]);
					}
				}
				/*------缓存机制----------*/
				//将运行结果的有效数据缓存
				if(rtnJson.length !== 0){
					param.dataLast.rtnJson = rtnJson;
				}
				// 页码无效时启用上次的缓存数据
				if(rtnJson.length == 0){
					rtnJson = param.dataLast.rtnJson;
				}
				return rtnJson;
			}

			// 3.排序的方法
			this.fitler = function(ArrFitler,data){
				var rtnData = [];
				// if()
				for(var i = 0 , len = data.length ; i < len ; i++){
					var aLen = ArrFitler.length;
					var fullMark = 0;//判断条件是否积满
					for(var j = 0 ; j < aLen ; j++){
						var key = ArrFitler[j]['key'];
						var val = ArrFitler[j]['val'];
						if(data[i][key] == val){
							fullMark++;
						}
						if(fullMark == aLen){
							rtnData.push(data[i]);
						}
					}
				}
				return rtnData;
			}

			// 排序的类在上层实现
			this.sortSevice = new  Sort();

		}


		/*============== 六、 更底层的工具类  实现在上一层 =================*/
		//排序工具
		function Sort(){
			//正序方法
			this.plus = function (arr,key){
				for(var i = 0 , len = arr.length ; i < len ; i++){
					for(var j = 0 , len = arr.length ; j < len - i - 1; j++){
						if(arr[j][key]/1 > arr[j+1][key]/1){
							var temp =  arr[j];
							arr[j] = arr[j+1];
							arr[j+1] = temp;
						}
					}
				}
				return arr;
			}
			//字母正序方法
			this.plus_US = function (arr,key){
				for(var i = 0 , len = arr.length ; i < len ; i++){
					for(var j = 0 , len = arr.length ; j < len - i - 1; j++){
						if(arr[j][key] > arr[j+1][key]){
							var temp =  arr[j];
							arr[j] = arr[j+1];
							arr[j+1] = temp;
						}
					}
				}
				return arr;
			}
			//逆序方法
			this.minus = function (arr,key){
				for(var i = 0 , len = arr.length ; i < len ; i++){
					for(var j = 0 , len = arr.length ; j < len - i - 1; j++){
						if(arr[j][key]/1 < arr[j+1][key]/1){
							var temp =  arr[j];
							arr[j] = arr[j+1];
							arr[j+1] = temp;
						}
					}
				}
				return arr;
			}
			//字母逆序方法
			this.minus_US = function (arr,key){
				for(var i = 0 , len = arr.length ; i < len ; i++){
					for(var j = 0 , len = arr.length ; j < len - i - 1; j++){
						if(arr[j][key] < arr[j+1][key]){
							var temp =  arr[j];
							arr[j] = arr[j+1];
							arr[j+1] = temp;
						}
					}
				}
				return arr;
			}			
			//默认排序
			this.defau = function(arr,key){
				return arr;
			}
		}


		/*============== 七、 返回值，实现$的链式调用=================*/
		param.pageIndexNode.find('.first').trigger('click');
		return this;
	}

})(jQuery,undefined);


