# The Main file that controls and calling of other functions. This imports all other files. 
import CRC_Calculation #  File names
import Device_Number
import Open_Port
#import Device_Status
#import Signal_Strength
import Sensor_Information
import Http_Server
import time
import http.server

# CREATE A CONDITION WHEN NOTHING IS BEING SEND

file = open("Sensor Data.txt","w") # Creating the file
file.write('Device Number\tDevice Type\tTime of Request\tTemperature\tDevice Alert\tDevice Status\tDevice Path\tRoute Signal Strength\n')
#received_data=Open_Port.sendReceiver([0x43,0x01],7)  # Calling the 'sendReceiver' funtion from file with argument as the request code and device number      

Http_Server.Handler.ParseData()
payload_data=[]
deviceNumber_data=[]

#a = http.server.HTTPServer( ('', 80), Http_Server.Handler )
##print("Hello world!")
#print(Http_Server.Handler.do_POST())
#a.serve_forever()

#for i in range(6):# Received data is of 7 bytes and the 1st byte is always the CRC of 'C/F/'
#    payload_data.append(int(received_data[i],16))
#    if(i>0 and i<5):# Store the bytes from 1-4 as they contain the useful data
#        deviceNumber_data.append(received_data[i])
#
#print("\nWaiting....\n")
#time.sleep(2)
#
#CRC_Output=CRC_Calculation.CalcRC8(payload_data,len(payload_data)) # Calling CRC to calculate 
#CRC_Calculation.CompareCRC(CRC_Output,received_data[6])     # and match the CRC code
#
#
#device_number=Device_Number.CalcDeviceNum(deviceNumber_data,len(deviceNumber_data),24)# Calculates the Device that underwent change, using the argument of data which was calculated earlier
#print("\nWaiting....\n")
#time.sleep(2)
#print("The device that underwent changes are as follows")
#print(device_number)
#
#serial_number=[]
#
#Sensor_Information.SensorInformation(device_number)# Calculates the staus, temperature and other information regarding every sensor and stores in file















#if len(device_number)!=0:
#    for i in range(len(device_number)):
#        CRC=(CRC_Calculation.CalcRC8([0x49,device_number[i]],2))
#        request_code.append([0x49,device_number[i],int(CRC,16)])
#        #print(request_code)
#    
#    print('\nWaiting')
#    time.sleep(2)
#    
#    for i in range(len(device_number)):
#        data_sensor=Open_Port.sendReceiver(request_code[i],27)
#        temp_time=time.localtime()
#        device_alert=data_sensor[15]
#        device_status=data_sensor[14]
#        device_path=[int(data_sensor[8],16),int(data_sensor[9],16)]
#        #print(device_status,'\t',i)
#        temperature_sensor=int(data_sensor[16],16)
#        serial_number=Device_Number.HexCombine([data_sensor[2],data_sensor[3],data_sensor[4]],3,16)
#        #print("Serial Number is",hex(serial_number))
#        if(int(device_alert,16)==0x01):
#            print("\nDevice ", device_number[i], " is ACTIVATED!!")
#            status_sensor='ACTIVATED'
#        else:
#            print("\nDevice ", device_number[i], " is DEACTIVED")
#            status_sensor='DEACTIVATED'
#            
#        status=Device_Status.DeviceStatus(device_status)
#        
#        print("Temperature of Device ",device_number[i], " is ",temperature_sensor,' degrees\n')
#        print("Current Time:",temp_time[3],':',temp_time[4])
#    
#        print('Device Status: ',status)
#        print('Device Path: ',device_number[i],'-',int(data_sensor[8],16),'-',int(data_sensor[9],16),'\n')
#        device_signal=Signal_Strength.SignalStrength([data_sensor[10],data_sensor[11],data_sensor[12]])
#        print("Device Signal: ",device_signal)
#        if(serial_number==0x210f56):
#            print("Device Type: Contact Sensor")
#            device_type='Contact Sensor'
#        elif(serial_number==0x140f72 or serial_number==0x1110ab or serial_number==0x161011):
#            print("Device Type: PIR Sensor")
#            device_type='PIR Sensor'#WHY WOULD YOU NEED TO LOG TIME? HOW IN REAL LIFE USEFUL
#        file.write(str(device_number[i])+'\t\t'+device_type+'\t\t'+str(temp_time[3])+':'+str(temp_time[4])+'\t\t'+str(temperature_sensor)+'\t'+status_sensor+'\t'+str(status)+'\t'+str(device_number[i])+'-'+str(int(data_sensor[8],16))+'-'+str(int(data_sensor[9],16))+'\t\t'+str(device_signal[0])+'/'+str(device_signal[1])+'/'+str(device_signal[2])+'\n')
#else:
#    print("No Device is activated yet")
#
#file.close()


#LINE 8-35
# What if the length of the string is not 7 more than  7 bytes. Should I cancel the pooling or
# shoudl I send yo
#for i in range(1):
#    port = "COM4"
#    baud = 19200
#    
#    ser = serial.Serial(port, baud, timeout=1)
#    if ser.isOpen():
#        print(ser.name + ' is open...')
#    received_data=[]
#    cmd = input("Enter command or 'exit':")
#    bitmap=[0x43,0x01]
#    bits=bytearray(bitmap)
#    ser.write(bits)
#
#    count=0
#    for i in range(7): # Should I make it len. What if not 7 then wrong anyways?
#        for line in ser.read(): 
#              time.sleep(1)
#             # print "line(" + str(count) + ")=" + line
#              received_data.append(line)
#              count=count+1
#              #print(received_data[i] + "  and the "+hex(ord(received_data[i])))
#              received_data[i]=hex((received_data[i]))
#              #print(received_data[i] + "  and the "+bin(ord(received_data[i])))
#              print(received_data)          
     
#Stores data from the received information