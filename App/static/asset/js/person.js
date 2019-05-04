layui.use(['http', 'api'],
function(exports){

var HTTP = layui.http;
var API = layui.api;


new Vue({
	data: {
		status: 'view' // view - edit
	},
	el: '#app',
	computed: {
		useInfo: function() {
			var info = window.sessionStorage.getItem('useInfo');
			try {
				info = JSON.parse(info);
			} catch(e) {
				info = {};
			}
			return info;
		}
	},
	methods: {
		getUser: function() {
			var info = window.sessionStorage.getItem('useInfo');
			return info;
		},
		changeEdit: function() {
			this.status = 'edit';
		},
		save: function() {
			var _this = this;
			console.log(this.useInfo);
			HTTP.ajax({
				url: API.updateUser,
				data: this.useInfo,
				success: function(res) {
					layer.msg('保存成功');
					_this.status = 'view';
				}
			})
		}
	},
	created: function() {
		var usr = this.getUser();
		if (!usr) {
			window.location.href = 'login.html';
		}
	}
})





}); 