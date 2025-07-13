# Turned_on used as a base class for the smart devices
class Base:
    def __init__(self):
        self.switched_on = False
    
    def toggle_switch(self):
        self.switched_on = not self.switched_on


# Smart plug class with consumption rate
class SmartPlug(Base):
    
    consumption_options = range(0, 151) #Valid consumption rate range
    def __init__(self, consumption_rate):
        super().__init__()
        if not self.switched_on: # if the device is off, the consumption rate is 0
            self._consumption_rate = 0
        else: # if the device is on, the consumption rate is the inputted consumption rate
            self._consumption_rate = consumption_rate

    @property # getter for consumption rate
    def consumption_rate(self):
        return self._consumption_rate
    
    @consumption_rate.setter # setter for consumption rate
    def consumption_rate(self, new_consumption_rate):
        if new_consumption_rate in self.consumption_options: #Checing weither the inputted consumption rate is valid
            self._consumption_rate = new_consumption_rate
        else:
            print("Invalid consumption rate")

        
    def __str__(self):
        status = "on" if self.switched_on else "off" #Checking the status of the device
        return f"SmartPlug is {status} with a consumption rate of {self.consumption_rate}"

def test_smart_plug(): #Testing the smart plug class
    sp1 = SmartPlug(120)
    print(sp1)
    sp1.toggle_switch()
    print(sp1)
    sp1.consumption_rate = 130
    print(sp1)
    sp1.consumption_rate = 160
    print(sp1)

# Smart oven class with temperature
class SmartOven(Base):
    temp_options = range(0,261) #Valid temperature range

    def __init__(self):
        super().__init__()
        if not self.switched_on: # if the device is off, the temperature is 0
            self._temperature = 0
        elif self.switched_on: # if the device is on, the temperature is the default temperature of 150
            self._temperature = 150

    @property
    def temperature(self): # getter for temperature
        return self._temperature

    @temperature.setter # setter for temperature
    def temperature(self, new_temp):
        if new_temp in self.temp_options: #Checking weither the inputted temperature is within the valid temp range
            self._temperature = new_temp
        else: 
            print("Invalid temperature")
    def __str__(self):
        if self.switched_on: #Checking the status of the device
            return f"SmartOven is on with a temperature of {self._temperature}"
        else:
            return f"SmartOven is off with a temperature of {self._temperature}"


class SmartWashingMachine(Base):
    wash_options = {
        'Daily Wash',
        'Quick Wash',
        'Eco',
        'None',
    } #Valid wash cycle options

    def __init__(self):
        super().__init__()
        if not self.switched_on: # if the device is off, the wash cycle is set to None
            self._wash_mode = 'None'
        else:
            self._wash_mode = 'Daily Wash'

    @property
    def wash_mode(self): # getter for wash cycle
        return self._wash_mode

    @wash_mode.setter # setter for wash cycle
    def wash_mode(self, new_wash_mode):
        if new_wash_mode in self.wash_options:
            self._wash_mode = new_wash_mode
        elif new_wash_mode == "None":
            print("Invalid wash cycle")
    def __str__(self):
        if self.switched_on: #Checking the status of the device
            return f"SmartWashingMachine is on with a cycle of {self._wash_mode}"
        else:
            return f"SmartWashingMachine is off with a cycle of {self._wash_mode}"
        
def test_custome_device(): #Testing the custom devices
    swm1 = SmartWashingMachine()
    so1 = SmartOven()
    print(swm1)
    print(so1)

    swm1.toggle_switch()
    so1.toggle_switch()
    print(swm1)
    print(so1)

    swm1.wash_mode = 'Quick Wash'
    so1.temperature = 200
    print(swm1)
    print(so1)

    so1.temperature = 300
    swm1.wash_mode = "Fast Wash"
    print(so1)
    print(swm1)


# smart home
class SmartHome(Base):   
    def __init__(self):
        super().__init__()
        self.devices = []
        self.max_devices = 5 #Max number of devices
        self.devices_switched_on = 0

    def add_devices(self,device):
        if len(self.devices) < self.max_devices: #Checking if the max number of devices
            self.devices.append(device)
        else:
            print('device rejected: Max devices reached')

    def remove_device(self,index):
        if index in range(len(self.devices)): #Checking if the index is within the range of the devices
            self.devices.pop(index)
        else:
            print("invalid selection")

    def get_device(self,index):
        return self.devices[index]

    def toggle_device(self,index):
        if self.devices[index].switched_on: #Checking the status of the device
            self.devices_switched_on -= 1
            if isinstance (self.devices[index], SmartWashingMachine): #Checking weither the device is a smartwashingmachine
                self.update_option(index, "None")
            if isinstance (self.devices[index], SmartOven) or isinstance (self.devices[index], SmartPlug): #Checking weither the device is a smartoven or smartplug
                self.update_option(index, 0)
        else:
            self.devices_switched_on += 1
            if isinstance (self.devices[index], SmartWashingMachine):
                self.update_option(index, "Daily Wash")
            elif isinstance (self.devices[index], SmartOven):
                self.update_option(index, 150)
            elif isinstance (self.devices[index], SmartPlug):
                self.update_option(index, 75)


        return self.devices[index].toggle_switch()

    def switch_all_on(self):
        for i in range(len(self.devices)): #Going through each of the devices 
            if not self.devices[i].switched_on: #Checking if the device is on
                self.toggle_device(i)
    
    def switch_all_off(self):
        for i in range(len(self.devices)): #Going through each of the devices
            if self.devices[i].switched_on: #Checking if the device is off
                self.toggle_device(i)

    def update_option(self, index, value):
            device = self.devices[index]
            if isinstance(device, SmartOven): #Checking weither the deive is a smartoven
                device.temperature = value
            elif isinstance(device, SmartWashingMachine): #checking weither the device is a smartwashingmachine
                device.wash_mode = value
            elif isinstance(device, SmartPlug): #checking weither the device is a smartplug
                device.consumption_rate = value

    def __str__(self):
        output = f'SmartHome with {len(self.devices)} device/s \n'
        for i in range(len(self.devices)):
            output += f'{i+1} - {self.devices[i]}\n'
        return  output
        


def test_smart_home(): #Testing the smart home class
    sp1 = SmartPlug(120)
    so1 = SmartOven()
    swm1 = SmartWashingMachine()
    sh1 = SmartHome()
    sh1.add_devices(sp1)
    sh1.add_devices(so1) 
    sh1.add_devices(swm1)
    print(sh1)

    print(sh1.get_device(0))
    print(sh1.get_device(1))
    print(sh1.get_device(2))

    sh1.toggle_device(0)
    sh1.toggle_device(1)
    sh1.toggle_device(2)
    print(sh1)

    sh1.toggle_device(0)
    sh1.toggle_device(1)
    sh1.toggle_device(2)
    print(sh1)

    sh1.switch_all_on()
    print(sh1)

    sh1.switch_all_off()
    print(sh1)

    sp2 = SmartPlug(110)
    so2 = SmartOven()
    swm2 = SmartWashingMachine()
    sh1.add_devices(sp2)
    sh1.add_devices(so2)
    sh1.add_devices(swm2)
    print(sh1)

    sh1.update_option(0,130)
    sh1.update_option(1, 230)
    sh1.update_option(2, "Quick Wash")
    print(sh1)

    sh1.update_option(0,190)
    sh1.update_option(1, 300)
    sh1.update_option(2, "Fast Wash")
    print(sh1)

    sh1.remove_device(4)
    print(sh1)
