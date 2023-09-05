// mapboxgl.accessToken = 'XXX';
var darkMap = false;

const map = new mapboxgl.Map({
    container: 'mapContainer', // container ID
    // Choose from Mapbox's core styles, or make your own style with Mapbox Studio
    style: 'mapbox://styles/mapbox/navigation-day-v1', // style URL for dark theme, // style URL
    center: [-11, 11], // starting position [lng, lat]
    zoom: 18// starting zoom
});
 

map.on('style.load', () => {
    // Insert the layer beneath any symbol layer.
    const layers = map.getStyle().layers;
    const labelLayerId = layers.find(
    (layer) => layer.type === 'symbol' && layer.layout['text-field']
    ).id;
     
    // The 'building' layer in the Mapbox Streets
    // vector tileset contains building height data
    // from OpenStreetMap.
    map.addLayer(
    {
        'id': 'add-3d-buildings',
        'source': 'composite',
        'source-layer': 'building',
        'filter': ['==', 'extrude', 'true'],
        'type': 'fill-extrusion',
        'minzoom': 15,
        'paint': {
            'fill-extrusion-color': '#aaa',
        
            // Use an 'interpolate' expression to
            // add a smooth transition effect to
            // the buildings as the user zooms in.
            'fill-extrusion-height': [
                'interpolate',
                ['linear'],
                ['zoom'],
                15,
                0,
                15.05,
                ['get', 'height']
            ],
            'fill-extrusion-base': [
                'interpolate',
                ['linear'],
                ['zoom'],
                15,
                0,
                15.05,
                ['get', 'min_height']
            ],
            'fill-extrusion-opacity': 0.6
        }
    },
    labelLayerId
    );
});

var marker = new mapboxgl.Marker()
  .setLngLat([-83.425199, 42.614384])
  .addTo(map);

 

// Declare variables
var lastLat, lastLon;
var animateMarker;
 // Calculate bearing between two points
function calculateBearing(startLat, startLon, endLat, endLon){
    var y = Math.sin(endLon - startLon) * Math.cos(endLat);
    var x = Math.cos(startLat) * Math.sin(endLat) - Math.sin(startLat) * Math.cos(endLat) * Math.cos(endLon - startLon);
    var bearing = Math.atan2(y, x) * 180 / Math.PI;
    return (bearing + 360) % 360;
}
 // Move the marker smoothly to a new position
function moveMarker(marker, newLat, newLon, duration, speed) {
    var startPoint = marker.getLngLat();
    var endPoint = new mapboxgl.LngLat(newLon, newLat);
    var startTime = Date.now();
    var endTime = startTime + duration;

    var animateMarker = function() {
        var now = Date.now();
        var timePoint = (now - startTime) / duration; // Normalized time point in animation, from 0 to 1
        var lnglat = new mapboxgl.LngLat(
            startPoint.lng + (endPoint.lng - startPoint.lng) * timePoint,
            startPoint.lat + (endPoint.lat - startPoint.lat) * timePoint
        );
        marker.setLngLat(lnglat);
            // Define zoom level based on speed
        var zoomLevel;
        if (speed <= 30) {
            zoomLevel = 18; // Zoomed in more when speed is slow
        } else if (speed <= 60) {
            zoomLevel = 17;
        } else {
            zoomLevel = 12; // Zoomed out when speed is fast
        }
            // Fly to the new position with appropriate zoom and bearing
            if (zoomLevel == 18) {
            map.flyTo({center: lnglat, zoom: zoomLevel, bearing: 0, pitch: 0});
            } else {
                map.flyTo({center: lnglat, zoom: zoomLevel, bearing: calculateBearing(startPoint.lat, startPoint.lng, endPoint.lat, endPoint.lng), pitch: 60});
        }
        if (now < endTime) {
            // If the animation hasn't finished yet, schedule the next frame
            requestAnimationFrame(animateMarker);
        }
    }

    // Start the animation
    requestAnimationFrame(animateMarker);
}

 // Update the marker's position
function updateMarkerPosition(lat, lon, speed) {
    // If we have a last known position, animate the movement from there
    if (lastLat !== undefined && lastLon !== undefined) {
        moveMarker(marker, lat, lon, 1000, speed);  // Move smoothly to new position over 1 second
    } else {
        // If we don't have a last known position, just set the marker position
        marker.setLngLat([lon, lat]);
    }
    // Update last known position
    lastLat = lat;
    lastLon = lon;
} 

