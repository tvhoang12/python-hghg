class Animal:
    
    alive = True
    
    def eat(self):
        print("This animal is eating.")
    def sleep(self):
        print("This animal is sleeping.")
    def drink(self):
        print("This animal is drinking.")

class Rabbit(Animal):
    
    def run(self):
        print("This rabbit is running.")

class Fish(Animal):
    
    def swim(self):
        print("This fish is swimming.")

class Hawk(Animal):
    
    def eat(self):
        print("this Hawk is eating fish.")
    def fly(self):
        print("This hawk is flying.")

class goldenFish(Fish):
    def color(self):
        print("This fish is golden.")
hawk = Hawk()
hawk.eat()

class dog(Animal):
    def bark(self):
        print("This dog is barking.")
        
class golden(dog, Fish):
    
    def __init__(self):
        self.Dog = dog()
        self.fish = Fish()
        
    def fis(self):
        print("This is golden fish.")
    
    def dog(self):
        print("This is golden dog.")

# fish = goldenFish()
# print(fish.alive)
# fish.swim()
# fish.eat()

Golden = golden()
Golden.bark()
Golden.fis()
Golden.eat()