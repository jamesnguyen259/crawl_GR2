$(document).ready(function(){
        var map;
        var mapLat = 21.028511;
        var mapLng = 105.804817;
        var mapDefaultZoom = 15;
        map = new ol.Map({
            target: "map",
            layers: [
                new ol.layer.Tile({
                    source: new ol.source.OSM({
                    url: "https://a.tile.openstreetmap.org/{z}/{x}/{y}.png"
                    })
                })
            ],
            view: new ol.View({
                center: ol.proj.fromLonLat([mapLng, mapLat]),
                zoom: mapDefaultZoom
            })
        });

        $('#addMarker').on('click', function(){
            $.ajax({
              type: "GET",
              url: 'http://localhost:3000/out3.json',
              error: function() {
                  $('#info').html('<p>An error has occurred</p>');
              },
              success: function(data){
                for(var i = 0; i< data.length; i++){
                    var vectorLayer = new ol.layer.Vector({
                    source:new ol.source.Vector({
                    features: [new ol.Feature({
                    geometry: new ol.geom.Point(ol.proj.transform([parseFloat(data[i].lng), parseFloat(data[i].lat)], 'EPSG:4326', 'EPSG:3857')),
                    })]
                    }),
                    style: new ol.style.Style({
                        image: new ol.style.Icon({
                        anchor: [0.5, 0.5],
                        anchorXUnits: "fraction",
                        anchorYUnits: "fraction",
                        src: "http://maps.google.com/mapfiles/ms/icons/blue.png"
                        })
                        })
                    });
                    map.addLayer(vectorLayer);
                }
              }
            });
        });
});
