class MyClass:
    pass
class Dog:
    species = "Canis familiaris"


    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} barks!"

    def dog_math(self, num1, num2):
        answer = num1 + num2
        return f"{num1} + {num2} = snack time for {self.name}, and {answer} for hoomans."

dog1 = Dog("Axel", 4)
dog2 = Dog("Max", 2)

dog1 = Dog("Axel", 4)
print(dog1.bark()) # Outputs: Axel barks

class GermanShepard(Dog):
    def guard(self):
        return f"{self.name} is guarding!"
    
gs_dog = GermanShepard("Dax", 5)
print(gs_dog.guard()) #Outputs: Dax is guarding!

print(dog1.name)
print(dog1.age)
print(dog2.name)
print(dog2.age)
print(dog1.dog_math(3, 12))
print(dog2.dog_math(2, 8))
