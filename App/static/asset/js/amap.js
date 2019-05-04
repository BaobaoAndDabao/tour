


layui.define(function (exports) {

  function loadMap(fn) {
    var script = document.createElement("script");
    script.type = "text/javascript";
    script.src = "https://webapi.amap.com/maps?v=1.4.8&key=a42f8fc982b7fcf299e5c4579ab2c419";
    document.body.appendChild(script);
    script.onload = script.onreadystatechange = function () {
      fn(window.AMap);
    }
  };


  function getLocalCity(fn) {
    var loaclCity = window.localStorage.getItem('loaclCity');
    if (loaclCity) {
      return fn(JSON.parse(loaclCity));
    }
    loadMap(function (AMap) {
      AMap.plugin('AMap.CitySearch', function () {
        var citySearch = new AMap.CitySearch()
        citySearch.getLocalCity(function (status, result) {
          if (status === 'complete' && result.info === 'OK') {
            window.localStorage.setItem('loaclCity', JSON.stringify(result));
            fn(result);
          }
        })
      });
    });
  }


  exports('amap', {
    getLocalCity: getLocalCity
  });

}); 