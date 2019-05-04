layui.define(function(exports){


var publicAPI = {
  login: '/user/login',
  updateUser: 'mock/updateUser.php',
  search: 'mock/search.php',
  searchHotel: 'mock/searchHotel.php'
};


exports('api', publicAPI);

}); 