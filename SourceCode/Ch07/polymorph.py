class Device:
    def power_on(self):
        pass

class Smartphone(Device):
    def power_on(self):
        print ("Smartphone is powering on...")

class Laptop(Device):
    def power_on(self):
        print ("Laptop is booting up...")

class SmartTV(Device):
    def power_on(self):
        print ("Smart TV is starting up...")



myphone = Smartphone()
mylaptop = Laptop()
mytv = SmartTV()



myphone.power_on()
mylaptop.power_on()
mytv.power_on()
