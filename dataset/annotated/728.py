def get_cat_speak(name: str) -> str:
    class Animal:
        def __init__(self, name: str):
            self.name = name

    class Cat(Animal):
        def speak(self) -> str:
            return '{} meows.'.format(self.name)

    cat = Cat(name)
    return cat.speak()

