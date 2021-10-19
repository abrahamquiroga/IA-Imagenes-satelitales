require(["esri/config","esri/Map", "esri/views/MapView"], function (esriConfig,Map, MapView) {
    esriConfig.apiKey = "AAPK5c5a8ece12214f40bc6e26716c031b6bxdGRfHT0VxMHAIp2xDtb2PDhsj3ASGxazyLElM3-0uo-8VXSftrtTHi6EWYCNcIy";

    const map = new Map({
      basemap: "arcgis-topographic" // Basemap layer service
    });

    const view = new MapView({
      map: map,
      center: [-118.805, 34.027], // Longitude, latitude
      zoom: 13, // Zoom level
      container: "viewDiv" // Div element
    });
  });

  /* leaflef */

var mymap = L.map('mapid').setView([-16.130,-64.534], 6);
L.tileLayer('https://a.tile.openstreetmap.org/{z}/{x}/{y}.png', {
	maxZoom: 15,
}).addTo(mymap);

document.getElementById("select-location").addEventListener('change', function(e){
    coords = e.target.value.split(","),
    mymap.flyTo(coords, 13)
});