layui.define(function(exports){

exports('api', {
  login: '/user/login',
  updateUser: '/user/update',
  searchFlight: '/flight/search',
  searchHotel: '/hotel/search',
  searchLandscape: '/landscape/search',
  insertflight: '/flight/insert',
  insertHotel: '/hotel/insert',
  insertScape: '/landscape/insert',
  queryAllLandscape: '/landscape/queryAll',
  queryAllHotel: '/hotel/queryAll',
  queryAllFlight: '/flight/queryAll',
  buyFlight: '/flight/buy',
    buyHotel: '/hotel/buy',
  sendRecommend: '/recommend/send',
  raidersRecommend: '/recommend/raiders'
});

}); 