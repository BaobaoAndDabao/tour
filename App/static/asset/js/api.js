layui.define(function(exports){


var publicAPI = {
  login: '/user/login',
  updateUser: '/user/update',
  searchFlight: '/flight/search',
  searchHotel: 'mock/searchHotel.php',
  insertflight: '/flight/insert'
};


exports('api', publicAPI);

}); 