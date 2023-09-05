function changeStyleButtonCallback(){
    console.log("changeStyle clicked");
    if(darkMap){
        map.setStyle('mapbox://styles/mapbox/navigation-day-v1');
    }else{
        map.setStyle('mapbox://styles/mapbox/navigation-night-v1');
    }
    darkMap = !darkMap;
}

function carMonitorButtonCallback(){
    console.log("changeMonitor clicked");
}

function settingsButtonCallback(){
    console.log("settings clicked");
}

function previewCamerasButtonCallback(){
    console.log("previewCameras clicked");
}