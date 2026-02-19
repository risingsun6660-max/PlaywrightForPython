class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def creativity(self,coding):
        return "{} knows {}".format(self.name,coding)
    
    def gender(self,gen):
        return "{} is a {}".format(self.name,gen)
    
person1 = Person("john","50")
person2 = Person("ben","60")

print(person1.name,person1.age)
print(person2.name,person2.age)
print(person1.creativity("python"))
print(person1.gender("male"))