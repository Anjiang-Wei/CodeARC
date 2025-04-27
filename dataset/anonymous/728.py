def solution(name):
    class Animal:
        def __init__(self, name):
            self.name = name

    class Cat(Animal):
        def speak(self):
            return '{} meows.'.format(self.name)

    cat = Cat(name)
    return cat.speak()

