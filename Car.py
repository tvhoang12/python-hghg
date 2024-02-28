class Car:
    def __init__(self, make, name, year, color):
        self.make = make
        self.name = name
        self.year = year
        self.color = color
    
    def drive(self):
        print("you are driving a" + self.name + "car")
    def stop(self):
        print("you have stopped the car")