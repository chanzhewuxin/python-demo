class Animal(object):
    def run(self):
        print('Animal is running.')

class Dog(Animal):
     

    def run(self):
        print('Dog also is animal.')

class Pig(Animal):
    pass

dog = Dog()
dog.run()
# dog = Animal()
# dog.run()

# print(isinstance(dog,Animal))

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Dog())
run_twice(Pig())