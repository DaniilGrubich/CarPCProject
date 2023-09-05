% Open file
fid = fopen('gps_data3.txt', 'r');

% Initialize arrays
latitude_raw = [];
longitude_raw = [];
speed = [];

% Read each line
while ~feof(fid)
    line = fgetl(fid);
    parts = strsplit(line, ' ');

    % Parse latitude and longitude
    latitude_raw = [latitude_raw; str2double(parts{2})];
    longitude_raw = [longitude_raw; str2double(parts{3})];
    
    % Parse speed if it exists
    if numel(parts) > 3
        speed = [speed; str2double(parts{4})];
    else
        speed = [speed; NaN]; % Fill with NaN for lines without speed
    end
end

% Close file
fclose(fid);

% Convert latitude and longitude from DDMM.MMMM to decimal degrees
latitude_deg = fix(latitude_raw / 100);
latitude_min = mod(latitude_raw, 100);
latitude = latitude_deg + latitude_min / 60;

longitude_deg = fix(longitude_raw / 100);
longitude_min = mod(longitude_raw, 100);
longitude = -1 * (longitude_deg + longitude_min / 60); % Apply correction for western hemisphere

% Convert speed from knots to m/s
speed_mps = speed * 0.514444;

% Create a geographic bubble chart
gb = geobubble(latitude, longitude, speed_mps, 'Basemap', 'satellite');

% Customize chart
title(gb.Parent.Parent, 'GPS Data'); % Set title on parent axes
