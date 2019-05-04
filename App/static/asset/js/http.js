layui.define(function(exports){



// ajax切面
function ajax(param) {
  // var form = new FormData()
  // var data = param.data || {};
  // debugger;
  // for (var props in data) {
  //   form.append(props, data[props]);
  // }
  return $.ajax({
    url: param.url,
    data: param.data,
    type: 'POST',
    dataType: "json",
    contentType: "application/x-www-form-urlencoded;charset=UTF-8",
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