$(document).ready(function(){
        map = new OpenLayers.Map("mapdiv");
        map.addLayer(new OpenLayers.Layer.OSM());
        var lonLat = new OpenLayers.LonLat(105.804817,21.028511).transform(
            new OpenLayers.Projection("EPSG:4326"),
            map.getProjectionObject()
        );
        var zoom=16;
        // var markers = new OpenLayers.Layer.Markers( "Markers" );
        // map.addLayer(markers);
        // markers.addMarker(new OpenLayers.Marker(lonLat));
        map.setCenter (lonLat, zoom);
        epsg4326 =  new OpenLayers.Projection("EPSG:4326"); //WGS 1984 projection
        projectTo = map.getProjectionObject(); //The map projection (Spherical Mercator)
        var vectorLayer = new OpenLayers.Layer.Vector("Overlay");

        $('#addMarker').on('click', function(){
            $.ajax({
              type: "GET",
              url: 'http://localhost:3000/out3.json',
              error: function() {
                  $('#info').html('<p>An error has occurred</p>');
              },
              success: function(data){
                for(var i = 0; i< data.length; i++){
                    // var pos = new OpenLayers.LonLat(data[i].lng, data[i].lat).transform(
                    //     new OpenLayers.Projection("EPSG:4326"),map.getProjectionObject());
                    // markers.addMarker(new OpenLayers.Marker(pos));
                    var feature = new OpenLayers.Feature.Vector(
                    new OpenLayers.Geometry.Point( data[i].lng, data[i].lat ).transform(epsg4326, projectTo),
                    {description: data[i].event_name + "<br>" + "on " + data[i].event_time + "<br>" + "at " + data[i].event_place} ,
                    {externalGraphic: 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png', graphicHeight: 25, graphicWidth: 21, graphicXOffset:-12, graphicYOffset:-25  }
                    );
                    vectorLayer.addFeatures(feature);
                }
                map.addLayer(vectorLayer);

                //Add a selector control to the vectorLayer with popup functions
                var controls = {
                selector: new OpenLayers.Control.SelectFeature(vectorLayer, { onSelect: createPopup, onUnselect: destroyPopup })
                };

                function createPopup(feature) {
                    feature.popup = new OpenLayers.Popup.FramedCloud("pop",
                    feature.geometry.getBounds().getCenterLonLat(),
                    null,
                    '<div class="markerContent">'+feature.attributes.description+'</div>',
                    null,
                    true,
                    function() { controls['selector'].unselectAll(); }
                    );
                    //feature.popup.closeOnMove = true;
                    map.addPopup(feature.popup);
                }

                function destroyPopup(feature) {
                    feature.popup.destroy();
                    feature.popup = null;
                }

                map.addControl(controls['selector']);
                controls['selector'].activate();
              }
            });
        });
});
