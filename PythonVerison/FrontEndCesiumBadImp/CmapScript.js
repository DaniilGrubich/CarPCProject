Cesium.Ion.defaultAccessToken = 'XXX';
var viewer = new Cesium.Viewer('cesiumContainer', {
    imageryProvider : new Cesium.OpenStreetMapImageryProvider({
        url : 'https://a.tile.openstreetmap.org/'
    }),
    baseLayerPicker : true
});

// viewer.animation.container.style.visibility = 'hidden';
// viewer.timeline.container.style.visibility = 'hidden';
// viewer._cesiumWidget._creditContainer.style.display = "none";
// viewer.imager
// viewer.forceResize();

let vehicle = viewer.entities.add({
    position : Cesium.Cartesian3.fromDegrees(-83.425199, 42.614384, 1), // Initial position
    point : {
        pixelSize : 10,
        color : Cesium.Color.RED
    }
});

let prevPosition = vehicle.position.clone();
let nextPosition = vehicle.position.clone();
let dt = 1;
let t = 0;

viewer.camera.flyTo({
    destination : Cesium.Cartesian3.fromDegrees(-83.425199, 42.614384 , 50.0)
});





viewer.scene.preRender.addEventListener(function(scene, time) {
    if (t <= dt) {
        let newPosition = Cesium.Cartesian3.lerp(prevPosition, nextPosition, t / dt);
        vehicle.position = newPosition;
        t += scene.frameState.deltaTime * 0.001; // deltaTime is in milliseconds
    } else {
        vehicle.position = nextPosition; // Make sure the vehicle reaches the next position
    }
});

// viewer.trackedEntity = trackedEntity;
