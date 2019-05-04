layui.define(function(exports){



// ajax切面
function ajax(param) {
  layer.msg('玩命卖萌中');
  return $.ajax({
    url: param.url,
    data: param.data,
    type: 'POST',
    dataType: "json",
    success: function(response) {
      if (response.code != 0) {
        layer.msg('请求失败,稍后再试');
      } else {
        param.success(response.data);
      }
    }
  });
};


  
//输出test接口
exports('http', {
  ajax: ajax
});

}); 