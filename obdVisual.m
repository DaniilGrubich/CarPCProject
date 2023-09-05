filename = 'obd2.txt';
delimiter = ',';
data1 = dlmread(filename, delimiter);

filename = 'obd2-2.txt';
delimiter = ',';
data2 = dlmread(filename, delimiter);

filename = 'obd2-3.txt';
delimiter = ',';
data3 = dlmread(filename, delimiter);

filename = 'obd2-4.txt';
delimiter = ',';
data4 = dlmread(filename, delimiter);

filename = 'obd2-5.txt';
delimiter = ',';
data5 = dlmread(filename, delimiter);

data = [data1; data2; data3; data4; data5];
plot(data(:, 1))