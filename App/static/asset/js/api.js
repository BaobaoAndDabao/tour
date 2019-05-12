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
  buyLandscape: '/landscape/buy',
  sendRecommend: '/recommend/send',
  raidersRecommend: '/recommend/raiders',
  queryAllPostRecord: '/postRecord/queryAll',
  queryByPostRecordId: '/postRecord/queryByPostRecordId',
  insertPostRecord: '/postRecord/insert',
  replyPostRecord: '/postRecord/reply',
  deletePostRecord: '/postRecord/delete',
  queryByUserCoupon: '/coupon/queryByUser',
  getShareCoupon: '/coupon/getShareCoupon'
});

}); 