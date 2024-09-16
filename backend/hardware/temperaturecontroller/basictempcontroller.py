from hardware.temperaturecontroller.base import TempController
import logging


RELAY_ON = 1
RELAY_OFF = 0


class BasicTempController(TempController):
    def __init__(self, temp_controller_config: dict, devices: dict):
        """
        Constructor. Initializes the stirrer.
        :param temp_controller_config:
          dict
            heaterPin
              Which gpio pin to control the heating element
            heaterPumpPin
              Which gpio pin to control the heater pump
            coolerPin
              Which gpio pin to control the cooler pump
            gpioID
              The ID of the GPIO device used to control heating and cooling
            maxTemp
              Maximum temperature the hardware will support
            minTemp
              Minimum temperature the hardware will support
        """
        super().__init__(temp_controller_config, devices)
        self.gpio = devices[temp_controller_config["gpioID"]]
        self.heaterPin = temp_controller_config["heaterPin"]
        self.heaterPumpPin = temp_controller_config["heaterPumpPin"]
        self.coolerPin = temp_controller_config["coolerPin"]
        self.maxTemp = temp_controller_config["maxTemp"]
        self.minTemp = temp_controller_config["minTemp"]

        self.gpio.setup(self.heaterPin)
        self.gpio.setup(self.heaterPumpPin)
        self.gpio.setup(self.coolerPin)

        self.gpio.output(self.heaterPin, RELAY_OFF)
        self.gpio.output(self.heaterPumpPin, RELAY_OFF)
        self.gpio.output(self.coolerPin, RELAY_OFF)

        self.thermometer = devices[temp_controller_config["thermometerID"]]

    def turnHeaterOn(self):
        """
        Turns heater on.

        :return:
        None
        """
        logging.debug("heater turned on")
        self.gpio.output(self.heaterPin, RELAY_ON)

    def turnHeaterOff(self):
        """
        Turns heater off.

        :return:
        None
        """
        logging.debug("heater turned off")
        self.gpio.output(self.heaterPin, RELAY_OFF)

    def turnHeaterPumpOn(self):
        logging.debug("heater pump turned on")
        self.gpio.output(self.heaterPumpPin, RELAY_ON)

    def turnHeaterPumpOff(self):
        logging.debug("heater pump turned off")
        self.gpio.output(self.heaterPumpPin, RELAY_OFF)

    def turnCoolerOn(self):
        """
        Turn cooler on.

        :return:
        None
        """
        logging.debug("cooler turned on")
        self.gpio.output(self.coolerPin, RELAY_ON)

    def turnCoolerOff(self):
        """
        Turn cooler off.

        :return:
        None
        """
        logging.debug("cooler turned off")
        self.gpio.output(self.coolerPin, RELAY_OFF)

    def getTemp(self):
        """
        Read the temperature from the temperature sensor.
        :return:
        The temperature of the temperature sensor.
        """
        return self.thermometer.getTemp()

    def getMaxTemperature(self):
        return self.maxTemp

    def getMinTemperature(self):
        return self.minTemp

    def getPIDConfig(self):
        return self.pidConfig
