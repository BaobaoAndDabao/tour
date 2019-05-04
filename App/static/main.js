// 模块化别名配置
layui.config({
  base: 'static/asset/js/' //假设这是你存放拓展模块的根目录
});

goLogin();

/**
 * 判断是否登录
 */
function isLogin() {
  var info = window.sessionStorage.getItem('useInfo');
  if (!info) return false;
  try {
    info = JSON.parse(info);
  } catch (e) {
    info = null;
  }
  return !!info;
};


function isLoginPage() {
  var href = window.location.href;
  var result = false;
  if (href.indexOf('login.html') > -1) {
    result = true;
  };
  return result;
}
/**
 * 跳登录
 */
function goLogin() {
  var islogin = isLogin();
  if (!islogin && !isLoginPage()) {
    window.location.href = 'login.html';
  }
}

