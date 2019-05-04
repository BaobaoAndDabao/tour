layui.use(['http', 'api'],
function(exports){

var HTTP = layui.http;
var API = layui.api;


function login() {

 	layui.use('form', function(){
	  var form = layui.form;
	  //监听提交
	  form.on('submit(login)', function(data){
	    HTTP.ajax({
				url: API.login,
				data: {
					userName: '222',
					password: '1334'
				},
	    	success: function(res) {
	    		if (!isSuccess(res)) {
	    			layer.msg('用户名或密码错误');
	    			return;
	    		};
	    		window.sessionStorage.setItem('useInfo', JSON.stringify(res));

	    		if (res.type == 'admin') {
	    			window.location.href = 'admin.html';
	    		} else {
	    			window.location.href = 'person.html';
	    		}
	    	}
	    });

	   return false;
	  });
	});
};


// 判断登录是否成功
function isSuccess(info) {
	return info && info.userName;
};



login();

}); 