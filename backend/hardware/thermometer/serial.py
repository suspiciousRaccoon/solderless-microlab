from hardware.thermometer.base import TempSensor
from w1thermsensor import W1ThermSensor, Sensor
import serial
import re

class SerialTempSensor(TempSensor):
    tempSer = None
    def __init__(self, args):
        """
        Constructor. Initializes the sensor.
        :param args:
          dict
            serialDevice
              A string with the device read from
        """
        self.tempSer = serial.Serial(args["serialDevice"], timeout=0.5)

    def getTemp(self):
        """
        Get the temperature of the sensor in celsius.
        :return:
            Temperature in Celsius
        """
        line = "12345678901"
        lastLine = ""
        while (len(line) > 10 or len(line) < 2):
            lastLine = line
            try:
                line = self.tempSer.readline()
            except Exception as e:
                print('Error reading from thermometer')
                print(e)
                continue
            finally:
                print('ser read ' + str(len(line)) + ' ' + str(line) )

        lastLine = str(line)
   
        start = lastLine.find('t1=')    # Look for 't1=' in the input line
        if start == -1:                 # Unclear why sometimes the thermometer returns 't1=' and other times just 't='
            start = lastLine.find('t=') + len('t=')
        else:                           # This should be the default case
            start = lastLine.find('t1=') + len('t1=')

        end = lastLine.find('\\',start)
        if end == -1:   # Different thermometers may parse differently. These conditionals may need to expand.
            end = lastLine.find(' ',start)
            
        print('found ' + str(start) + ' ' + str(end) + ' ' + lastLine + ' ' + lastLine[start:end])
        if(start > -1 and end > -1):
            temperature = float(lastLine[start:end])
        else:
            temperature = "Error"
        print('Read temperature ' + str(temperature)) # + ' ' + str(lastLine))

        return temperature
