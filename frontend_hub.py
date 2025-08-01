from tkinter import Tk, Frame, Label, Entry, Button, StringVar, Toplevel
from backend_hub import SmartHome, SmartOven, SmartWashingMachine, SmartPlug

class SmartHomeApp():

    def __init__(self, smarthome, create_smarthomes):
        self.smarthome = smarthome #Assigning a smarthome object to the class
        self.create_smarthomes = create_smarthomes #Assigning a function from smarthomes app to the class
        

        self.win = Toplevel()
        self.win.title("Smart Home App")


        self.win_frame = Frame(self.win)
        self.win_frame.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
        )

        
        self.smart_home_widgets = [] #List for the widgets in the smarthome
        self.max_devices = 5 #assigning the max value of devices that can be in the smarthome


    def create_buttons(self):
        #Creating the Turn all on and turn all off that will be permenant
        turn_all_on = Button(
            self.win_frame,
            text="Turn all on",
            command=lambda: self.switch_all_on()
        )
        turn_all_on.grid(
            sticky="w",
            row=0,
            column=0,
            padx=10,
        )
        turn_all_off = Button(
            self.win_frame,
            text="Turn all off",
            command=lambda: self.switch_all_off()
        )
        turn_all_off.grid(
            row=0,
            column=0,
            padx=85,
        )
        max_devices = Label(
            self.win_frame,
            text= f"Maximum Devices: {self.max_devices}"
        )
        max_devices.grid(
            row=0,
            column= 1,
            padx= 0,
        )
        
    def create_devices(self):
        self.delete_all_devices() #resetting the devices/ smarthome page
        if len(self.smarthome.devices) < self.max_devices: #Checking if the number of devices is less than the max devices
            add_button = Button(
                self.win_frame,
                text="Add",
                command=lambda: self.add_device()
            )
            add_button.grid(
                sticky="w",
                row=len(self.smarthome.devices) + 1,
                column=0,
                padx=10,
            )
            self.smart_home_widgets.append(add_button)

        for i in range(len(self.smarthome.devices)): #Going through each of the devices
            if self.smarthome.devices[i].switched_on == True: 
                status = "On" #Assigning the value of 'On' to status if the device is on
            else:
                status = "Off" #Assigning the value of 'Off' to status if the device is off

            if isinstance(self.smarthome.devices[i], SmartPlug): #Checking weither the device is a smartplug
                device = f"Plug: {status}, " + f" Consumption Rate: {self.smarthome.devices[i].consumption_rate}" #Creating a string value for the smartplug
            elif isinstance(self.smarthome.devices[i], SmartOven): #Checking weither the device is a smartoven
                device = f"Oven: {status}, " + f" Temperature: {self.smarthome.devices[i].temperature}" #Creating a string value for the smartoven
            elif isinstance(self.smarthome.devices[i], SmartWashingMachine): #Checking weither the device is a smartwashingmachine
                device = f"Washing Machine: {status}, " + f" Wash Mode: {self.smarthome.devices[i].wash_mode}" #Creating a string value for the smartwashingmachine

            device_label= Label(
                self.win_frame,
                text=device #Assigning the string value of the device that is corresponding to the label
                
            )
            device_label.grid(
                sticky= "w",
                row=i+1,
                column=0,
            )
            self.smart_home_widgets.append(device_label) #Adding the device label to the list of widgets
        
            toggle_switch = Button(
                self.win_frame,
                text="Toggle",
                command=lambda i=i: self.toggle_device(i)
            )
            toggle_switch.grid(
                row=i+1,
                column=1,
                padx=5,
                pady=5,
            )
            if self.smarthome.devices[i].switched_on == True: #Checking if the device is on to determine weither the device can be edited
                edit_device = Button(
                    self.win_frame,
                    text="Edit",
                    command=lambda i=i: self.edit_device(i) #Assigning the edit device function to the button
                )
                edit_device.grid(
                    row=i+1,
                    column=2,
                    padx=5,
                    pady=5,
                )
                self.smart_home_widgets.append(edit_device) #Adding the edit device button to the list of Widgets
            remove_device = Button(
                self.win_frame,
                text="Remove",
                command=lambda i=i: self.remove_device(i)
            ) 
            remove_device.grid(
                row=i+1,
                column=4,
                padx=5,
                pady=5,
            ) 
            self.smart_home_widgets.append(remove_device) #Adding the remove device button to the list of Widgets
            self.smart_home_widgets.append(toggle_switch) #Adding the toggle switch button to the list of Widgets   




    def toggle_device(self,index):
       
        self.smarthome.toggle_device(index) #Toggling the device of device in the index
        self.create_devices() #Refreshing the devices page
        self.create_smarthomes() #Refreshing the smarthomes page


    def switch_all_on(self):

        self.smarthome.switch_all_on() #Switching all devices on
        self.create_devices() #Refreshing the devices page
        self.create_smarthomes() #Refreshing the smarthomes page
    
    def switch_all_off(self):

        self.smarthome.switch_all_off() #Switching all devices off
        self.create_devices() #Refreshing the devices page
        self.create_smarthomes() #Refreshing the smarthomes page

    def edit_device(self,index):
        edit_window = Toplevel() #Creating a new window for the edit device as a TopLevel window (Window above all previous windows)
        edit_window.title("Edit Device")

        edit_frame = Frame(edit_window)

        edit_frame.grid(
        row=0,
        column=0,
        padx=10,
        pady=10,
        )


        device_setting = StringVar() #Creating a string variable for the device setting

        edit_entry = Entry(
                edit_frame,
                textvariable = device_setting
            )
        edit_entry.grid(
            row=1,
            column=2,
            padx=5,
            pady=5,
        ) 

        if isinstance(self.smarthome.get_device(index), SmartPlug): #Checking if the device is a smartplug
            edit_button = Button(
                edit_frame,
                text="New Consumption Rate",
                command=lambda: self.update_option(index, device_setting.get(), edit_window, edit_entry) #Assigning the update option function to the button
            )
            edit_entry.insert(0, "0-150") #Inserting the value of 0-150 to the entry box, to give the user the range of values that can be entered

        elif isinstance(self.smarthome.devices[index], SmartOven): #Checking if the device is a smartoven
            edit_button = Button(
                edit_frame,
                text="New Temperature:",
                command= lambda: self.update_option(index, device_setting.get(), edit_window, edit_entry) #Assigning the update option function to the button
            )
            edit_entry.insert(0, "0-260") #Inserting the value of 0-260 to the entry box, to give the user the range of values that can be entered

        elif isinstance(self.smarthome.devices[index], SmartWashingMachine): #Checking if the device is a smartwashingmachine
            edit_button = Button(
                edit_frame,
                text="New Wash Cycle:",
                command= lambda: self.update_option(index, str(device_setting.get()), edit_window, edit_entry)
            )
            edit_entry.insert(0, "Daily Wash, Quick Wash, Eco") #Inserting the value of Daily Wash, Quick Wash, Eco to the entry box, to give the user the range of values that can be entered

        edit_button.grid(
                row=1,
                column=1,
                padx=5,
                pady=5,
            )
        
    def update_option(self, index, value, edit_window, edit_entry):

        device = self.smarthome.get_device(index)

        if isinstance(device, SmartWashingMachine): #Checking weither the device is a smartwashingmachine
            if value in ["Daily Wash", "Quick Wash", "Eco"]: #Checking if the value is in the list of wash cycles
                self.smarthome.update_option(index, value)
                edit_window.destroy()
                self.create_devices()
            else:
                edit_entry.delete(0,"end") #Deleting the entry box
                edit_entry.insert(0,"Daily Wash, Quick Wash, Eco") #Inserting the default value to the entry box
                invalid_label = Label(
                    edit_window,
                    text=self.smarthome.update_option(index, value)
                )
                invalid_label.grid(
                    row=1,
                    column=0,
                    padx=5,
                    pady=5,
                )

        elif isinstance(device, SmartOven): #Checking weither the device is a smartoven
            value = int(value)
            if value >= 0 and value <= 260: #Checking if the value is between 0 and 260
                self.smarthome.update_option(index, value)
                edit_window.destroy() #Destroying the edit window
                self.create_devices()
            else:
                edit_entry.delete(0,"end") #Deleting the entry box
                edit_entry.insert(0,"0-260") #Inserting the default values to the entry box
                invalid_label = Label(
                    edit_window,
                    text=self.smarthome.update_option(index, value)
                )
                invalid_label.grid(
                    row=1,
                    column=0,
                    padx=5,
                    pady=5,
                )

        elif isinstance(device, SmartPlug): #Checking weither the device is a smartplug
            value = int(value)
            if value >= 0 and value <= 150: #Checking if the value is between 0 and 150
                self.smarthome.update_option(index, value)
                edit_window.destroy()
                self.create_devices()
            else:
                edit_entry.delete(0,"end") #Deleting the entry box
                edit_entry.insert(0,"0-150") #Inserting the default value to the entry box
                invalid_label = Label(
                    edit_window,
                    text=self.smarthome.update_option(index, value)
                )
                invalid_label.grid(
                    row=1,
                    column=0,
                    padx=5,
                    pady=5,
                )

    def remove_device(self,index):
        self.smarthome.remove_device(index)
        self.create_devices()
        self.create_smarthomes()

    def delete_all_devices(self):
        for i in self.smart_home_widgets:
            i.destroy() #Destroying the widgets in the list of smart home devices
        self.smart_home_devices = [] #Resetting the list of smart home devices
    
    def add_device(self):
        add_window = Toplevel() #Creating a new window for the add device as a TopLevel window 
        add_window.title("Add Device")

        add_frame = Frame(add_window)
        add_frame.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
        )

        add_smartplug = Button(
            add_frame,
            text="SmartPlug",
            command=lambda: self.add_smartplug(add_window) #Assigning the add smartplug function to the button
        )
        add_smartplug.grid(
            row=2,
            column=1,
            padx=5,
            pady=5,
        )

        add_smartoven = Button(
            add_frame,
            text="SmartOven",
            command=lambda: self.add_smartoven(add_window)#Assigning the add smartoven function to the button
        ) 

        add_smartoven.grid(
            row=2,
            column=2,
            padx=5,
            pady=5
        )

        add_smartwashingmachine = Button(
            add_frame,
            text="SmartWashingMachine",
            command=lambda: self.add_smartwashingmachine(add_window) #Assigning the add smartwashingmachine function to the button
        )

        add_smartwashingmachine.grid(
            row=2,
            column=3,
            padx=5,
            pady=5,
        )

    
    
    def add_smartplug(self, add_window):   
        device_name = SmartPlug(45) #Creating a smartplug object with a consumption rate of 45 
        self.smarthome.add_devices(device_name) #Adding the smartplug object to the smarthome
        add_window.destroy()
        self.create_devices()
        self.create_smarthomes()

    def add_smartoven(self,add_window):
        device_name = SmartOven() #Creating a smartoven object
        self.smarthome.add_devices(device_name) #Adding the smartoven object to the smarthome
        add_window.destroy()
        self.create_devices()
        self.create_smarthomes()

    def add_smartwashingmachine(self,add_window):
        device_name = SmartWashingMachine() #Creating a smartwashingmachine object  
        self.smarthome.add_devices(device_name) #Adding the smartwashingmachine object to the smarthome
        add_window.destroy()
        self.create_devices()
        self.create_smarthomes()

    def devices_switched_on(self):
        count = 0
        for i in range(len(self.smarthome.devices)): #Going through each of the devices and seeing which ones are on, adding to the count if trues
            if self.smarthome.devices[i].switched_on == True:
                count += 1
        return count
        
    def run(self):
        self.create_buttons()
        self.create_devices()
        self.win.mainloop()
            

