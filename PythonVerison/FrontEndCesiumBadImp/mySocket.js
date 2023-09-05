var socket = io('http://127.0.0.1:5000');

socket.on('connect', function() {
    console.log('Connected to server');
});

// socket.on('image', function(msg) {
//     document.getElementById('video').src = 'data:image/jpeg;base64,' + msg;
// });

socket.on('setClock', function(msg){
    console.log('Time Recieved')
    document.getElementById('lblTime').innerHTML = msg;
});

socket.on('songData', function(msg){
    console.log('Song Data Recieved');
    data = msg.split('|');
    console.log(data);

    picLink = data[0];
    songName = data[1];
    artistName = data[2];
    progress = data[3];
    totalTime = data[4];

    document.getElementById('songName').innerHTML = songName;
    document.getElementById('songArtist').innerHTML = artistName;
    document.getElementById('albumPic').src = picLink;




});

socket.on('newGPSPoint', function(msg){
    let data = msg.split('|');
    let longitude = parseFloat(data[0]);
    let latitude = parseFloat(data[1]);
    let speed = parseFloat(data[2]);
    let timeDiff = parseFloat(data[3]); // Make sure your server emits this value

    prevPosition = nextPosition;
    nextPosition = Cesium.Cartesian3.fromDegrees(longitude, latitude, 1);
    dt = timeDiff;
    t = 0;
});
