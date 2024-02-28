class car:
    def turnOn(self):
        print("This car is turning on.")
        return self
    
    def turnOff(self):
        print("This car is turning off.")
        return self
    
Car = car()
Car.turnOn().turnOff()