def test_smart_home_app():

    sh1 = SmartHome()
    so1 = SmartOven()
    swm1 = SmartWashingMachine()
    sp1 = SmartPlug(120)
    sh1.add_devices(so1)
    sh1.add_devices(swm1)
    sh1.add_devices(sp1)
    print(sh1.get_device(0))
    sh1.toggle_device(0)
    print(sh1.get_device(0))
    app = SmartHomeApp(sh1)
    app.run()



class SmartHomesApp():
    def __init__(self):
        self.smart_homes = []
        self.win = Tk()
        self.win.title("Smart Homes App")

        self.win_frame = Frame(self.win)
        self.win_frame.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
        )
        self.smart_homes_widgets = [] #List for the widgets in the smarthomes
        self.max_smarthomes = 3 #Assigning the max value of smarthomes

    def create_smart_homes(self):
        self.delete_all_smart_homes() #resetting the smarthomes page
        max_smarthomes_label = Label(
            self.win_frame,
            text= f"Maximum SmartHomes: {self.max_smarthomes}"
        )
        max_smarthomes_label.grid(
            row=0,
            column=1
        )
        if len(self.smart_homes) < self.max_smarthomes:
            add_button = Button(
                self.win_frame,
                text="Add Smart Home",
                command=lambda: self.add_smart_home()
            )
            add_button.grid(
                row=0,
                column=0,
                padx=10,
            )
            self.smart_homes_widgets.append(add_button) #Adding the add button to the list of widgets

        for i in range(len(self.smart_homes)):
            smart_home_label = Label(
                self.win_frame,
                text=f"Smart Home {i+1}"
            )
            smart_home_label.grid(
                row=i+1,
                column=0,
                padx=10,
            )
            self.smart_homes_widgets.append(smart_home_label) #Adding the smart home label to the list of widgets

            smart_home_open_button = Button(
                self.win_frame,
                text="Open",
                command=lambda i=i: self.open_smart_home(i)
            )
            smart_home_open_button.grid(
                row=i+1,
                column=3,
                padx=10,
            )
            smart_home_remove_button = Button(
                self.win_frame,
                text="Remove",
                command=lambda i=i: self.remove_smarthome(i)
            )
            smart_home_remove_button.grid(
                row=i+1,
                column=4,
                padx=10,
            )
            self.smart_homes_widgets.append(smart_home_open_button) #Adding the open button to the list of widgets
            self.smart_homes_widgets.append(smart_home_remove_button) #Adding the remove button to the list of widgets

            devices_label = Label(
                self.win_frame,
                text=f"Devices: {len(self.smart_homes[i].devices)}"
            )
            devices_label.grid(
                row=i+1,
                column=1,
                padx=10,
            )
            switched_on_label = Label(
                self.win_frame,
                text=f"Switched on: {self.smart_homes[i].devices_switched_on}"
            )
            switched_on_label.grid(
                row=i+1,
                column=2,
                padx=10,
            )
            
            self.smart_homes_widgets.append(devices_label) #Adding the devices label to the list of widgets
            self.smart_homes_widgets.append(switched_on_label) #Adding the switched on label to the list of widgets

    def open_smart_home(self, index):
        app = SmartHomeApp(self.smart_homes[index], self.create_smart_homes) #Assigning a smart home app object to the class
        self.create_smart_homes()
        app.run()

    def add_smart_home(self):
        self.smartplug= SmartPlug(45) #adding the three devices to the smarthome as a starting point
        self.smartoven = SmartOven()
        self.smartwashingmachine = SmartWashingMachine()
        smart_home = SmartHome()
        smart_home.add_devices(self.smartplug)
        smart_home.add_devices(self.smartoven)
        smart_home.add_devices(self.smartwashingmachine)
        self.smart_homes.append(smart_home)
        self.create_smart_homes()

    def remove_smarthome(self,index):
        self.smart_homes.pop(index) #Removing the smarthome from the list of smarthomes
        self.create_smart_homes()

    def delete_all_smart_homes(self):
        for i in self.smart_homes_widgets:
            i.destroy()
        self.smart_homes_widgets = []

    def run(self):
        self.create_smart_homes()
        self.win.mainloop() #Running the mainloop

def test_smart_homes_app(): #Testing the smart homes app
    sh_app = SmartHomesApp()
    sh_app.run()
test_smart_homes_app()
