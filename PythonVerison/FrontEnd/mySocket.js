var socket = io('http://127.0.0.1:5000');

socket.on('connect', function() {
    console.log('Connected to server');
});

socket.on('image', function(msg) {
    console.log(msg[0]);
    document.getElementById('video').src = 'data:image/jpeg;base64,' + msg;
});

socket.on('setClock', function(msg){
    console.log('Time Recieved')
    document.getElementById('lblTime').innerHTML = msg;
});

socket.on('songData', function(msg){
    console.log('Song Data Recieved');
    data = msg.split('|');

    picLink = data[0];
    songName = data[1];
    artistName = data[2];
    progress = data[3];
    totalTime = data[4];
    newSongString = data[5];
    
    if(newSongString === "True"){
        document.getElementById('albumPic').src = picLink;
    }

    document.getElementById('songName').innerHTML = songName;
    document.getElementById('songArtist').innerHTML = artistName;
    document.getElementById('songProgress').style.width = progress/totalTime*100 + '%';



});

socket.on('carParameters', function(msg){
    // console.log(msg);
    let newStr = msg.slice(1, -1);
    let data = newStr.split(',');

    // console.log(data);
    // Assign array values to variables
    let [pid_engine_load, pid_coolant_temp, pid_short_term_fuel_trim_1, pid_long_term_fuel_trim_1, pid_intake_map, pid_engine_rpm, pid_vehicle_speed, pid_timing_advance, pid_intake_temp, pid_maf_flow, pid_throttle, pid_runtime, pid_commanded_evaporative_purge, pid_fuel_level, pid_evap_sys_vapor_pressure, pid_barometric, pid_catalyst_temp_b1s1, pid_control_module_voltage, pid_absolute_engine_load, pid_air_fuel_equiv_ratio, pid_relative_throttle_pos, pid_ambient_temp, pid_absolute_throttle_pos_b, pid_acc_pedal_pos_d, pid_commanded_throttle_actuator] = data.map(parseFloat);
    console.log(pid_engine_load, pid_coolant_temp, pid_short_term_fuel_trim_1, pid_long_term_fuel_trim_1, pid_intake_map, pid_engine_rpm, pid_vehicle_speed, pid_timing_advance, pid_intake_temp, pid_maf_flow, pid_throttle, pid_runtime, pid_commanded_evaporative_purge, pid_fuel_level, pid_evap_sys_vapor_pressure, pid_barometric, pid_catalyst_temp_b1s1, pid_control_module_voltage, pid_absolute_engine_load, pid_air_fuel_equiv_ratio, pid_relative_throttle_pos, pid_ambient_temp, pid_absolute_throttle_pos_b, pid_acc_pedal_pos_d, pid_commanded_throttle_actuator);

    // ambientTempGauge.set(pid_ambient_temp);

    loadGauge.set(pid_engine_load);
    shortTrimGauge.set(pid_short_term_fuel_trim_1);
    coolantGauge.set(pid_coolant_temp);
    throttleGauge.set(pid_throttle);
    //runtimeGauge.set();

    absoluteLoadGauge.set(pid_absolute_engine_load);
    longTrimGauge.set(pid_long_term_fuel_trim_1);
    IntakeTempGauge.set(pid_intake_temp);
    speedGauge.set(pid_vehicle_speed);
    voltageGauge.set(pid_control_module_voltage);

    RPMGauge.set(pid_engine_rpm);
    airFlowGauge.set(pid_maf_flow);
    fuelGauge.set(pid_fuel_level);
    //g14 = createGauge('gridCanvas14', 'gridLabel14', 0, 6000, 500, 750, 2500, '', .8);
    equiRatioGaugeGauge.set(pid_air_fuel_equiv_ratio);

    // // Splitting the received string into an array
    // var data = msg.split('|');

    // // Assigning each value to a variable (make sure to parse it to a float)
    // var rpm = parseFloat(data[0]);
    // var speed = parseFloat(data[1]);
    // var coolantTemp = parseFloat(data[2]);
    // var intakeTemp = parseFloat(data[3]);
    // var voltage = parseFloat(data[4]);
    // var fuelLevel = parseFloat(data[5]);
    // var avgMpg = parseFloat(data[6]);
    // var airFuelRatio = parseFloat(data[7]);
    // var intakeMap = parseFloat(data[8]);
    // var mafFlow = parseFloat(data[9]);

    // // Set the values to the gauges
    // rpmGauge.set(rpm);
    // speedGauge.set(speed);
    // coolantTempGauge.set(coolantTemp);
    // intakeTempGauge.set(intakeTemp);
    // voltageGauge.set(voltage);
    // fuelLevelGauge.set(fuelLevel);
    // avgMPGGauge.set(avgMpg);
    // airFuelRatioGauge.set(airFuelRatio);
    // intakeMapGauge.set(intakeMap);
    // mafFlowGauge.set(mafFlow);
    // myChart.data.datasets[0].data[0] = avgMpg;
    // myChart.update();

});

socket.on('newGPSPoint', function(msg){
    let data = msg.split('|');
    let lon = parseFloat(data[0]);
    let lat = parseFloat(data[1]);
    let speed = parseFloat(data[2]);
    // console.log(data);

    updateMarkerPosition(lat, lon, speed);
});
