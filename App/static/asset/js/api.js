layui.define(function(exports){


var publicAPI = {
  login: '/user/login',
  updateUser: '/user/update',
  search: 'mock/search.php',
  searchHotel: 'mock/searchHotel.php'
};


exports('api', publicAPI);

}); 