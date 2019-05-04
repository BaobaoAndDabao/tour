function loadScript(url, fn) {
  var script = document.createElement("script");
  script.type = "text/javascript";
  script.src = url;
  document.body.appendChild(script);
  script.onload = script.onreadystatechange = function () {
    fn && fn();
  }
};

var navHtml = `
<ul class="layui-nav layui-bg-blue" lay-filter="">
  <li class="layui-nav-item">
    <a href="">预定</a>
    <dl class="layui-nav-child">
      <dd><a href="flyInfo.html" class="layui-this">机票</a></dd>
      <dd><a href="">酒店</a></dd>
      <dd><a href="" >景点门票</a></dd>
    </dl>
  </li>
  <li class="layui-nav-item"><a href="#/raiders">热门攻略</a></li>
  <li class="layui-nav-item"><a href="">推荐</a></li>
  <li class="layui-nav-item"><a href="">社区交流</a></li>
  <li class="layui-nav-item"><a href="">资源共享</a></li>
  <li class="layui-nav-item"><a href="person.html">个人中心</a></li>
</ul>
`;

loadScript('./lib/layui/layui.js');
loadScript('./js/xadmin.js');
loadScript('./js/cookie.js');
$("body").prepend(navHtml);