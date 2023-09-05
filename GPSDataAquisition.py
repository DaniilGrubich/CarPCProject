import threading
import time
from pySerialTransfer import pySerialTransfer as txfer
import serial
import time
import pynmea2


# PID 	PID Name	                    Short Name	Explanation
# 0x04	PID_ENGINE_LOAD	                A	        Represents the current computed relative load value of the engine.
# 0x05	PID_COOLANT_TEMP	            B	        Denotes the temperature of the coolant in the engine.
# 0x06	PID_SHORT_TERM_FUEL_TRIM_1	    C	        Short term modifications to the fuel system to maintain an optimal air/fuel ratio.
# 0x07	PID_LONG_TERM_FUEL_TRIM_1	    D	        Long term modifications to the fuel system to maintain an optimal air/fuel ratio.
# 0x0B	PID_INTAKE_MAP	                E	        Represents the manifold absolute pressure, which provides information about the vacuum in the intake manifold.
# 0x0C	PID_ENGINE_RPM	                F	        Measures the speed at which the engine's crankshaft is spinning.
# 0x0D	PID_VEHICLE_SPEED	            G	        Measures the current speed of the vehicle.
# 0x0E	PID_TIMING_ADVANCE	            H	        Indicates the ignition timing advance for #1 cylinder (not including mechanical advance).
# 0x0F	PID_INTAKE_TEMP	                I	        Indicates the temperature of the air entering the intake manifold.
# 0x10	PID_MAF_FLOW	                J	        Mass Air Flow sensor reports the amount of air entering the engine.
# 0x11	PID_THROTTLE	                K	        Measures the position of the throttle valve.
# 0x1F	PID_RUNTIME	                    L	        Engine run time since start.
# 0x2E	PID_COMMANDED_EVAPORATIVE_PURGE	M	        The commanded evaporative purge controls the purge control solenoid valve to manage the amount of fuel vapor that is purged from the charcoal canister.
# 0x2F	PID_FUEL_LEVEL	                N	        Measures the current level of fuel in the tank.
# 0x32	PID_EVAP_SYS_VAPOR_PRESSURE	    O	        Pressure of the fuel vapor in the Evaporative Emission Control System.
# 0x33	PID_BAROMETRIC	                P	        Atmospheric pressure at current location and altitude.
# 0x3C	PID_CATALYST_TEMP_B1S1	        Q	        Measures the temperature of the catalyst to ensure optimal catalytic converter efficiency.
# 0x42	PID_CONTROL_MODULE_VOLTAGE	    R	        Voltage supplied to the Engine Control Module.
# 0x43	PID_ABSOLUTE_ENGINE_LOAD	    S	        The absolute load value represents an approximation of the current absolute load value of the engine.
# 0x44	PID_AIR_FUEL_EQUIV_RATIO	    T	        Represents the current air-fuel equivalence ratio.
# 0x45	PID_RELATIVE_THROTTLE_POS	    U	        Position of the throttle valve in relation to its maximum range.
# 0x46	PID_AMBIENT_TEMP	            V	        Outside/ambient temperature as detected by the vehicle.
# 0x47	PID_ABSOLUTE_THROTTLE_POS_B	    W	        Absolute position of the throttle valve B.
# 0x4A	PID_ACC_PEDAL_POS_D	            X	        Position D of the accelerator pedal.
# 0x4B	PID_ACC_PEDAL_POS_E	            Y	        Position E of the accelerator pedal.
# 0x4C	PID_COMMANDED_THROTTLE_ACTUATOR	Z	        Commanded position of the throttle actuator control.

codes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Z']
codeCoutner = 0
priorityCodes = ['G', 'J', 'F']
parameterLatters = ''


carParameters = [0]*len(codes)  


    
       

with open('obd2-5.txt', 'w') as f:
    while True:
        try:
            link = txfer.SerialTransfer('COM9')
            
            link.open()
            time.sleep(2 ) 

            while True:
                try:
                    # Convert list to string
                    priorityCodes_str = ''.join(priorityCodes)
                    interatingCode = codes[codeCoutner%len(codes)]
                    codeCoutner=codeCoutner+1
                    while(priorityCodes.__contains__(interatingCode)):
                        interatingCode = codes[codeCoutner%len(codes)]
                        codeCoutner=codeCoutner+1
                    # Combine strings and convert to bytes
                    command = (priorityCodes_str + interatingCode)
                    parameterLatters = priorityCodes_str + interatingCode

                    str_ = command
                    str_size = link.tx_obj(str_, 0)
                    print(str_)
                    link.send(str_size)
                    
                    ###################################################################
                    # Wait for a response and report any errors while receiving packets
                    ###################################################################
                    while not link.available():
                        if link.status < 0:
                            if link.status == txfer.CRC_ERROR:
                                print('ERROR: CRC_ERROR')
                            elif link.status == txfer.PAYLOAD_ERROR:
                                print('ERROR: PAYLOAD_ERROR')
                            elif link.status == txfer.STOP_BYTE_ERROR:
                                print('ERROR: STOP_BYTE_ERROR')
                            else:
                                print('ERROR: {}'.format(link.status))
                    
                    
                    # ###################################################################
                    # # Parse response string
                    # ###################################################################
                    rec_str_   = link.rx_obj(obj_type=type(str_),
                                            obj_byte_size=27,
                                            start_pos=0)
                    
                    
                    split_content = rec_str_.split(',')
                    print(rec_str_)
                    # Split the string into parts by comma
                    parts = rec_str_.split(",")

                    # The first 5 parts should be the float numbers, so we convert them
                    float_content = [float(part) for part in parts[:-2]]  # We exclude the last part 'XXXXX'
                    
                    valCounter = 0
                    
                    for i in parameterLatters:
                        try:
                            carParameters[codes.index(i)] = float_content[valCounter]
                            valCounter = valCounter+1
                        except:
                            break

                    f.write(str(carParameters))
                    f.write('\n')
                    f.flush()  # Force write to file
                    time.sleep(1/24)


                    # ###################################################################
                    # # Display the received data
                    # ###################################################################
                    # print('SENT: {} '.format( str_))
                    # print('RCVD: {} '.format(rec_str_))
                    # print(' ')
                except:
                    break
                    
                
        except:
            continue








# # Replace with your serial port
# ser = serial.Serial('COM14', 9600, timeout=1)

# try:
#     with open('gps_data.txt', 'w') as f:
#         while True:
#             try:
#                 line = ser.readline().decode('utf-8').rstrip()

#                 if line:
#                     # Parse NMEA sentence
#                     msg = pynmea2.parse(line)

#                     # Process GGA and RMC sentences
#                     if msg.sentence_type == 'GGA':
#                         data = [msg.timestamp, msg.lat, msg.lon]
#                         print(' '.join(map(str, data)))
#                         f.write(' '.join(map(str, data)))
#                         f.write('\n')
#                         f.flush()  # Force write to file

#                     elif msg.sentence_type == 'RMC':
#                         data = [msg.timestamp, msg.lat, msg.lon, msg.spd_over_grnd]
#                         print(' '.join(map(str, data)))
#                         f.write(' '.join(map(str, data)))
#                         f.write('\n')
#                         f.flush()  # Force write to file

#                 # Adjust this to control how often you want to write to the file
#                 time.sleep(0.1)

#             except KeyboardInterrupt:
#                 print("Stopped")
#                 break

#             except pynmea2.ParseError as e:
#                 print(f"Parse error: {e}")
#                 continue

# finally:
#     ser.close()
