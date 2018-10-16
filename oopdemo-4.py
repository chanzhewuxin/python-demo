class Animal(object):
    pass


class Mammal(Animal):
    pass


class Runnalbe(object):
    def run(self):
        print('Running...')


class Dog (Mammal, Runnalbe):
    pass
