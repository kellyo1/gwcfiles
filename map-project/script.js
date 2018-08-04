var ourLocation;
var map;
var view;

function init(){
  ourLocation= ol.proj.fromLonLat([-122.416647,37.777051]);  //Twitter HQ

  view= new ol.View({
    center: ourLocation,
    zoom: 6
  });

  map= new ol.Map({
    target: 'map',
    layers:[
      new ol.layer.Tile({
        source:new ol.source.OSM(),
      })
    ],view: view

  });
}

function panHome(){
  view.animate({
    center: ourLocation,
    duration:2000 //two seconds
  });
}

function panToLocation(){
  var countryName = document.getElementById("country-name").value;

  var query = "https://restcountries.eu/rest/v2/name/"+countryName;

  var lon = 0.0;
  var lat = 0.0;

  query = query.replace(/ /g, "%20");
  alert(query);

  // Make an HTTP GET Request
  var countryRequest = new XMLHttpRequest();
  countryRequest.open('GET', query, false);

  countryRequest.send();


  //alert("Ready State "+ countryRequest.readyState);

  var countryInformation = JSON.parse(countryRequest.responseText);

  var lat = countryInformation[0].latlng[0];
  var lon = countryInformation[0].latlng[1];

  var location = ol.proj.fromLonLat([lon, lat]);

  view.animate({
    center: location,
    duration:2000 //two seconds
  });
}

window.onload =init;
